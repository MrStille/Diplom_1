import os
import sys

from praktikum.ingredient import Ingredient

sys.path.append(os.getcwd())

from praktikum.bun import Bun
from praktikum.database import Database


class TestDatabase:

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) > 0
        for bun in buns:
            assert isinstance(bun, Bun)
            assert len(bun.get_name()) > 0
            assert bun.get_price() > 0

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) > 0
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)
            assert len(ingredient.get_name()) > 0
            assert ingredient.get_price() > 0
            assert len(ingredient.get_type()) > 0
