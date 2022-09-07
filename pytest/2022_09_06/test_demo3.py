"""
共享同一测试实例，不利于测试隔离
通常是每个测试有唯一的测试实例
"""
class TestClassDemoInstance:
    # 类属性
    value = 0

    def test_one(self):
        self.value=1
        assert self.value ==1

    def test_two(self):
        assert self.value ==1 