from email import header

# -*- encoding: utf-8 -*-
'''
@File    :   test_parametrize_demo2_eg2.py
@Time    :   2022/09/14 15:02:52
@Author  :   lmz
@Email   :   lumengzhen@wangtengtech.com
@GitLab  :   http://10.25.10.111:8088/lumengzhen/Learn
@Copyright : 侵权必究
'''

# here put the import lib

import pytest

def test_compute(param1):
    assert param1 < 4 