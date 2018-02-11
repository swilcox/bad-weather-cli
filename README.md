# bad-weather-cli
BADash Weather metrics client

required environment variables that must be set:

* OWM_KEY = OpenWeather API Key
* BADASH_API_KEY = API Key for posting to BADash
* BADASH_API_URL = URL for posting events to BADash

** Running from the command line

Example: 

```
$ python get_weather.py 37234 US nashville-weather
```

** Running in AWS Lambda

Set Environment variables.

Set Input for execution with payload:

```
{'zipcode': '37234', 'country': 'US', 'job': 'nashville-weather'}
```

