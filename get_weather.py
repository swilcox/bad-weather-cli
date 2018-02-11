"""get_weather.py script

Environment variables that must be set:

- OWM_KEY = OpenWeather API Key
- BADASH_API_URL = Full BADash API URL (including /events path)
- BADASH_API_KEY = API Key for posting to BADash

"""
import os
import sys

import pyowm
import requests


def get_current_temperature(zipcode, country):
    """get the current temperature"""
    owm = pyowm.OWM(os.environ.get('OWM_KEY'))
    observation = owm.weather_at_zip_code(zipcode, country)
    weather = observation.get_weather()
    return {
        'temperature': weather.get_temperature('fahrenheit')['temp'],
        'wind_speed': weather.get_wind('miles_hour')['speed'],
        'wind_direction': weather.get_wind('miles_hour')['deg'],
        'humidity': weather.get_humidity(),
        'status': weather.get_status(),
    }


def send_to_badash(job, data):
    """send some data to badash"""
    data['job'] = job
    data['result'] = 0
    resp = requests.post(os.environ.get('BADASH_API_URL', ''), json=data, headers={'X-Api-Key': os.environ.get('BADASH_API_KEY')})
    print(resp.status_code)


def lambda_handler(event, context):
    """handle AWS Lambda calling this script"""
    if event.get('zipcode') and event.get('country') and event.get('job'):
        data = get_current_temperature(event['zipcode'], event['country'])
        send_to_badash(event['job'], data)
    else:
        print('Error: no zipcode and/or country and/or job supplied!')
        exit(-1)


def main():
    """main"""
    data = get_current_temperature(sys.argv[1], sys.argv[2])
    send_to_badash(sys.argv[3], data)


if __name__ == "__main__":
    main()
