import pytest
def pytest_generate_tests(metafunc):
    if "db" in metafunc.fixturenames:
        metafunc.parametrize("db", ["d1", "d2"], indirect=True)


class DB1:
    "one database object"


class DB2:
    "alternative database object"


@pytest.fixture
def db(request):
    if request.param == "d1":
        return DB1()
    elif request.param == "d2":
        return DB2()
    else:
        raise ValueError("invalid internal test config")
    

"""
测试函数的参数化仅发生在收集阶段,这在仅运行test时才设置昂贵的资源比如DB连接或是subprocess时非常有用

db fixture在设置阶段已经完成了2个DB值的实例化
而pytest_generate_tests在收集阶段生成了两个对test_db_initialized的相应调用。
"""
def test_db_initialized(db):
    if db.__class__name == "DB2":
        pytest.fail("deliberately failing for demo purposes")