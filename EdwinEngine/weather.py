import requests, json
from bg_tts import talk
import datetime

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "fbb0126317878e1dd873d7d0326efb6d"

def give_me_the_weather(speech_input):
    string = speech_input.split()
    if 'кажи' in string:
        string.remove('кажи')
        
    string.remove('температурата')
    string.remove('в')
    location = ' '.join(string)
    
    URL = BASE_URL + "q=" + location + "&appid=" + API_KEY
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        sys = data['sys']
        
        temperature = main['temp']
        feels_like = main['feels_like']
        
        cels = round(temperature - 273.15)
        fl = round(feels_like - 273.15)
        
        sunrise = datetime.datetime.fromtimestamp(sys['sunrise'])
        sunrise = sunrise.strftime("%H:%M")
        sunset = datetime.datetime.fromtimestamp(sys['sunset'])
        sunset = sunset.strftime("%H:%M")
        
        print("Температурата в " + location + " е " + str(cels) + " градуса")
        talk("Температурата в " + location + " е " + str(cels) + " градуса")
        
        print("Но се чувства като " + str(fl) + " градуса")
        talk("Но се чувства като " + str(fl) + " градуса")
        
        print("Изгревът е към " + str(sunrise))
        talk("Изгревът е към " + str(sunrise))
        
        print("Залезът е към " + str(sunset))
        talk("Залезът е към " + str(sunset))

    else:
        print("Error in HTTP request")
