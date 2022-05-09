"""If you need to change hotel information, this is where you do it.
"""

from .hotel import Hotel

lakewood = Hotel('Lakewood', 3, [[110, 80], [90, 80]])
bridgewood = Hotel('Bridgewood', 4, [[160, 110], [60, 50]])
ridgewood = Hotel('Ridgewood', 5, [[220, 100], [150, 40]])
# my_hotel = Hotel('my_hotel_name', my_hotel_rating,
        # [
            # [weekday_regular_price, weekday_reward_price],
            # [weekend_regular_price, weekend_reward_price]
        # ])

def get_hotels():
    """Useful for getting all hotels at the same time."""
    return [lakewood, bridgewood, ridgewood]
