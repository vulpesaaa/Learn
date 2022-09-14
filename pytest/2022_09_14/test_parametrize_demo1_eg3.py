# -*- encoding: utf-8 -*-
'''
@File    :   test_parametrize_demo1_eg3.py
@Time    :   2022/09/14 12:02:52
@Author  :   lmz
@Email   :   lumengzhen@wangtengtech.com
@GitLab  :   http://10.25.10.111:8088/lumengzhen/Learn
@Copyright : 侵权必究
'''

# here put the import lib

import pytest
pytestmark = pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])

@pytest.fixture
def fun():
    return 'fun'


# eg3:验证全局变量，参数化模块中的所有测试
class TestClass:
    def test_simple_case(self,n,expected):
        assert n+1 == expected

    def test_weird_simple_case(self,n,expected):
        assert (n*1) +1 == expected

    # 即使不用到n,expected 也需要传递参数
    def test_no_param(self,fun,n,expected):
        assert 'fun' == fun