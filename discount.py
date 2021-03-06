class Discount(object):
    def __init__(self):
        self.bogof_items = []

    def bogof_for_item(self, basket, item):
        items_found = 0
        for basket_item in basket.items:
            if basket_item == item:
                items_found += 1
        discount = (items_found // 2) * item.price
        return discount

    def add_to_bogof(self, item):
        self.bogof_items.append(item)

    def bogof_discount(self, basket):
        total_bogof_discount = 0
        for item in self.bogof_items:
            total_bogof_discount += self.bogof_for_item(basket, item)
        return total_bogof_discount

    def extra_10_per_cent(self, basket):
        basket_total = basket.get_total()
        basket_total -= self.bogof_discount(basket)
        if (basket_total > 20.00):
            basket_total *= 0.9
        return basket_total

    def extra_2_percent_for_loyal_cust(self, basket, customer):
        basket_total = self.extra_10_per_cent(basket)
        if (customer.has_loyalty_card):
            basket_total *= 0.98
        return basket_total
