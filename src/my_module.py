from . import data

def get_cheapest_hotel(number):   #DO NOT change the function's name
    hotels, inputs = data.get_hotels(), convert_input(number)
    return get_winner(hotels, inputs).name

def get_winner(hotels, inputs):
    return sorted(sorted(hotels, key=lambda h: h.classification, reverse=True), key=lambda h: h.get_sum_of_prices(inputs))[0]

def convert_input(input_string):
    reward, is_weekend_list = clear_input_string(input_string)
    return [{'reward': reward, 'weekend': weekend} for weekend in is_weekend_list]

def clear_input_string(input_string):
    client_type, dates = separate_client_type_from_dates(input_string)
    reward = is_reward_client(client_type)
    is_weekend_list = are_weekends(dates)
    return (reward, is_weekend_list)

def separate_client_type_from_dates(input_string):
    client_type, dates = input_string.split(':')
    return (client_type, dates.strip())

def is_reward_client(client_type):
    #return client_type == 'Rewards'
    return client_type.startswith('Rew')

def are_weekends(dates):
    return [is_weekend(date.strip()) for date in dates.split(',')]

def is_weekend(date):
    return date[date.find('(') + 1: date.find(')')] in ('sat', 'sun')
