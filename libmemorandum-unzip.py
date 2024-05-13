#!/data/data/com.termux/files/usr/bin/python3
# "Name: LIBMEMORANDUM-UNZIP (v0.01), Created by: Luis Adha (c) (2024) GNU/GPLv3"
import sys
import os
import subprocess
import shutil
import glob

if len(sys.argv) < 2:
    print("Argument required!")
    sys.exit()

subprocess.run(['unzip', '-o', sys.argv[1]], stdout=subprocess.DEVNULL)