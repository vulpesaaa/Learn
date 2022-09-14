import pytest

# eg3:验证模块级别的fixture重写,重写/test/conftest.py的username
@pytest.fixture
def username(username):
    return 'overriden-else-'+ username


def test2_username(username):
    assert username == 'overriden-else-username'

# eg4:验证用非参数化fixture覆盖参数化fixture,此处测试用例test3是参数化fixture，test4是非参数化fixture
def test3_username(parametrized_username):
    assert parametrized_username in ['one','two','three']

def test4_username(non_parametrized_username):
    assert non_parametrized_username == 'username'