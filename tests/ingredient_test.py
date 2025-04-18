import os
import sys
sys.path.append(os.getcwd())

from praktikum import ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

class TestIngredient:
    name = "IngredientA"
    price = 1.2
    type = INGREDIENT_TYPE_SAUCE

    def test_get_name(self):
        ingredient_a = ingredient.Ingredient(self.type, self.name, self.price)
        assert ingredient_a.get_name() == self.name

    def test_get_price(self):
        ingredient_a = ingredient.Ingredient(self.type, self.name, self.price)
        assert ingredient_a.get_price() == self.price

    def test_get_type(self):
        ingredient_a = ingredient.Ingredient(self.type, self.name, self.price)
        assert ingredient_a.get_type() == self.type
