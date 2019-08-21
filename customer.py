class Customer(object):
    def __init__(self, name):
        self._name = name
        self._has_loyalty_card = False

    @property
    def name(self):
        return self._name

    @property
    def has_loyalty_card(self):
            return self._has_loyalty_card

    @has_loyalty_card.setter
    def has_loyalty_card(self, value):
        self._has_loyalty_card = value
