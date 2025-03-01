from django.shortcuts import render
import requests
from decouple import config

def get_weather(request):
    city = request.GET.get('city', 'Praha') # Výchozí město bude Praha
    api_key = config('OPENWEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=cz"

    response = requests.get(url)
    weather_data = response.json()

    if response.status_code == 200:
        weather = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
        }
    else:
        weather = {'error': 'Město nebylo nalezeno. Zkuste jiné.'}

    return render(request, 'weather/weather.html', {'weather': weather})
