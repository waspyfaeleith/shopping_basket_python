import unittest
from basket import Basket
from item import Item

class TestBasket(unittest.TestCase):
    def setUp(self):
        self.basket = Basket()
        self.beans = Item("Beans", 0.22)

    def test_basket_starts_empty(self):
        self.assertEqual(0, self.basket.number_of_items())

    def test_can_add_item_to_basket(self):
        self.basket.add(self.beans)
        self.assertEqual(1, self.basket.number_of_items())


if __name__ == '__main__':
    unittest.main()
