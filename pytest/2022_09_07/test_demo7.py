# contents of test_append.py
import pytest

# eg1 : fixture重复使用demo 每个测试获取自己干净的数据 测试之间独立互不干扰
# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


# test_string和test_int都重新请求了order这个fixture，互不干扰,在对应的测试中有效，而不是同一对象
def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]


def test_int(order):
    # Act
    order.append(2)

    # Assert
    assert order == ["a", 2]