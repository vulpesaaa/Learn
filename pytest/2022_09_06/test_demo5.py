import pytest
def test_one():
    a =2
    assert a%2 ==1 ,"value was odd"


def test_assert():
    # 内置0异常
    with pytest.raises(ZeroDivisionError) :
        1/0