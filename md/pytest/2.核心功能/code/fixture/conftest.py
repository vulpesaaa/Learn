import sys
import pytest
import smtplib

# 参数scope="module" 多个测试模块可使用smtp_connection这个fixture
@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.qq.com", 587, timeout=5)