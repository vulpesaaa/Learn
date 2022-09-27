import pytest
"""
demo1_eg1:断言3是否等于4
"""
def f():
    return 3


def test_function():
    assert f() == 4