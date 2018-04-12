import unittest
from item import Item

class TestItem(unittest.TestCase):

    def test_item_has_description(self):
        item = Item("Beans", 0.20)
        self.assertEqual("Beans", item.description)

    def test_item_has_price(self):
        item = Item("Beans", 0.20)
        self.assertEqual(0.2, item.price)

    def test_can_change_price(self):
        item = Item("Beans", 0.20)
        item.price = 0.22
        self.assertEqual(0.22, item.price)

if __name__ == '__main__':
    unittest.main()
