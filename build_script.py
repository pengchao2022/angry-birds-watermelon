import PyInstaller.__main__
import os


# 显式定义图标的正确路径
icon_path = os.path.join('assets', 'images', 'angry_bird.icns')

# 检查图标是否存在
if not os.path.exists(icon_path):
    print(f"⚠️ 警告: 未找到图标文件 {icon_path}, 将不使用自定义图标。")
    icon_arg = []
else:
    print(f"✅ 找到图标文件: {icon_path}")
    icon_arg = [f'--icon={icon_path}']

PyInstaller.__main__.run([
    'main.py',
    '--name=AngryBirdsWatermelon',
    '--windowed',
    '--onedir',
    # 将 assets 文件夹整体打包进去
    '--add-data=assets:assets', 
    '--noconfirm',
    '--clean',
] + icon_arg)

