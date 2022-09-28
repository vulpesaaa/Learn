import pytest

# eg1: fixture demo
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# @pytest.fixture说明将fruit_bowl声明为一个fixture
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]

# 查看参数，搜索与fruit_bowl参数相同的fixture，获得该fixture返回的内容，将其作为对象传递给测试函数
def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)