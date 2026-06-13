import tomllib
import sys
import os

def get_app_version():
    """从 pyproject.toml 读取版本号"""
    # 逻辑逻辑：指向项目根目录下的 pyproject.toml
    # 注意：如果 constants.py 在 src/utils/ 下，要往上回退两级
    if hasattr(sys, '_MEIPASS'):
        toml_path = os.path.join(sys._MEIPASS, 'pyproject.toml')
    else:
        # 这里使用 os.path.abspath 确保路径定位到根目录
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        toml_path = os.path.join(base_dir, 'pyproject.toml')
        
    try:
        with open(toml_path, "rb") as f:
            data = tomllib.load(f)
            return data["project"]["version"]
    except Exception:
        return "0.0.0"