#Title : SimpleMD5Checksum
#Version : 0.1
#Author : Yi 'Pusungwi' Yeon Jae
#Description : Simple creating md5 checksum PyQt4 script

import sys
from cx_Freeze import setup, Executable

base = "Win32GUI"
build_options = {"packages": ["sys", "hashlib"], "includes": ["re"]}

setup(
    name = "SimpleMD5Checksum",
    version = "0.1",
    description = "Simple creating md5 checksum to use PyQt4 script",
    options = {"build_exe" : build_options},
    executables = [Executable("main.py", base = base)]
)
