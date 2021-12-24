# -*- coding: utf-8 -*-
# @Time : 2021/9/7 9:43
# @Author : 黄小渣
# @FileName: movejpg.py
# @Software: PyCharm
import os
import shutil
in_file = 'C:/Users/Administrator/Desktop/data'
out_file = 'C:/Users/Administrator/Desktop/picture'
files_name = os.listdir(in_file)
for i in files_name:
    if i[-3:] == 'txt':
        shutil.copyfile(os.path.join(in_file,i),os.path.join(out_file,i))
print('完成')

