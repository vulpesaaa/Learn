# content of test_fixture_marks.py
import pytest

# 运行这个测试将跳过值为2的​​data_set​​调用
@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param


@pytest.fixture(params=['a', 'b', pytest.param('c', marks=pytest.mark.skip)],ids=['first','two','three'])
def data_setids(request):
    return request.param

def test_data(data_set):
    pass

def test_dataids(data_setids):
    pass