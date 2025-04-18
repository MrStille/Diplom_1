from unittest.mock import Mock
import os
import sys
sys.path.append(os.getcwd())

import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture(scope='function')
def mock_ketchup():
    ingredient = Mock()
    ingredient.get_price.return_value = 1
    ingredient.get_name.return_value = 'Ketchup'
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient


@pytest.fixture(scope='function')
def mock_mustard():
    ingredient = Mock()
    ingredient.get_price.return_value = 1
    ingredient.get_name.return_value = 'Mustard'
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient

@pytest.fixture(scope='function')
def mock_beef():
    ingredient = Mock()
    ingredient.get_price.return_value = 7
    ingredient.get_name.return_value = 'Beef'
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING

@pytest.fixture(scope='function')
def mock_bun():
    bun = Mock()
    bun.get_price.return_value = 10
    bun.get_name.return_value = 'Mocked_Bun'
    return bun


@pytest.fixture(scope='function')
def mock_cheese():
    ingredient = Mock()
    ingredient.get_price.return_value = 5
    ingredient.get_name.return_value = 'Cheese'
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient
