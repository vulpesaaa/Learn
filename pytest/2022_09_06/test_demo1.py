import pytest
"""
-q以“安静”报告模式执行测试
pytest -q test_sysexit.py
pytest将在当前目录及其子目录中运行 ​test_*.py​ 或 ​*_test.py​ 形式的所有文件。
"""

def func(x):
    return x+1

def test_answer():
    # assert 断言判断func(3)是否满足期望值
    assert func(3) == 5

def f():
    # 抛出异常
    raise SystemExit(1)


def test_mytest():
    # raises断言f()代码引发了SystemExit异常
    with pytest.raises(SystemExit):
        f()