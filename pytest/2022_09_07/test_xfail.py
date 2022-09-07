import pytest
"""
@pytest.mark.xfail

xfai还有一种使用方法就是@pytest.mark.xfail标签, 他的含义:期望测试用例是失败的, 但是不会影响测试用例的的执行; 如果测试用例执行失败的则结果是xfailed(不会额外显示出错误信息), 如果用例执行成功则结果是xpassed

condition:如果满足条件则标记用例执行失败,  默认为True
reason:用例标记为预期失败的原因,  默认为None
raises:指定个异常类或者异常类元组表明期望用例抛出这些异常;若用例失败不是因为这些异常那用例会执行失败标记为FAILED
run:是否执行, 若为True则执行,若为False则用例不执行直接标记为XFAIL,默认为True
strict:为False用例执行成功为xpassed执行失败则为xfailed;为True用例执行成功标记为failed执行失败则为xfailed,  默认None
"""
class Test_Two():
#eg1: reason 参数
    def test_01(self):
        print("===========> test_01 start")
        pytest.xfail(reason='该功能尚未完善')
        print("===========> test_01")

    def test_02(self):
        print("===========> test_02")
#eg2:condition参数
    # 参数condition为True则pytest.mark.xfail不执行
    @pytest.mark.xfail(condition=1<2, reason="pytest.mark.xfail不执行")
    def test_03(self):
        print("===========> test_03")

    # 参数condition为False则pytest.mark.xfail执行
    @pytest.mark.xfail(condition=1>2, reason="pytest.mark.xfail执行")
    def test_04(self):
        print("===========> test_04")
#eg3:run参数
    @pytest.mark.xfail(run=True)      # 参数run为True执行
    def test_05(self):
        print("===========> test_05")
        assert 1==1

    @pytest.mark.xfail(run=False)      # 参数run为False不执行,直接标记为xfailed
    def test_06(self):
        print("===========> test_06")
        assert 1==1


class Test_One:
#eg4:strict和reason参数
    @pytest.mark.xfail(strict=False,reason="strict为false,用例执行成功则结果为xpassed")
    def test_07(self):
        print("===========> test_07")
        assert 1==1
    @pytest.mark.xfail(strict=False,reason="strict为false,用例执行失败则结果为xfailed")
    def test_08(self):
        print("===========> test_08")
        assert 1==0
    @pytest.mark.xfail(strict=True,reason="strict为true,用例执行成功则结果为failed")
    def test_09(self):
        print("===========> test_09")
        assert 1==1
    @pytest.mark.xfail(strict=True,reason="strict为true,用例执行失败则结果为xfailed")
    def test_10(self):
        print("===========> test_10")
        assert 1==0



if __name__ == "__main__":
    pytest.main(["-rs", "test_xfail.py::Test_One"])