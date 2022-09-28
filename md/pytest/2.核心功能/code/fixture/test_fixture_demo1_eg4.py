import pytest

# 一个test/fixture一次可以请求多个fixture
@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture
def second_entry():
    return 2

# order作为fixture请求2个fixture,分别是first_entry和second_entry
@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]

@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]

# test_string作为test请求2个fixture,分别是order和expected_list
def test_string(order, expected_list):
    # Act
    order.append(3.0)

    # Assert
    assert order == expected_list