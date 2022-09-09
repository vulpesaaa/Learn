import pytest
# 本例仅作演示，从测试传递fixture数据
@pytest.fixture
def fixt(request):
    marker = request.node.get_closest_marker("fixt_data")
    if marker is None:
        data = None
    else:
        data = marker.args[0]

    return data

# 装饰器应用的未知标记fixt_data会提示warning，因为fixt_data为自定义标记，需要注册才不会告警
# 标记mark仅用于测试，对fixture没有影响
@pytest.mark.fixt_data(42)
def test_fixt(fixt):
    assert fixt ==42