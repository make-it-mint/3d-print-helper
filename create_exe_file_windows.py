import shutil

import PyInstaller.__main__

# creates a standalone windows executable in a new sub directory "dist"
# pyInstaller required --> Documentation: https://pyinstaller.org/en/v4.1/usage.html
# adds following files & directories to the directory of the new executable
# - settings.py, slicerpath.txt, modelpath.txt, ui.py and config_files directory
PyInstaller.__main__.run(["main.py", "--onefile", "--windowed"])

shutil.copy("settings.py", "dist/settings.py")
shutil.copy("modelpath.txt", "dist/modelpath.txt")
shutil.copy("slicerpath.txt", "dist/slicerpath.txt")
shutil.copy("ui.py", "dist/ui.py")
shutil.copytree("config_files", "dist/config_files")
