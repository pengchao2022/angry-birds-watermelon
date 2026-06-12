import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'main.py',                    # 入口文件在根目录
    '--name=AngryBirdsWatermelon',
    '--windowed',
    '--onedir',                   # 使用文件夹模式保证启动速度
    '--noconfirm',
    '--clean',
    # 关键：将 assets 文件夹完整打包进去
    '--add-data=assets:assets',
    '--icon=angry_bird.png',      # 如果你有 .icns 格式最好，没有则用 png
])