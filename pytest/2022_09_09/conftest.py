# content of conftest.py
import pytest
import smtplib

# 范围是模块
@pytest.fixture(scope="module")
def smtp_connection(request):
    # 此fixture可接收一个请求对象request
    # request的模块属性可获得一个smtpserver属性的测试模块
    # 即test_anothersmtp.py测试模块中的smtpserver属性
    server = getattr(request.module, "smtpserver", "smtp.qq.com")
    smtp_connection = smtplib.SMTP(server, 587, timeout=5)
    yield smtp_connection
    print("finalizing {} ({})".format(smtp_connection, server))
    smtp_connection.close()