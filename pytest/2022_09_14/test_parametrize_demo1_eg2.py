# -*- encoding: utf-8 -*-
'''
@File    :   test_parametrize_demo1_eg2.py
@Time    :   2022/09/14 12:02:52
@Author  :   lmz
@Email   :   lumengzhen@wangtengtech.com
@GitLab  :   http://10.25.10.111:8088/lumengzhen/Learn
@Copyright : 侵权必究
'''

# here put the import lib

import pytest

# eg2:验证测试类带有参数集的函数会被调用
@pytest.mark.parametrize("n,expected",[(1,2),(3,4)])
class TestClass:
    def test_simple_case(self,n,expected):
        assert n+1 == expected

    def test_weird_simple_case(self,n,expected):
        assert (n*1) +1 == expected
