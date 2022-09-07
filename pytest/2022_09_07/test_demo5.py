import pytest
# eg1:fixture demo

@pytest.fixture
def f():
    return 3

def f1():
    return 1

# 获取fixture f的返回值
def test_one(f):
    assert f == 1

# f1函数的返回值
def test_two(f1=f1()):
    assert f1 ==1