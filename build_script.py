import PyInstaller.__main__
import os
import plistlib

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

# 2. 打包后修改 Info.plist
def update_app_display_name(app_path, display_name):
    plist_path = os.path.join(app_path, 'Contents', 'Info.plist')
    if os.path.exists(plist_path):
        with open(plist_path, 'rb') as f:
            plist = plistlib.load(f)
        
        # 设置显示名称 (CFBundleDisplayName 是 Finder 中看到的名字)
        plist['CFBundleDisplayName'] = display_name
        
        with open(plist_path, 'wb') as f:
            plistlib.dump(plist, f)
        print(f"✅ 已成功将显示名称修改为: {display_name}")
    else:
        print(f"❌ 错误: 未找到 Info.plist 文件于 {plist_path}")

# 执行修改：将 'AngryBirdsWatermelon' 修改为你想显示的 'Angry Birds Watermelon'
update_app_display_name('dist/AngryBirdsWatermelon.app', 'Angry Birds')