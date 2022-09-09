import pytest
import allure

# feature:功能点，类似测试套testsuit
@allure.feature("登录")
class TestLogin():
    # story：子功能点，类似测试用例testcase
    @allure.story("登录成功")
    def test_login_success(self):
        print("登录成功")
        pass

    @allure.story("密码错误")
    def test_login_failure(self):
        # with allure.step放在测试用例中，测试步骤
        # @allure.step 测试步骤
        with allure.step("输入用户名"):
            print("输入用户名")
        with allure.step("输入密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("登录失败"):
            assert '1' == 1
            print("登录失败")
        pass

    @allure.story("用户名密码错误")
    def test_login_failure_a(self):
        print("用户名或者密码错误，登录失败")
        pass


@allure.feature("注册")
class TestRegister():
    @allure.story("注册成功")
    def test_register_success(self):
        print("测试用例：注册成功")
        pass

    @allure.story("注册失败")
    def test_register_failure(self):
        with allure.step("输入用户名"):
            print("输入用户名")
        with allure.step("输入密码"):
            print("输入密码")
        with allure.step("再次输入密码"):
            print("再次输入密码")
        print("点击注册")
        with allure.step("注册失败"):
            assert 1 + 1 == 2
            print("注册失败")
        pass
