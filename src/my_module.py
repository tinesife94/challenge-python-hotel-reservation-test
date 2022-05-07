""" Provides the get_cheapest_hotel() funcion.

Mudule provided with the problem.
"""

from . import data

def get_cheapest_hotel(number):   #DO NOT change the function's name
    """Provides the name of the most advantageos hotel for the client.

    Based on the client's fidelity plan and schedule, this means:
        1 - Lowest budget hotel (or hotels, if there is a tie)
        2 - Hotel with the highest classification score in 1.

    For hotels described in the presented problem, a tie in classification
    score is impossible. If a tie occurs, the function still returns only one
    hotel name, but the returned name is implementation dependent.
    """
    hotels, inputs = data.get_hotels(), convert_input(number)
    return get_winner(hotels, inputs).name

def get_winner(hotels, inputs):
    """Returns the hotel object most compatible with the customer's needs."""
    classification = lambda h: h.classification
    sum_of_prices = lambda h: h.get_sum_of_prices(inputs)
    ret = sorted(hotels, key=classification, reverse=True)
    return sorted(ret, key=sum_of_prices)[0]

def convert_input(input_string):
    """Used to get data from the input string in a more friendly format."""
    reward, is_weekend_list = clear_input_string(input_string)
    return [{'reward': reward,
            'weekend': weekend} for weekend in is_weekend_list]

def clear_input_string(input_string):
    """Used to extract useful information from the input string."""
    client_type, dates = separate_client_type_from_dates(input_string)
    reward = is_reward_client(client_type)
    is_weekend_list = are_weekends(dates)
    return (reward, is_weekend_list)

def separate_client_type_from_dates(input_string):
    """Used to separate the client fidelity status from his schedule."""
    client_type, dates = input_string.split(':')
    return (client_type, dates.strip())

def is_reward_client(client_type):
    """Tests if a client has a Rewards status.

    As there is an inconsistency between the problem description and the
    examples provided, a small adaptation was made to support both cases:
    Reward and Rewards.
    """
    #return client_type == 'Rewards'
    return client_type.startswith('Rew')

def are_weekends(dates):
    """Used to get the client's schedule in a more friendly format."""
    return [is_weekend(date.strip()) for date in dates.split(',')]

def is_weekend(date):
    """Tests if the date information provided represents a weekend."""
    return date[date.find('(') + 1: date.find(')')] in ('sat', 'sun')
