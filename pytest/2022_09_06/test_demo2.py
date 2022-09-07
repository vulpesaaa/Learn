# 发现以test_前缀的函数，所以无需任何子类
# 前提所有类前必须要有Test，否则会跳过该类
# 传递文件名，即可使用该模块
# eg:pytest -q demo2.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")