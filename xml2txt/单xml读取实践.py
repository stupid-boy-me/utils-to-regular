#success
# -*- coding: utf-8 -*-
# @Time : 2021/9/7 10:55
# @Author : 黄小渣
# @FileName: 单xml读取实践.py
# @Software: PyCharm
'''读取单个xml文件进行实践'''
import os
import xml.etree.ElementTree as ET

def read_information(file_path):
    tree = ET.parse(file_path)
    #获取宽和高
    a = tree.find('size')
    w, h = [int(a.find('width').text),
            int(a.find('height').text)]
    name = tree.find('object').find('name').text
    if name == 'damage':
        label = 1
    else:
        label = 0
    # 读取检测框的左上、右下角点的坐标
    bbox = tree.find('object').find('bndbox')
    x1,y1,x2,y2 = [int(bbox.find('xmin').text),
                   int(bbox.find('ymin').text),
                   int(bbox.find('xmax').text),
                   int(bbox.find('ymax').text)]

    # 这里也很关键，yolov5需要中心点以及宽和高的标注信息，并且进行归一化，
    # 下边label后边的四个值即是归一化后保留4位有效数字的x，y，w，h
    obj_struct = [label,
                  round((x1+x2)/(2.0*w),4),
                  round((y1+y2)/(2.0*h),4),
                  round((x2-x1)/(w),4),
                  round((y2-y1)/(h),4)]
    # print(obj_struct)  # 这里是单个xml，如果是多个的话，需要创建一个list来进行包裹
    return obj_struct

if __name__ == '__main__':
    t = ''
    file_path = 'C:/Users/Administrator/Desktop/0001.xml'
    result = read_information(file_path)
    out_path = 'C:/Users/Administrator/Desktop/1.txt'
    print(result)
    with open(out_path,'w') as f:
        for a in result:
            t = t + str(a) + '   '
        f.writelines(t)


