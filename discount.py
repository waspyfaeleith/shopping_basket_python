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
