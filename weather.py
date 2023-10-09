import requests
import myapikey
from datetime import datetime, timedelta

def check(climb, rain):
    # Coordinates for Sandstone, MN
    latitude = 46.129469
    longitude = -92.859276

    # Calculate the timestamp for 48 hours ago
    now = datetime.now()
    now = int(datetime.timestamp(now))
    time_48_hours_ago = datetime.now() - timedelta(hours=48)
    timestamp_48_hours_ago = int(datetime.timestamp(time_48_hours_ago))

    # Build the API request URL
    url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={latitude}&lon={longitude}&dt={now}&appid={myapikey.api_key}"

    # Make the API request
    response = requests.get(url)
    data = response.json()
    current = data['current']['weather'][0]['main']
    if current == 'Rain':
        rain = True
        climb = False
    else:
        rain = False
    print(current)
    return climb, rain

