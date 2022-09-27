import pytest

def func(x):
    return x+1

def test_answer():
    # assert 断言判断func(3)是否满足期望值
    assert func(3) == 5