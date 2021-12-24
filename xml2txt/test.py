# -*- coding: utf-8 -*-
# @Time : 2021/9/7 11:44
# @Author : 黄小渣
# @FileName: test.py
# @Software: PyCharm
import os
import xml.etree.ElementTree as ET

def read_information(file_path):
    tree = ET.parse(file_path)
    #获取宽和高
    a = tree.find('size')
    b = tree.findall('size')
    print(a)
    print(b)


if __name__ == '__main__':
    file_path = 'C:/Users/Administrator/Desktop/0001.xml'
    read_information(file_path)