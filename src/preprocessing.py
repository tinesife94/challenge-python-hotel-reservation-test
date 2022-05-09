"""Provides useful functions that clear and transform provided inputs.
"""

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
