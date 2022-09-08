# contents of test_append.py
import pytest


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return []

# 自动适配fixture,["a"]
@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)

# 都依赖于order对象,由于autouse=True,append_first已经自动适配,order已经更新为['a'],在请求order时不再是[]
# scope默认是function,生命周期为1个测试用例,下面有2个测试用例
def test_string_only(order, first_entry):
    print("\ntest_string_only\t",order)
    assert order == [first_entry]
    # 生命周期到一个测试结束,不影响下一个测试,仍为['a']
    order.append(3)


def test_string_and_int(order, first_entry):
    print("\ntest_string_and_int\t",order)
    order.append(2)
    assert order == [first_entry, 2]