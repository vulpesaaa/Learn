# content of test_module.py
import pytest
#在测试期间,pytest只激活最少个数的fixture实例;
# 如果你拥有一个参数化的fixture,所有使用它的用例会在创建的
# 第一个fixture实例并销毁后,才会去使用第二个实例

# 作用域【模块级别】
@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    param = request.param
    print("\n  SETUP modarg", param)
    yield param
    print("\n  TEARDOWN modarg", param)


@pytest.fixture(scope="function", params=[1, 2])
def otherarg(request):
    param = request.param
    print("\n  SETUP otherarg", param)
    yield param
    print("\n  TEARDOWN otherarg", param)

# otherarg的作用域是function【用例级别】,所以独立完成,即param[1]后调用拆卸函数,后继续使用param[2]执行测试test_0
def test_0(otherarg):
    print("  RUN test0 with otherarg", otherarg)


def test_1(modarg):
    print("\n  RUN test1 with modarg", modarg)


def test_2(otherarg, modarg):
    print("  RUN test2 with otherarg {} and modarg {}".format(otherarg, modarg))

# 此测试仅验证是否modarg会在此测试后拆卸fixture
def test_3(otherarg):
    print("*************test3*****",otherarg)


"""
mod1的TEARDOWN操作完成后,才开始mod2的SETUP操作;
用例test_0独立完成测试;
用例test_1和test_2都使用到了模块级别的modarg,同时test_2也使用到了用例级别的otherarg.
它们执行的顺序是,test_1先使用mod1,接着test_2使用mod1和otherarg 1/otherarg 2,
然后test_1使用mod2,最后test_2使用mod2和otherarg 1/otherarg 2;
也就是说test_1和test_2共用相同的modarg实例,最少化的保留fixture的实例个数;
"""