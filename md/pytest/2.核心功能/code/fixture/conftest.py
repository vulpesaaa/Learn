import sys
import pytest
import smtplib

# 
# # 参数scope="module" 多个测试模块可使用smtp_connection这个fixture
# @pytest.fixture(scope="module")
# def smtp_connection():
#     return smtplib.SMTP("smtp.qq.com", 587, timeout=5)


# # test_fixture_demo6_eg1
# @pytest.fixture(scope="module")
# def smtp_connection(request):
#     server = getattr(request.module, "smtpserver", "smtp.gmail.com")
#     smtp_connection = smtplib.SMTP(server, 587, timeout=5)
#     yield smtp_connection
#     print("finalizing {} ({})".format(smtp_connection, server))
#     smtp_connection.close()


# test_fixture_demo7_eg1
@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection
    print("finalizing {}".format(smtp_connection))
    smtp_connection.close()


