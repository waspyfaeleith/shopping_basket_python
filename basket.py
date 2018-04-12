class Basket(object):
    def __init__(self):
        self.items = []

    def number_of_items(self):
        return len(self.items)

    def add(self, item):
        self.items.append(item)
