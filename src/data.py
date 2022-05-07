""" If you need to change hotels information, this is where you do it.
"""

from .hotel import Hotel

lakewood = Hotel('Lakewood', 3, [[110, 80], [90, 80]])
bridgewood = Hotel('Bridgewood', 4, [[160, 110], [60, 50]])
ridgewood = Hotel('Ridgewood', 5, [[220, 100], [150, 40]])

def get_hotels():
    """Useful for getting all hotels at the same time."""
    return [lakewood, bridgewood, ridgewood]
