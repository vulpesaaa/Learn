import pytest

# 覆盖上级目录同名的conf
@pytest.fixture
def username(username):
    return 'overridden-'+username