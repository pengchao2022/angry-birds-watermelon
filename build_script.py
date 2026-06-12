import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'main.py',                    
    '--name=AngryBirdsWatermelon',
    '--windowed',
    '--onedir',                   
    '--noconfirm',
    '--clean',
    '--add-data=assets:assets',
    '--icon=angry_bird.icns',     
])