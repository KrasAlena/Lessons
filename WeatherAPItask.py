'''
Task: https://github-com.translate.goog/robotautas/kursas/wiki/Konsultacija-Oras-pagal-IP?_x_tr_sl=lt&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp#užduotis

We have a string with many ip addresses:
ip_list = ['122.35.203.161', '174.217.10.111', '187.121.176.91', '176.114.85.116', '174.59.204.133', '54.209.112.174', '109.185.143.49', '176.114.253.216', '210.171.87.76', '24.169.250.142']
Generate a CSV file containing IP,Country,City,Temp,Weather columns.

Use the following APIs:

https://freegeoip.app/
https://openweathermap.org/api (Or any other API suitable for the task)
You will need to register for OpenWeather and get an API-key.
Do not write the API-key directly in the code, use environment variables
'''

import requests
import os
import dotenv
import csv

dotenv.load_dotenv()

w_api_key = os.environ.get('WEATHER-API-KEY')
geo_api_key = os.environ.get('IP-API-KEY')

ip_list = ['122.35.203.161', '174.217.10.111', '187.121.176.91', '176.114.85.116', '174.59.204.133', '54.209.112.174', '109.185.143.49', '176.114.253.216', '210.171.87.76', '24.169.250.142']

with open('weather_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['IP', 'Country', 'City', 'Temp', 'Weather']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for ip in ip_list:
        response_ip = requests.get(f'https://api.ipbase.com/v2/info?apikey={geo_api_key}&ip={ip}')
        ip_data = response_ip.json()

        latitude = ip_data['data']['location']['latitude']
        longitude = ip_data['data']['location']['longitude']

        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={w_api_key}')
        weather_data = response.json()

        ip_country = weather_data['sys']['country']
        ip_city = weather_data['name']
        ip_temp = weather_data['main']['temp']
        ip_weather = weather_data['weather'][0]['description']

        writer.writerow({'IP': ip, 'Country': ip_country, 'City': ip_city, 'Temp': ip_temp, 'Weather': ip_weather})