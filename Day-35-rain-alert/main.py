import os
import requests


endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("owm_api_key")
TOPIC = "rainalert"  # CHANGE THIS to your topic
url = f"https://ntfy.sh/{TOPIC}"


parameter = {
    "q" : "islamabad",
    "appid" : api_key,
    "cnt" : 4
}

response = requests.get(endpoint, params=parameter)
response.raise_for_status()
weather_data = response.json()

is_it_rainig = False
for hourly_data in weather_data['list']:
    weather_code = hourly_data['weather'][0]['id']
    if int(weather_code) < 600:
        is_it_rainig = True


def send_notification(message, title="Notification"):
    """Sends a notification"""
    requests.post(
        url,
        headers={"Title": title},
        data=message.encode('utf-8')
        )
    print("✓ Notification sent!")

if is_it_rainig:
    send_notification("It's gonna rain", "Rain Alert")