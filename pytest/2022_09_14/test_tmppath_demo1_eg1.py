import pytest
from pathlib import Path
CONTENT  = "content"
# tmp_path是一个pathlib.path​对象，为测试用例创建一个临时目录
def test_case_file(tmp_path):
    # 临时目录： C:\Users\lmz\AppData\Local\Temp\pytest-of-lmz\pytest-5\test_case_file0\sub
    d = tmp_path / "sub"
    print(d,type(d))
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT) # 写入内容content
    assert p.read_text() == CONTENT
    # iterdir迭代此文件夹下的所有文件
    assert len(list(tmp_path.iterdir())) == 1
    assert 0