from praktikum import ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:

    def __init__(self):
        self.name = "IngredientA"
        self.price = 1.2
        self.type = INGREDIENT_TYPE_SAUCE
        self.ingredient_a = ingredient.Ingredient(self.type, self.name, self.price)

    def test_get_name(self):
        assert self.ingredient_a.get_name() == self.name

    def test_get_price(self):
        assert self.ingredient_a.get_price() == self.price

    def test_get_type(self):
        assert self.ingredient_a.get_type() == self.type
