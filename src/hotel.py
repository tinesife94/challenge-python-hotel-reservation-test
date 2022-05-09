#!/usr/bin/env python
"""
Import this module to use the Hotel class.

>>> lakewood = Hotel("Lakewood", 3, [[110, 80], [90, 80]])
>>> isinstance(lakewood, Hotel)
True
"""

class Hotel:
    """A class to facilitate hotel management.

    >>> lakewood = Hotel("Lakewood", 3, [[110, 80], [90, 80]])

    >>> lakewood.get_price(weekend=False, reward = False)
    110

    >>> lakewood.get_price(weekend = True, reward = False)
    90

    >>> lakewood.get_sum_of_prices([
    ... {'weekend':False, 'reward':False},
    ... {'weekend':True, 'reward':False}
    ... ])
    200
    """

    def __init__(self, name, classification, price_table):
        self.name = name
        self.classification = classification
        self.price_table = price_table

    def get_price(self, *, weekend, reward):
        """Provides the reservation price based on week day and client type."""
        return self.price_table[weekend][reward]

    def get_sum_of_prices(self, inputs):
        """Provides the price total for multiple reservations."""
        return sum(self.get_price(**inp) for inp in inputs)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
