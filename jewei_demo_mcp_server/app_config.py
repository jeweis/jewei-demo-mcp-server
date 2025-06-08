# app_config.py
"""
配置模块，用于管理应用程序配置
"""

import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    """配置类，用于管理应用程序配置"""
    
    # 测试配置
    DB_USER = os.getenv("DB_USER", "root")
    
    # 服务器配置
    SERVER_NAME = os.getenv("SERVER_NAME", "JEWEI-DEMO-Server")
    
    # 连接字符串
    @property
    def CONNECTION_STRING(self):
        """构建字符串"""
        return f"{self.DB_USER}测试"

# 创建默认配置实例
config = Config()