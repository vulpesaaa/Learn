# content of conftest.py
import pytest
import smtplib

# params有2个参数，一个测试则运行两次smtp_connection实例
@pytest.fixture(scope="module", params=["smtp.qq.com", "mail.python.org"])
def smtp_connection(request):
    # request.param访问一个值，而非params，否则会提示 AttributeError: 'SubRequest' object has no attribute 'params'错误
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection
    print("finalizing {}".format(smtp_connection))
    smtp_connection.close()



import pytest
import os
import tempfile
# 创建临时空目录，结束后自动切换到原目录
@pytest.fixture
def cleandir():

    with tempfile.TemporaryDirectory() as newpath: #创建一个临时目录
        old_cwd = os.getcwd()   # 获取当前路径，运行脚本的路径而非脚本所在目录
        os.chdir(newpath)       # 切换到指定目录，此处是切换到临时目录
        yield
        os.chdir(old_cwd)       # 切换到当前目录