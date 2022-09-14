import pytest
def pytest_generate_tests(metafunc):
    idlist = []
    argvalues = []
    # 遍历scenarios
    # 获取id、项、参数名、参数值
    # 参数化，作用域范围为class类
    for scenario in metafunc.cls.scenarios:
        idlist.append(scenario[0])
        items = scenario[1].items()
        argnames = [x[0] for x in items]
        argvalues.append([x[1] for x in items])
    metafunc.parametrize(argnames, argvalues, ids=idlist, scope="class")


scenario1 = ("basic", {"attribute": "value"})
scenario2 = ("advanced", {"attribute": "value2"})

# 可看到"basic"和"advanced"作为测试函数的变体
# pytest  test_parametrize_demo2_eg3.py --collect-only 
class TestSampleWithScenarios:
    scenarios = [scenario1, scenario2]

    def test_demo1(self, attribute):
        assert isinstance(attribute, str)

    def test_demo2(self, attribute):
        assert isinstance(attribute, str)