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


def test_string_only(order, first_entry):
    print("\ntest_string_only\t",order)
    assert order == [first_entry]


def test_string_and_int(order, first_entry):
    print("\ntest_string_and_int\t",order)
    order.append(2)
    assert order == [first_entry, 2]