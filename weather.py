import requests

key2 = '255237a4f339f0f1642b5f217eb70a5d'

def get_weather(city_name):
    api_address = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key2}&units=metric'
    json_data = requests.get(api_address).json()

    if json_data.get("cod") != 200:
        return None, None, None  # Invalid city, API error

    city_actual = json_data.get("name")
    description = json_data["weather"][0]["description"]
    temperature = round(json_data["main"]["temp"], 1)

    return city_actual, description, temperature
