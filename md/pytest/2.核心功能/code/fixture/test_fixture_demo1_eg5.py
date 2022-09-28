# 每个测试可以请求fixture多次(缓存返回值)
import pytest


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order():
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)

@pytest.fixture
def append_two(order,first_entry):
    return order.append(first_entry)

# 同一个测试期间，append_first请求了order,order 的返回值被缓存,所以此次的访问order对象是同一个,即值仍旧是["a"]
def test_string_only(append_first, order, first_entry):
    print("\n",append_first,order,first_entry)
    # Assert
    assert order == [first_entry]

# 请求新的测试对象, 请求append_first之后order对象更新为['a'] , 请求append_two后order对象在['a']的基础上更新为['a','a']
def test_string_two(append_first,append_two, order, first_entry):
    print("\n",append_first,append_two,order,first_entry)
    assert order == [first_entry,first_entry]