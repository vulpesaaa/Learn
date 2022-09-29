---
tags: [安装, 测试框架, 单元测试, pytest, python]
title: pytest-1安装
created: '2022-09-22T08:02:18.223Z'
modified: '2022-09-22T08:13:20.904Z'
---

# pytest-1安装
## 一、安装
## 二、demo
## 三、执行测试用例
## 四、其他
### 1.命令行参数
### 2.分析测试执行时间
### 3.管理插件的加载
### 4.调用pytest

# pytest-1安装
简介：pytest是一个基于python的单元测试框架
## 一、安装
前提条件：python3.7+PyPy3

在cmd或终端中输入以下命令
    
    > pip install pytest

下载失败可使用以下命令

    > pip install pytest  -i https://pypi.douban.com/simple/

验证是否安装

    > pytest --version
    > pytest 7.1.0

```
pytest --version
pytest 7.1.0
```

## 二、demo
测试用例py文件的命名规范为test_* 和*_test函数，

函数名的格式为test_* 和*_test

类名的格式为Test* 

参照上述原则，创建第一个demo用例test_demo.py


执行测试用例，在终端中，执行当前测试用例
pytest test_demo.py


## 三、执行测试用例
## 四、其他
### 1.命令行参数
### 2.分析测试执行时间
### 3.管理插件的加载
### 4.调用pytest
