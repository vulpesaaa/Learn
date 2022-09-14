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
# eg4: 在参数化中标记单个测试实例
# "6*9",42失败标记为xfailed
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+4",6),pytest.param("6*9",42,marks=pytest.mark.xfail,id="xfailed")])
def test_eval(test_input,expected):
    assert eval(test_input) == expected