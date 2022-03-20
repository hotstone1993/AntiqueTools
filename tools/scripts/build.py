#!/usr/bin/python3

import os
import subprocess

BUILD_DIR = '../../build'

if not os.path.isdir(BUILD_DIR):
    os.mkdir(BUILD_DIR)
os.chdir(BUILD_DIR)
subprocess.call(['cmake', '..'])
subprocess.call(['cmake', '--build', '.'])