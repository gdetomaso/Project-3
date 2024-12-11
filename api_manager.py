import api_maps, api_nps, api_weather

def get_national_park_info_for_park_and_month(park_code, month):
    # call NPS api with park code, get a NationalPark object, error in return
    national_park_info, np_error = api_nps.get_national_park_info_from_api(park_code)
    if np_error:
        print("Sorry, could not get park information", np_error)

        return { 'park_error': np_error }  

    else:
        # there's data, make weather and travel requests 
        weather_description, weather_error = api_weather.get_weather(national_park_info.postal_code, month)
        travel_description, travel_error = api_maps.get_directions(national_park_info.lat, national_park_info.long)  # this returns a dictionary 
            
        # The weather and travel API requests are independent, they may both work, both fail, one work, one fail, so return
        # whatever data/error we get from both 

        return {
            'park_info': national_park_info,
            'weather_description': weather_description,
            'weather_error': weather_error,
            'travel_description': travel_description,
            'travel_error': travel_error
        }
    


def get_weather(postal_code, month):
    weather_info = api_weather.get_weather(postal_code, month)
    return weather_info

def get_maps_info(long, lat):
    maps_info = api_maps.get_directions(long, lat)
    return maps_info
