class Basket(object):
    def __init__(self):
        self.items = []

    def number_of_items(self):
        return len(self.items)

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def empty(self):
        self.items = []

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
