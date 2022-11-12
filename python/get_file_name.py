# -*- coding: utf-8 -*-

import os


# 获取指定路径所有子文件和子目录
def get_path_filename(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件


# 返回指定路径下特定类型的文件
def get_type_filename(file_dir, filetype):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == filetype:
                L.append(os.path.join(root, file))
    return L


def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif os.path.splitext(file_path)[1] =='.jpeg':
            list_name.append(file_path)


get_path_filename(file_dir="C:\\Users\\Administrator\\Desktop\\过滤包")

# py = get_type_filename(file_dir="C:\\Users\\Administrator\\PycharmProjects\\LearnShell\\python", filetype=".py")
# print(py,py文件')

