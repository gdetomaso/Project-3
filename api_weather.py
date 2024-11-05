import requests
#from models import Weather
import os

def getWeather(postal_code, month):

    key = os.environ.get('PROJ_WEATHER')
    query = {'unitGroup': 'us', 'include': 'days', 'key': key, 'contentType': 'json'}
    zip = postal_code
    month = month

    url = (f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline//{zip}/2023-{month}-01/2023-{month}-28')

    data = requests.get(url, params=query).json()

    list_of_info = data['days']

    total_max_temp = 0
    total_min_temp = 0
    total_precip = 0
    count = len(list_of_info)

    for item in list_of_info:
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

    weather_info =(f'In {month_name} the average high and low temperatures are {avg_max_temp:.2f}F and {avg_min_temp:.2f}F and the average precipitation is {avg_precip:.2f} inches.')

    return weather_info
