import unittest
from item import Item

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item("Beans", 0.20)

    def test_item_has_description(self):
        self.assertEqual("Beans", self.item.description)

    def test_item_has_price(self):
        self.assertEqual(0.20, self.item.price)

    def test_can_change_price(self):
        self.item.price = 0.22
        self.assertEqual(0.22, self.item.price)

if __name__ == '__main__':
    unittest.main()
