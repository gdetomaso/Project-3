""" This code uses the API provided by the National Park Service. Specifically, it takes the park name, state in which the park is located
and the description of the park. The API URL format requires a four-digit state code created by the National Park Service. That four-digit code is found
through the park_code_lookyp.py module and imported to use in this module. """

import requests
from models import NationalPark
import os
from pprint import pprint



# when the user inputs data into program
# you will be receiving national park name as string

# def main2():
#     #api_key = os.environ['NATIONAL_PARKS_KEY']
#     national_park_info, error = get_national_park_info_from_api(api_key)
#     if error or not national_park_info:
#         print("Sorry, could not get park information", error)
#     else:
#         park_name, postal_code, park_description, lat_of_park, long_of_park = show_park_info(national_park_info)
#         #return NationalParkInfo(park_name, postal_code, park_description, lat_of_park, long_of_park)
#         print(f'Park Name: {park_name} \nPark Postal Code: {postal_code}\nPark Description: {park_description} \nPark Latitude: {lat_of_park} \nPark Longitude: {long_of_park}')
#         # prints park name from information pulled from api website based on query


def get_national_park_info_from_api(park_code):
    api_key = os.environ['NATIONAL_PARKS_KEY']
    url = f'https://developer.nps.gov/api/v1/parks?parkCode={park_code}&api_key={api_key}' #this is all parks, by parkCode: https://developer.nps.gov/api/v1/parks?parkCode=yell&api_key=
    response = requests.get(url)
    try:
        response.raise_for_status() # Raise exception for 400/500 errors
        national_park_info = response.json()
        park_data = national_park_info['data']
        park_result = NationalPark(park_code=park_code,
                                   lat=get_park_lat(park_data),
                                   long=get_park_long(park_data),
                                   postal_code=get_park_postal_code(park_data),
                                   park_name=get_park_name(park_data),
                                   park_description=get_park_description(park_data))
        return park_result, None  
    except Exception as e:
        print (e)
        print(response.text)
        return None, e


def get_park_name(national_park_info):
    try:
        park_name = national_park_info[0]['fullName']
        return park_name
    except KeyError:
        print('The park name data is not available')
        return None


def get_park_postal_code(national_park_info):
    try:
        postal_code= national_park_info[0]['addresses'][0]['postalCode']
        return postal_code
    except KeyError:
        print('The park postal code data is not available')
        return None


def get_park_description(national_park_info):
    try:
        park_description = national_park_info[0]['description']
        return park_description
    except KeyError:
        print('The park description data is not available')
        return None


def get_park_lat(national_park_info):
    try:
        park_lat_long = national_park_info[0]['latLong']
        split_lat_long= park_lat_long.split(',')
        lat_of_park = split_lat_long[0].split(':')[1]   
        return lat_of_park
    except KeyError:
        print('The park latitude data is not available')
        return None


def get_park_long(national_park_info):
    try:
        park_lat_long = national_park_info[0]['latLong']
        split_lat_long= park_lat_long.split(',')
        long_of_park = split_lat_long[1].split(':')[1]  
        return long_of_park
    except KeyError:
        print('The park longitude data is not available')
        return None


def show_park_info(national_park_info):
    park_name = get_park_name(national_park_info)
    postal_code = get_park_postal_code(national_park_info)
    park_description = get_park_description(national_park_info)
    park_lat = get_park_lat(national_park_info)
    park_long = get_park_long(national_park_info)
    return park_name, postal_code, park_description, park_lat, park_long


# if __name__ == '__main__':
#     main2()