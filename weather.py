import requests

API_KEY = 'e65645856d2f9f8a5fb3206da89f2305'

def get_weather(city):
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(weather_url)
    return response.json()
