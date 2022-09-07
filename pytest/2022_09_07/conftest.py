import sys
# 禁止将断言重写的模块写入缓存，即.pyc​ 文件不会缓存在磁盘
# 在只读文件系统或 zip 文件中，重写将静默跳过缓存，即无法写入.pyc文件
sys.dont_write_bytecode = True


from test_demo3 import Foo
# 自定义输出
def pytest_assertrepr_compare(op,left,right):
    # isinstance(left, Foo)判断left是Foo类型
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            "   vals: {} != {}".format(left.val, right.val),
        ]



import pytest
import smtplib

# 参数scope="module" 多个测试模块可使用smtp_connection这个fixture
@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.qq.com", 587, timeout=5)