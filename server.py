# server.py
"""
MCP服务器主模块，提供DEMO功能
"""

from typing import Dict, Any
from fastmcp import FastMCP
from pydantic import Field

from jewei_demo_mcp_server.app_config import config
from jewei_demo_mcp_server.core import helloworld

# 创建MCP服务器实例
mcp = FastMCP(name=config.SERVER_NAME)

@mcp.tool()
def hello(name: str) -> Dict[str, Any]:
    """返回问好内容
    
    Args:
        name: 你的名字
        
    Returns:
        包含问好结果的字典，格式为：
        {
            "text": [问好内容],
            "code": [代号]
        }
    """
    return helloworld()


@mcp.resource(
    uri="data://sql_describe",      # Explicit URI (required)
    name="sql语句编写规范",     # Custom name
    description="sql语句编写规范和说明（在编写sql语句前必看）", # Custom description
    mime_type="text/plain", # Explicit MIME type
    tags={"必看", "规范"} # Categorization tags
)
def sql_describe() -> str:
    """sql语句编写规范和说明（在编写sql语句前必看）"""
    ret = f'''
    SQL语句编写规范：
    
    1. 安全限制：只允许执行SELECT语句
    2. 不允许使用以下关键字：insert, update, delete, drop, alter, create, truncate, exec, execute
    3. 查询语句应尽量简洁，避免复杂的子查询和连接
    4. 查询结果行数应控制在合理范围内，避免返回过多数据
    5. 使用参数化查询，避免SQL注入风险
    6. 表名和列名应使用反引号(``)包裹，避免与MySQL关键字冲突
    7. 使用适当的WHERE条件限制查询范围
    8. 避免使用SELECT *，应明确指定需要的列
    '''
    return ret

@mcp.prompt(
    name="introduction",  # Custom prompt name
    description="当用户问好时",  # Custom description
    tags={"hello", "你好"}  # Optional categorization tags
)
def introduction_prompt(
    user_name: str = Field(description="用户姓名，非必填")
) -> str:
    """当用户问好时，需要生成的用户消息."""
    return f"用户名叫 '{user_name}' ，你需要友好的回复对方的问好，需要有Emoji表情，且要使用中文 ."

def main():
    """主函数，用于启动MCP服务器"""
    print("启动 MySQL MCP 服务器...")
    mcp.run()
    # To use a different transport, e.g., HTTP:
    # mcp.run(transport="streamable-http", host="127.0.0.1", port=9000)

if __name__ == "__main__":
    main()