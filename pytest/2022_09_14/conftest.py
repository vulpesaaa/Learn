import pytest
# 将​​fixture​​作为一个插件，使其所有​​fixture​​和钩子可用于​app/tests​中的测试
# pytest_plugins = "mylibrary.fixtures"

# eg1: 参数化命令行参数中的stringinput参数的值
# def pytest_addoption(parser):
#     # --stringinput定义命令行参数
#     parser.addoption(
#         "--stringinput",  
#         action="append",
#         default=[],
#         help="list of stringinputs to pass to test functions",
#     )


# # metafunc对象
# def pytest_generate_tests(metafunc):
#     # 如果在stringinput在fixture名列表中，即测试用例调用fixture名为stringinput
#     if "stringinput" in metafunc.fixturenames:
#         # 参数化命令行参数中的stringinput参数的值，即"stringinput" :""
#         metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))


# eg2:生成参数组合，具体取决于命令行
def pytest_addoption(parser):
    # 命令行参数为"--all"
    parser.addoption("--all", action="store_true", help="run all combinations")

def pytest_generate_tests(metafunc):
    if "param1" in metafunc.fixturenames:
        if metafunc.config.getoption("all"):
            end = 5
        else:
            end = 2
        metafunc.parametrize("param1",range(end))