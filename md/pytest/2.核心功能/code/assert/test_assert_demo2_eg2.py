import pytest
"""
demo2_eg2:获取实际运行的异常信息-断言异常的值是否与字符串相匹配
"""
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)

    # 取消注释后,在命令行中运行pytest test_assert_demo2_eg2.py -s 
    # -s 会打印出print执行语句
    # print('excinfo.type:异常信息的类型',excinfo.type)
    # print('excinfo.value:异常信息的值',excinfo.value)
    # print('excinfo.traceback:异常信息的回溯',excinfo.traceback)
