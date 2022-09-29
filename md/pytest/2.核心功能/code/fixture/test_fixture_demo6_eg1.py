# eg:fixture可以内省请求的测试上下文 ，conftest.py
smtpserver = "mail.python.org"  # will be read by smtp fixture
# smtp_connection fixture​​函数从模块名称空间获取我们的邮件服务器名称
def test_showhelo(smtp_connection):
    assert 0, smtp_connection.helo()