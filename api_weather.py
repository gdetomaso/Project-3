import requests
#from models import Weather
import os

def get_weather(postal_code, month):

    key = os.environ.get('PROJ_WEATHER')
    query = {   # one line per key is more readable 
        'unitGroup': 'us', 
        'include': 'days', 
        'key': key, 
        'contentType': 'json',
    }

    zip = postal_code
    # month = month  # has no effect

    url = (f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{zip}/2023-{month}-01/2023-{month}-28')

    # TODO add error handling 

    try:
        response = requests.get(url, params=query)
        response.raise_for_status()
        data = response.json()
        weather_data_list = data.get('days')
        if not weather_data_list:
            return None, 'Unable to find weather data in response'
        else:
            weather_description = get_description_for_month(weather_data_list, month)
            return weather_description, None
    except Exception as e:
        return None, f'Unable to get weather data because {e}' 


def get_description_for_month(weather_data_list, month):

    # this function would be an excellent candidate for a unit test. It takes in a list and 
    # returns a string, no API calls or anything else external. 
    total_max_temp = 0
    total_min_temp = 0
    total_precip = 0
    count = len(weather_data_list)

    for item in weather_data_list:
        date = item['datetime']
        max_temp = item['tempmax']
        min_temp = item['tempmin']
        precip = item['precip']
        total_max_temp += max_temp
        total_min_temp += min_temp
        total_precip += precip

    avg_max_temp = total_max_temp / count
    avg_min_temp = total_min_temp / count
    avg_precip = total_precip / count

    month_names = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
    month_name = month_names[month-1]

    weather_info = f'In {month_name} the average high and low temperatures are {avg_max_temp:.2f}F and {avg_min_temp:.2f}F and the average precipitation is {avg_precip:.2f} inches.'

    return weather_info
