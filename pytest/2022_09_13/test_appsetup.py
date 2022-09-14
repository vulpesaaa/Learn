# content of test_appsetup.py
import pytest


class App:
    def __init__(self,smtp_connection):
        self.smtp_connection = smtp_connection

# 定义一个fixture为app，接收前面的smtp_connection，并将其实例化为一个app对象
@pytest.fixture(scope="module")
def app(smtp_connection):
    return App(smtp_connection)

def test_smtp_connection_exists(app):
    assert app.smtp_connection