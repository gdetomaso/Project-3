import requests

#when the user inputs data into program
#you will be receiving national park name as string name
#also receiving city and state name as string is this format "minneapolis, mn"


def getMaps(location):
    # location is the name of the city and state
    print(f'Getting directions data for: {location}')

    url = f'https://api.openrouteservice.org/v2/directions/driving-car?'
    # changed the API to openrouteservice since that is better for directions between two points
    api_key ='5b3ce3597851110001cf6248107ac5aa189f4f75a3eaf1a68d83d4fc'
    params = {
        'api_key' : api_key,
        'start': ['start_lon', 'start_lat'],
        'end': ['end_lon', 'end_lat']
    }
    # request parameters

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        # API request
        # raise errors for unwanted responses
        data = response.json()
        # check for results

        if data:
            # retrieve information
            starting_location = data['']
            home_address = starting_location['display_name']
            return {
                'home_address': home_address,
                'city': starting_location.get('address', {}).get('lat', ''),
                'country': starting_location.get('address', {}).get('lon', '')
            #     so the user can input city and country instead of lat and lon
            }
        else:
            return {'error': 'Location not found.'}
    except requests.exceptions.RequestException as e:
        print(f'Error fetching map data: {e}')
        return {'error': str(e)}
#     error handling

if __name__ == '__main__':
    location = '93.2650, 44.9778'
    # input format
    result = getMaps(location)
    print(result)

