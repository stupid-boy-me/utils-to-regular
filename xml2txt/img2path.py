# -*- coding: utf-8 -*-
# @Time : 2021/9/7 14:03
# @Author : 黄小渣
# @FileName: img2path.py
# @Software: PyCharm
#function:实现获取图片的路径
import os

list1 = []
def get_path(input_path):
    filenames = os.listdir(input_path)
    for file in filenames:
        dir_filename_path = os.path.join(input_path,file)
        list1.append(dir_filename_path)
        with open(output_path,'w') as f:
            for i in list1:
                f.writelines(i)
                f.writelines('\n')




if __name__ == "__main__":
    path = 'C:/Users/Administrator/Desktop/input/cover/'
    output_path = 'C:/Users/Administrator/Desktop/path.txt'
    get_path(path)