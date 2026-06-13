import sys
import os

def get_app_version():
    """从 pyproject.toml 读取版本号"""
    # 确定路径：开发环境下在根目录，打包后在 _MEIPASS 目录下
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    toml_path = os.path.join(base_path, 'pyproject.toml')
    
    try:
        # 使用简单的文本处理，不依赖 tomllib，兼容性最好
        with open(toml_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('version ='):
                    # 提取引号内的版本号: version = "1.0.1" -> 1.0.1
                    return line.split('"')[1]
    except Exception:
        # 如果读取失败，返回默认值，确保程序能启动
        return "0.0.0"
    return "0.0.0"