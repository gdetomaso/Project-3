import api_maps, api_nps, api_weather

def get_national_park_info_for_park_and_month(park_code, month):
    # call NPS api with park code, get a NationalPark object, error in return
    national_park_info, np_error = api_nps.get_national_park_info_from_api(park_code)

    if np_error:
        print("Sorry, could not get park information", np_error)
    else:
        # there's data
        # postal_code = api_nps.get_park_postal_code(national_park_info)
        postal_code = national_park_info.postal_code
        lat = national_park_info.lat
        long = national_park_info.long

    #todo after merge
        # weather, weather_error = api_weather.getWeather(postal_code, month)
        # travel_from_minneapolis, travel_error = api_maps.directions(lat,long)

        # TODO check for errors

        # return data if available
        return national_park_info, None, None
    # todo add weather, travel_from_minneapolis when merged