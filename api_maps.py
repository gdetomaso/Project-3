import requests
from pprint import pprint



#when the user inputs data into program
#you will be receiving national park name as string name
#also receiving city and state name as string is this format "minneapolis, mn"
start_lon = -93.282978
start_lat = 44.973667
# end_lon = -122.14346
# end_lat = 42.91138


def get_directions(end_lon, end_lat):
    # starting and ending longitude and latitude
    print(f'Getting directions data for: {end_lon, end_lat}')
    api_key = '5b3ce3597851110001cf6248107ac5aa189f4f75a3eaf1a68d83d4fc'
    url = f'https://api.openrouteservice.org/v2/directions/driving-car?'
    # changed the API to openrouteservice since that is better for directions between two points

    params = {
         'api_key' : f'{api_key}',
         'start': f'{start_lon},{start_lat}',
         'end': f'{end_lon},{end_lat}'
    }
     # request parameters
    # the data is in 'longitude, latitude' format
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
            distance_in_miles = distance / 1609.34
            duration_in_hours = duration / 3600
            # converting meters to miles and seconds to hours

            distance_in_miles_rounded = round(distance_in_miles, 2)
            duration_in_hours_rounded = round(duration_in_hours, 2)
            # rounding both to two decimal places
            travel_info = f'The park is {distance_in_miles_rounded} miles away, and a {duration_in_hours_rounded} hour drive.'
            return travel_info
        else:
            return {'error': 'Route not found.'}
    except requests.exceptions.RequestException as e:
        print(f'Error fetching map data: {e}')
        return {'error': str(e)}
#     error handling

# if __name__ == '__main__':

    # directions = get_directions(end_lon, end_lat)
    # pprint(directions)
    # api_key = '5b3ce3597851110001cf6248107ac5aa189f4f75a3eaf1a68d83d4fc'
    # url = f'https://api.openrouteservice.org/v2/directions/driving-car?api_key={api_key}&start=-93.282978,44.973667&end=-122.14346,42.91138'
    #

