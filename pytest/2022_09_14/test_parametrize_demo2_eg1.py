from email import header

# -*- encoding: utf-8 -*-
'''
@File    :   test_parametrize_demo2_eg1.py
@Time    :   2022/09/14 15:02:52
@Author  :   lmz
@Email   :   lumengzhen@wangtengtech.com
@GitLab  :   http://10.25.10.111:8088/lumengzhen/Learn
@Copyright : 侵权必究
'''

# here put the import lib

import pytest

# eg1: coftest.py 中pytest_generate_tests在收集测试函数中被调用
# pytest -q -rs -v  test_parametrize_demo2_eg1.py
# pytest -q --stringinput="hello" --stringinput="world" test_parametrize_demo2_eg1.py
def test_valid_string(stringinput):
    assert stringinput.isalpha() # 检测字符串是否只由字母或中文文字组成
