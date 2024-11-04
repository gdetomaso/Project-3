import requests
#from models import Weather
import os


#when the user inputs data into program
#you will be reciving month of visit as string name


# This function needs to return necassary data from API in string format
# program will not work if this function does not return necassary data
def getWeather(postal_code, month):
    # month is the name of the month of visit
    #print(month, postal_code)
    
    #test variable to test if function works



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

    weather_info =(f'In May the average high and low temperatures are {avg_max_temp:.2f}F and {avg_min_temp:.2f}F and the average precipitation is {avg_precip:.2f} inches.')

    return weather_info

