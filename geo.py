from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="hive-location")

def country_code_from_input(t):
    loc = geolocator.geocode(t, timeout=10)
    if loc is None:
        return None
    
    try:
        rev = geolocator.reverse([loc.latitude, loc.longitude], timeout=10)
    except TypeError: # "`address` must not be None"
        return None

    try:
        return rev.raw['address']['country_code']
    except KeyError:
        return None