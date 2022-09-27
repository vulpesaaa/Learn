import pytest
"""
demo2_eg3:match 正则表达式匹配异常的字符串表达式
"""
def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    # Regex pattern 匹配规则，163和包含123的不匹配，可改成163测试一下
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()

