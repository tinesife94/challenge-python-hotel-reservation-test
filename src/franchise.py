"""This module provides the franchise class.

The franchise class is useful for doing operations involving all members
of the franchise.
"""

class Franchise:
    """To facilitate operations on all members of the franchise."""
    def __init__(self, members_list):
        self.members_list = members_list
        self._sorted_members_list = sorted(members_list, key=name_as_key())

    def sort_members_by_price(self, client_information, *, reverse=False):
        """To order by price total, based on client_information.

        To get the list, run get_sorted_members()
        """
        self._sorted_members_list.sort(
                    key=price_as_key(client_information),
                    reverse=reverse
                    )

    def sort_members_by_classification(self, *, reverse=False):
        """To order by the service excellence rating.

        To get the result, run get_sorted_members()
        """
        self._sorted_members_list.sort(
                key=classification_as_key(),
                reverse=reverse
                )

    def get_best_member_for_client(self, client_information):
        """Returns the member with the lowest total price for the client.

        Tiebrakers:
            - service excellence rating (classification);
            - name
        """
        self.sort_members_by_classification(reverse=True)
        self.sort_members_by_price(client_information)
        return self._sorted_members_list[0]

    def get_sorted_members(self):
        """To get the result of sorting operations on franchise's members."""
        return self._sorted_members_list[:]

def price_as_key(inputs):
    """To get a key for sorting hotels by their total price."""
    return lambda hotel: hotel.get_sum_of_prices(inputs)

def classification_as_key():
    """To get a key for sorting hotels by their classification score."""
    return lambda hotel: hotel.classification

def name_as_key():
    """To get a key for sorting hotels by their name."""
    return lambda hotel: hotel.name
