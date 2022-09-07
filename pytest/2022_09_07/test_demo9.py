
# 每个测试可以请求fixture多次(缓存返回值)
# contents of test_append.py
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order():
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)

# 同一个测试期间，append_first请求了order,order 的返回值被缓存,所以此次的访问order对象是同一个,即值仍旧是["a"]
def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]