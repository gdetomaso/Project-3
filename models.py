#setting objects for National Parks API
class NationalPark:
    def __init__(self, park_name, park_code, lat, long, park_description, postal_code):
    # set the other fields
        self.name = park_name
        self.code = park_code
        self.lat = lat
        self.long = long
        self.description = park_description
        self.postal_code = postal_code

    def __str__(self):
        return f'{self.name}, {self.description}'
    #todo add the other fields


class Weather:
    def __init__(self, weather_info):
        self.weather_info = weather_info


class TravelDirections:
    def __init__(self, distance, travel_time):
        self.distance = distance
        self.travel_time = travel_time
