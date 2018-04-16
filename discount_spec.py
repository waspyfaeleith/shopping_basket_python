import unittest
from item import Item
from basket import Basket
from discount import Discount
from customer import Customer

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

    def test_10_percent_discount_on_total_over_20_pounds(self):
        dvd = Item("DVD",20.00)
        self.basket.add(self.beans)
        self.basket.add(self.beans)
        self.basket.add(dvd)
        basket_total = self.discount.extra_10_per_cent(self.basket)
        self.assertEqual(18.36, basket_total)

    def test_extra_2_per_cent_discount__cust_has_loyalty_card(self):
        customer = Customer("Jack")
        customer.has_loyalty_card = True
        dvd = Item("DVD",20.00)
        self.basket.add(dvd)
        basket_total = self.discount.extra_2_percent_for_loyal_cust(self.basket, customer)
        self.assertEqual(19.60, basket_total)

    def test_extra_2_per_cent_discount__cust_does_not_have_loyalty_card(self):
        customer = Customer("Jack")
        dvd = Item("DVD",20.00)
        self.basket.add(dvd)
        basket_total = self.discount.extra_2_percent_for_loyal_cust(self.basket, customer)
        self.assertEqual(20.00, basket_total)

if __name__ == '__main__':
    unittest.main()
