""" This code uses the API provided by the National Park Service. Specifically, it takes the park name, state in which the park is located
and the description of the park. The API URL format requires a four-digit state code created by the National Park Service. That four-digit code is found
through the park_code_lookyp.py module and imported to use in this module. """

import requests

import os
from pprint import pprint
from park_code_lookup import park_code

#when the user inputs data into program
#you will be receiving national park name as string


def main():
    api_key = os.environ['NATIONAL_PARKS_KEY']
    national_park_info, error = get_national_park_info_from_api(api_key)

    if error or not national_park_info:
        print("Sorry, could not get park information", error)
    else:
        park_name, park_state, park_description = show_park_info(national_park_info)
        print(f'Park Name: {park_name} \nPark State: {park_state} \nPark Description: {park_description}')
        # prints park name from information pulled from api website based on query


def get_national_park_info_from_api(api_key):
    url = f'https://developer.nps.gov/api/v1/parks?parkCode={park_code}&api_key={api_key}' #this is all parks, by parkCode: https://developer.nps.gov/api/v1/parks?parkCode=yell&api_key=
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise exception for 400/500 errors
        national_park_info = response.json()
        park_data = national_park_info['data']
        return park_data, None
    except Exception as e:
        print (e)
        pprint(response.text)
        return None, e


def get_park_name(national_park_info):
    try:
        park_name = national_park_info[0]['fullName']
        return park_name
    except KeyError:
        print('The park name data is not available')
        return None


def get_park_state(national_park_info):
    try:
        park_state = national_park_info[0]['addresses'][1]['stateCode']
        return park_state
    except KeyError:
        print('The park state data is not available')
        return None


def get_park_description(national_park_info):
    try:
        park_description = national_park_info[0]['description']
        return park_description
    except KeyError:
        print('The park description data is not available')
        return None


def show_park_info(national_park_info):
    park_name = get_park_name(national_park_info)
    park_state = get_park_state(national_park_info)
    park_description = get_park_description(national_park_info)
    return park_name, park_state, park_description


if __name__ == '__main__':
    main()