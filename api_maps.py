import requests

#when the user inputs data into program
#you will be receiving national park name as string name
#also receiving city and state name as string is this format "minneapolis, mn"


def getMaps(location):
    # location is the name of the city and state
    print(f'Getting directions data for: {location}')

    url = 'https://nominatim.openstreetmap.org/search'
    # Nominatim API is the geocoding service for OSM

    params = {
        'q' : location,
        'format': 'json',
        'addressdetails': 1,
        'limit': 1,
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
            starting_location = data[0]
            home_address = starting_location['display_name']
            return {
                'home_address': home_address,
                'city': starting_location.get('address', {}).get('city', ''),
                'country': starting_location.get('address', {}).get('country', '')
            #     so the user can input city and country instead of lat and lon
            }
        else:
            return {'error': 'Location not found.'}
    except requests.exceptions.RequestException as e:
        print(f'Error fetching map data: {e}')
        return {'error': str(e)}
#     error handling

if __name__ == '__main__':
    location = 'Minneapolis, USA'
    # input format
    result = getMaps(location)
    print(result)

