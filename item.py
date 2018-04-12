class Item(object):

    def __init__(self, description, price):
        self._description = description
        self._price = price

    @property
    def description(self):
        return self._description

    @property
    def price(self):
            return self._price

    @price.setter
    def price(self, value):
        self._price = value
