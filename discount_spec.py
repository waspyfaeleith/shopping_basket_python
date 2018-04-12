import unittest
from item import Item
from basket import Basket
from discount import Discount

class TestItem(unittest.TestCase):
    def setUp(self):
        self.beans = Item("Beans", 0.20)
        self.milk = Item("Milk", 0.75)
        self.basket = Basket()
        self.discount = Discount()

    def test_bogof_list_starts_empty(self):
        self.assertEqual(0, len(self.discount.bogof_items))

    def test_can_add_item_to_bogof_list(self):
        self.discount.add_to_bogof(self.beans)
        self.assertEqual(1, len(self.discount.bogof_items))

    def test_bogof_2_beans_is_20_pence(self):
        self.basket.add(self.beans)
        self.basket.add(self.beans)
        bogof_discount = self.discount.bogof_for_item(self.basket, self.beans)
        self.assertEqual(0.20, bogof_discount)

    def test_bogof_1_beans_is_0_pence(self):
        self.basket.add(self.beans)
        bogof_discount = self.discount.bogof_for_item(self.basket, self.beans)
        self.assertEqual(0.0, bogof_discount)

    def test_bogof_3_beans_is_20_pence(self):
        self.basket.add(self.beans)
        self.basket.add(self.beans)
        self.basket.add(self.beans)
        bogof_discount = self.discount.bogof_for_item(self.basket, self.beans)
        self.assertEqual(0.20, bogof_discount)

    def test_bogof_4_beans_is_40_pence(self):
        self.basket.add(self.beans)
        self.basket.add(self.beans)
        self.basket.add(self.beans)
        self.basket.add(self.beans)
        bogof_discount = self.discount.bogof_for_item(self.basket, self.beans)
        self.assertEqual(0.40, bogof_discount)

    def test_bogof_discount_basket_95_pence(self):
        self.basket.add(self.beans)
        self.basket.add(self.beans)
        self.basket.add(self.milk)
        self.basket.add(self.milk)
        self.discount.add_to_bogof(self.beans)
        self.discount.add_to_bogof(self.milk)
        bogof_discount = self.discount.bogof_discount(self.basket)
        self.assertEqual(0.95, bogof_discount)


if __name__ == '__main__':
    unittest.main()
