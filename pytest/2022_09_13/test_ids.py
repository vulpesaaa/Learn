# content of test_ids.py
import pytest

# 测试id,字符串形式,类似字典中的键值对中的键key
@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param


def test_a(a):
    pass


def idfn(fixture_value):
    if fixture_value == 0:
        return "eggs"
    else:
        return None

#fixture idfn传递字符串作为ids，如果返回的是None则默认根据参数名生成一个字符串
@pytest.fixture(params=[0, 1], ids=idfn)
def b(request):
    return request.param


def test_b(b):
    pass