# contents of conftest.py
import pytest

def compute_expensive_image():
    pass

def load_image(f):
    pass

# 作用域为会话范围
@pytest.fixture(scope="session")
def image_file(tmp_path_factory):
    # tmp_path_factory可用于从任何其他​fixture​或测试创建任意临时目录。
    img = compute_expensive_image()
    fn = tmp_path_factory.mktemp("data") / "img.png"
    img.save(fn)
    return fn


# contents of test_image.py
def test_histogram(image_file):
    img = load_image(image_file)
    # compute and test histogram