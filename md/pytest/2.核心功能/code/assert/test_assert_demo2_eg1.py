"""
抛出一个异常
"""
import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0