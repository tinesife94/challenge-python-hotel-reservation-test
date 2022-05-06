#!/usr/bin/env python

""" Module that provides the Hotel class.

>>> lakewood = Hotel("Lakewood", 3, [[110, 80], [90, 80]])
>>> lakewood.name
'Lakewood'
>>> lakewood.classification
3
>>> lakewood.price_table
[[110, 80], [90, 80]]
"""

import locale

class Hotel:
    """ A class to facilitate hotel management.

    >>> lakewood = Hotel("Lakewood", 3, [[110, 80], [90, 80]])
    >>> lakewood.get_price(weekend=False, reward = False)
    110
    >>> lakewood.get_price(weekend = True, reward = False)
    90
    >>> lakewood.get_price_string(weekend=False, reward=False)
    'R$ 110,00'
    >>> lakewood.get_sum_of_prices([
    ... {'weekend':False, 'reward':False},
    ... {'weekend':False, 'reward':False},
    ... {'weekend':False, 'reward':False}
    ... ])
    330
    """
    def __init__(self, name, classification, price_table):
        self.name = name
        self.classification = classification
        self.price_table = price_table

    def get_price(self, *, weekend, reward):
        """Provides the reservation price based on week day and client type."""
        return self.price_table[weekend][reward]

    def get_price_string(self, *, weekend, reward):
        """Provides the reservation price in a nice currency format."""
        locale.setlocale(locale.LC_ALL, '')
        return locale.currency(self.get_price(weekend=weekend, reward=reward))

    def get_sum_of_prices(self, inputs):
        """Provides the price total for multiple reservations."""
        return sum(self.get_price(**inp) for inp in inputs)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
