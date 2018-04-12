import unittest
from basket import Basket
from item import Item

class TestBasket(unittest.TestCase):
    def setUp(self):
        self.basket = Basket()
        self.beans = Item("Beans", 0.22)
        self.milk = Item("Milk", 0.60)

    def test_basket_starts_empty(self):
        self.assertEqual(0, self.basket.number_of_items())

    def test_can_add_item_to_basket(self):
        self.basket.add(self.beans)
        self.assertEqual(1, self.basket.number_of_items())

    def test_can_get_total_cost_of_items_in_basket(self):
        self.basket.add(self.beans)
        self.basket.add(self.milk)
        self.assertEqual(0.82, self.basket.get_total())



if __name__ == '__main__':
    unittest.main()
