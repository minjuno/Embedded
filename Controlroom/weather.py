import requests

API_KEY = '{your api keys}'

def get_weather(city):
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(weather_url)
    return response.json()

def set_background_image(description):
    if 'clear' in description:
        return 'https://example.com/snow.jpg'
    elif 'cloud' in description:
        return 'https://example.com/clouds.jpg'
    elif 'rain' in description:
        return 'https://example.com/mist.jpg'
    elif 'thunderstorm' in description:
        return 'https://example.com/thunderstorm.jpg'
    elif 'snow' in description:
        return 'https://example.com/snow.jpg'
    elif 'mist' in description:
        return 'https://example.com/mist.jpg'
    else:
        return 'https://example.com/default.jpg'
