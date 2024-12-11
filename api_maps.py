import requests
from pprint import pprint



#when the user inputs data into program
#you will be receiving national park name as string name
#also receiving city and state name as string is this format "minneapolis, mn"
start_lon = -93.282978
start_lat = 44.973667
# end_lon = -122.14346
# end_lat = 42.91138


def get_directions(end_lat, end_lon):  # Locations are almost always given as lat, lon in that order 
    # This assumes you are starting in Minneapolis 
    # starting and ending longitude and latitude
    print(f'Getting directions data for: {end_lon, end_lat}')
    api_key = '5b3ce3597851110001cf6248107ac5aa189f4f75a3eaf1a68d83d4fc'
    url = f'https://api.openrouteservice.org/v2/directions/driving-car?'
    # changed the API to openrouteservice since that is better for directions between two points

     # request parameters
    params = {
         'api_key' : f'{api_key}',
         'start': f'{start_lat},{start_lon}',
         'end': f'{end_lat},{end_lon}'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        # API request
        # raise errors for unwanted responses
        data = response.json()
        # check for results

        if data.get('features'):
            # retrieve information from the api
            route = data['features'][0]['properties']
            distance = route['summary']['distance']
            duration = route['summary']['duration']
            # the duration and distance values are nested
            # in the summary dictionary
            # return {
            #     'distance': distance,
            #     'duration': duration,
            # }
            # converting meters to miles and seconds to hours
            distance_in_miles = distance / 1609.34
            duration_in_hours = duration / 3600

            # rounding both to two decimal places
            distance_in_miles_rounded = round(distance_in_miles, 2)
            duration_in_hours_rounded = round(duration_in_hours, 2)
            travel_info = f'The park is {distance_in_miles_rounded} miles away, and a {duration_in_hours_rounded} hour drive.'
            # always return the same thing. Modified to be more consistent with other APIs
            return travel_info, None 
        else:
            return None, 'Route not found.'
    except requests.exceptions.RequestException as e:
        print(f'Error fetching map data: {e}')
        return None, f'Could not connect to map API because {e}'
    except Exception as e:  # handle all other errors, for example, API response is not JSON, 
        # or API response is JSON but not the correct format
        return None, f'Error fetching or processing map data: {e}'
        


# if __name__ == '__main__':

    # directions = get_directions(end_lon, end_lat)
    # pprint(directions)
    # api_key = '5b3ce3597851110001cf6248107ac5aa189f4f75a3eaf1a68d83d4fc'
    # url = f'https://api.openrouteservice.org/v2/directions/driving-car?api_key={api_key}&start=-93.282978,44.973667&end=-122.14346,42.91138'
    #

