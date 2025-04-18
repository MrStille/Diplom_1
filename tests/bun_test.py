from praktikum.bun import Bun


class TestBun:
    name = "New name"
    price = 123.3

    def test_get_name(self):
        bun = Bun(self.name, self.price)
        assert bun.get_name() == self.name

    def test_get_price(self):
        bun = Bun(self.name, self.price)
        assert bun.get_price() == self.price