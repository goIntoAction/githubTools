#!/usr/bin/env python
#coding=utf8

import os
dir = raw_input("输入文件夹：")
for d in os.listdir(dir):
    path = os.path.join(dir, d)
    if os.path.isdir(path):
        os.system("cd " + path + ";git pull")
