import requests

API_KEY = '{your api keys}'

def get_weather(city):
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(weather_url)
    return response.json()


