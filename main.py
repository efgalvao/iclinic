import requests
import json
from datetime import datetime

def forecast():
    """
    Get Weather forecast from openweather and informs wich days you should take an umbrella because the humidity is greater than 70%
    """
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=-21.1775000&lon=-47.8102800&exclude=hourly&appid=3985ca4c369bb3eb675da1bcd4a40690'
    response = requests.get(url)
    data = response.json()
    forecast = data['daily']
    days = []
    for day in forecast:        
        weekday = day['dt']
        weekday = datetime.fromtimestamp(weekday).strftime('%A')
        if day['humidity'] > 70:
            days.append(weekday)
    if len(days) == 1:
        print(f'You should take an umbrella in these days: {days[0]}.')
    elif len(days) >= 2:
        print(f'You should take an umbrella in these days: {(", ".join(days[0:-1]))} and {days[-1]}.')
    else:
        print(f'You should take an umbrella in these days: ')
