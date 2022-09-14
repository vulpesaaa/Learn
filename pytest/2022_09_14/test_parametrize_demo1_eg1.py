# -*- encoding: utf-8 -*-
'''
@File    :   test_parametrize_demo1_eg1.py
@Time    :   2022/09/14 12:02:52
@Author  :   lmz
@Email   :   lumengzhen@wangtengtech.com
@GitLab  :   http://10.25.10.111:8088/lumengzhen/Learn
@Copyright : 侵权必究
'''

# here put the import lib

import pytest

# eg1:检查某个输入是否会导致预期的输出,作用域：测试函数
# @parametrize​ 装饰器定义了三个不同的 ​(test_input,expected)元组，以便 ​test_eval ​函数将依次使用它们运行 3 次
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+4",6),("6*9",42)])
def test_eval(test_input,expected):
    assert eval(test_input) == expected

