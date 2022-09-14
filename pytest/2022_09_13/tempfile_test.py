import os
import pytest
# 验证在模块级别，fixture都生效
# 关键字必须为pytestmark 
# 注释后可验证pytest.ini是否全项目生效
pytestmark = pytest.mark.usefixtures("cleandir")

class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile","w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd())==[]

class TestNoUsefixtures:
    def test_cwd(self):
        assert os.listdir(os.getcwd()) == []

