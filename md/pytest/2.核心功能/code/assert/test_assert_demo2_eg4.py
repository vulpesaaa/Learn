import pytest
"""
demo2_eg4:@pytest.mark.xfail 如果抛出的异常是IndexError类型,则执行结果为xpassed否则为xfailed
"""
# 
def f():
    i =[]
    print(i[2])

@pytest.mark.xfail(raises=IndexError)
def test_f():
    f()
