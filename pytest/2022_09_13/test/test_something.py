import pytest

# # eg1：验证文件夹级别的fixture重写 eg2需注释掉否则会影响, /test/subfolder/conftest.py被重写，此为重写前的测试用例
# def test_username(username):
#     assert username == 'username'

# eg2:验证模块级别的fixture重写,重写/test/conftest.py的username
@pytest.fixture
def username(username):
    return 'overriden-' + username

def test1_username(username):
    assert username == 'overriden-username'

# eg3:验证覆盖具有直接测试参数化的fixture
@pytest.mark.parametrize('username',['directly-overridden-username'])
def test2_username(username):
    assert username == 'directly-overridden-username'

@pytest.mark.parametrize('username',['directly-overridden-username-other'])
def test3_username(other_username):
    assert other_username == 'other-directly-overridden-username-other'


# eg4:验证用非参数化fixture覆盖参数化fixture

#参数化的fixture被非参数化版本覆盖
@pytest.fixture
def parametrized_username():
    return 'overriden-username'
#非参数化的fixture被参数化版本覆盖
@pytest.fixture(params=['one','two','three'])
def non_parametrized_username(request):
    return request.param

def test4_username(parametrized_username):
    assert parametrized_username == 'overriden-username'

def test5_username(non_parametrized_username):
    assert non_parametrized_username in ['one','two','three']


