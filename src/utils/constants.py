import os
import sys
import tomllib

"""
游戏常量定义
"""

def get_resource_path(relative_path):
    """
    获取资源文件的绝对路径。
    PyInstaller 打包后，资源会被放置在临时目录中，
    通过 sys._MEIPASS 获取该目录路径。
    """
    try:
        # PyInstaller 创建的临时文件夹路径
        base_path = sys._MEIPASS
    except Exception:
        # 开发环境下，直接使用当前工作目录
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# 屏幕尺寸
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
RED = (231, 76, 60)
GREEN = (46, 204, 113)
BLUE = (52, 152, 219)
ORANGE = (230, 126, 34)
PURPLE = (155, 89, 182)
BROWN = (121, 85, 72)
DARK_BROWN = (93, 64, 55)
SKY_BLUE = (135, 206, 235)
GRASS_GREEN = (56, 142, 60)
CLOUD_WHITE = (248, 249, 250)
YELLOW = (241, 196, 15)
PINK = (255, 182, 193)
LIGHT_BLUE = (173, 216, 230)
WATERMELON_GREEN = (60, 179, 113)
WATERMELON_RED = (220, 20, 60)
WATERMELON_PINK = (255, 105, 180)
WATERMELON_DARK_GREEN = (34, 139, 34)

# 小羊颜色
SHEEP_WHITE = (255, 255, 255)
SHEEP_PINK = (255, 182, 193)
SHEEP_LIGHT_BLUE = (173, 216, 230)
SHEEP_LIGHT_GREEN = (144, 238, 144)
SHEEP_LIGHT_PURPLE = (216, 191, 216)
SHEEP_COLORS = [SHEEP_PINK, SHEEP_LIGHT_BLUE, SHEEP_LIGHT_GREEN, SHEEP_LIGHT_PURPLE]

# 游戏参数
GRAVITY = 0.3
LAUNCH_POWER = 0.4
MAX_PULL_DISTANCE = 80
BIRD_RADIUS = 20
SHEEP_RADIUS = 25