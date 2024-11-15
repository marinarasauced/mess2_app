import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "mess2",
    version = "1.0",
    description = "Modular Experiment Software System 2",
    author = "Marina J. Nelson",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
