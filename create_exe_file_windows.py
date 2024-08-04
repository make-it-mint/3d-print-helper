import PyInstaller.__main__
#creates a standalone windows executable in a new sub directory "dist"
#pyInstaller required --> Documentation: https://pyinstaller.org/en/v4.1/usage.html
#manually add following files & directories to the directory of the new executable
#- settings.py, slicerpath.txt, ui.py and config_files directory
PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--windowed'
])