# pytest提供内置​fixture /function​参数来请求任意资源，比如一个唯一的临时目录
def test_needsfiles(tmp_path):
    # 在运行测试之前，pytest会创建一个每个测试调用唯一的临时目录
    print(tmp_path)
    assert 0