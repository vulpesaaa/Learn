import pytest


@pytest.fixture
def fixture_one():
    print("\n执行fixture_one")
    return 1


@pytest.fixture
def fixture_two(fixture_one):
    print("\n执行fixture_two")
    yield 2
    print("\n执行fixture_two的teardown代码")


@pytest.fixture
def fixture_adding(fixture_one, fixture_two):
    print("\n执行fixture_adding")
    result = fixture_one + fixture_two
    yield result
    print("\n执行fixture_adding的teardown代码")


def test_demo(fixture_two,fixture_adding):
    print("\n执行测试函数test_demo")
    print(fixture_two,fixture_adding)
    assert fixture_adding == 3

