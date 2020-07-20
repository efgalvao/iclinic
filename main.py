import requests
import json
from datetime import datetime

def get_forecast():
    """
    Get Weather forecast from openweather.
    """
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=-21.1775000&lon=-47.8102800&exclude=hourly&appid=3985ca4c369bb3eb675da1bcd4a40690'
    response = requests.get(url)
    data = response.json()
    forecast = data['daily'][1:6]
    return forecast

def main():
    """
    Uses forecast from openweather and says which day you should take an umbrella.
    """
    forecast = get_forecast()
    days = []
    for day in forecast:        
        if day['humidity'] > 70:
            days.append(datetime.fromtimestamp(day['dt']).strftime('%A'))
    if len(days) == 1:
        print(f'You should take an umbrella in these days: {days[0]}.')
    elif len(days) >= 2:
        print(f'You should take an umbrella in these days: {(", ".join(days[0:-1]))} and {days[-1]}.')
    else:
        print(f'You should take an umbrella in these days: ')

if __name__ == '__main__':
    main()