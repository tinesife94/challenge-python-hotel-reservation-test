""" Has the get_cheapest_hotel() function.

Mudule provided with the problem.
"""

from . import data
from . import preprocessing
from . import franchise

def get_cheapest_hotel(number):   #DO NOT change the function's name
    """Provides the name of the most advantageos hotel for the client.

    Based on the client's fidelity plan and schedule, this means:
        1 - Lowest budget hotel (or hotels, if there is a tie)
        2 - Hotel with the highest classification score in 1.

    For hotels described in the presented problem, a tie in classification
    score is impossible. If a tie occurs, the function still returns only one
    hotel name, but the returned name is implementation dependent.
    """
    client_info = preprocessing.convert_input(number)
    miami = franchise.Franchise(data.get_hotels())
    return miami.get_best_member_for_client(client_info).name
