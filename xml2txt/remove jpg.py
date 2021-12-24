# -*- coding: utf-8 -*-
# @Time : 2021/9/7 10:24
# @Author : 黄小渣
# @FileName: remove jpg.py
# @Software: PyCharm
import os
in_file = 'D:/Project/longyue/yolo_longyue/xml'
file_names = os.listdir(in_file)
for file in file_names:
    if file[-3:] == 'xml':
        dir = os.path.join(in_file,file)
        os.remove(dir)