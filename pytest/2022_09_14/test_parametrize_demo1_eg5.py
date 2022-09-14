# -*- encoding: utf-8 -*-
'''
@File    :   test_parametrize_demo1_eg4.py
@Time    :   2022/09/14 14:54:10
@Author  :   lmz
@Email   :   lumengzhen@wangtengtech.com
@GitLab  :   http://10.25.10.111:8088/lumengzhen/Learn
@Copyright : 侵权必究
'''

# here put the import lib

import pytest
# eg5: 获取多个参数化参数的组合，堆栈参数化装饰器
# x=0/y=2、x=1/y=2、x=0/y=3 和 x=1/y=3
@pytest.mark.parametrize("x",[0,1])
@pytest.mark.parametrize("y",[2,3])
def test_foo(x,y):
    pass