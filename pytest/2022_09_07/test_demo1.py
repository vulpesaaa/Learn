import pytest
# eg1: 判断抛出异常 
def test_zero_division():
    # 判断抛出的异常是否是ZeroDivisionError异常
    with pytest.raises(ZeroDivisionError):
        1 / 0


# eg2: 异常实例，value属性
def test_recursion_depth():
    with pytest.raises(RecursionError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)



# eg3:match 正则表达式匹配异常的字符串表达式
def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    # Regex pattern 匹配规则，163和包含123的不匹配，可改成163测试一下
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()


# eg4:@pytest.mark.xfail 如果抛出的异常是IndexError类型，则执行结果为xpassed否则为xfailed
def f():
    i =[]
    print(i[2])

@pytest.mark.xfail(raises=IndexError)
def test_f():
    f()


