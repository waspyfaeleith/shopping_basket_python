import unittest
from customer import Customer
from basket import Basket

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Fred")

    def test_customer_has_name(self):
        self.assertEqual("Fred", self.customer.name)

    def test_customer_starts_with_no_loyalty_card(self):
        self.assertEqual(False, self.customer.has_loyalty_card)

    def test_can_change_loyalty_card_to_true(self):
        self.customer.has_loyalty_card = True
        self.assertEqual(True, self.customer.has_loyalty_card)

if __name__ == '__main__':
    unittest.main()
