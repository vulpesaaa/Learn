import os
import pytest

# 这个测试类中的所有测试用例都可使用cleandir，不需要直接访问fixture对象
@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile","w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd())==[]

# 此测试类验证mark.usefixtures在类级别生效
class TestNoUsefixtures:
    def test_cwd(self):
        assert os.listdir(os.getcwd()) == []

