

#setting objects for National Parks API
class NationalPark:
    def __init__(self, park_name, park_code, lat, long, description, postal_code):
    # todo set the other fields
        self.name = park_name
        self.code = park_code
        self.lat = lat
        self.long = long
        self.description = description
        self.postal_code = postal_code


class Weather:
    pass


class TravelDirections:
    def __init__(self, distance, travel_time):
        self.distance = distance
        self.travel_time = travel_time
