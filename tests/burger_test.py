import os
import sys
sys.path.append(os.getcwd())

from praktikum.burger import Burger

class TestBurger:

    def test_add_ingredient(self, mock_cheese, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_cheese)

        assert mock_cheese.get_price() + mock_bun.get_price() * 2 == burger.get_price()
        assert mock_cheese.get_name() in burger.get_receipt()
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_cheese

    def test_set_bun(self, mock_ketchup, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ketchup)

        assert mock_ketchup.get_price() + mock_bun.get_price() * 2 == burger.get_price()
        assert mock_bun.get_name() in burger.get_receipt()

    def test_move_ingredient(self, mock_ketchup, mock_bun, mock_cheese, mock_beef):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ketchup)
        burger.add_ingredient(mock_cheese)
        burger.add_ingredient(mock_beef)
        assert burger.ingredients[2] == mock_beef
        burger.move_ingredient(2,1)

        assert burger.ingredients[2] == mock_cheese
        assert burger.ingredients[1] == mock_beef

    def test_remove_ingredient(self, mock_ketchup, mock_bun, mock_cheese):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ketchup)
        burger.add_ingredient(mock_cheese)
        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ketchup
