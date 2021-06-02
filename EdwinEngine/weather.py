import requests, json
from bg_tts import talk
import datetime
from RPLCD import CharLCD
import RPi.GPIO as GPIO
from LCD import writeOnLCD

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "fbb0126317878e1dd873d7d0326efb6d"

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23], numbering_mode=GPIO.BOARD, auto_linebreaks=True)

def give_me_the_weather(speech_input):
    string = speech_input.split()
    
    if 'кажи' in string:
        string.remove('кажи')
        
    if 'в' in string:
        string.remove('в')
        
    if 'температурата' in string:
        string.remove('температурата')
        
    if 'температура' in string:
        string.remove('температура')
        
    if 'едвин' in string:
        string.remove('едвин')
        
    if 'Едвин' in string:
        string.remove('Едвин')
        
    if 'дай' in string:
        string.remove('дай')
        
    if 'прогнозата' in string:
        string.remove('прогнозата')
        
    if 'прогноза' in string:
        string.remove('прогноза')
        
    if 'за' in string:
        string.remove('за')
        
    location = ' '.join(string)
    print(location)
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
        writeOnLCD(str(cels) + " C")
        talk("Температурата в " + location + " е " + str(cels) + " градуса")
        lcd.clear()
        
        print("Но се чувства като " + str(fl) + " градуса")
        writeOnLCD(str(fl) + " C")
        talk("Но се чувства като " + str(fl) + " градуса")
        lcd.clear()
        
        print("Изгревът е към " + str(sunrise))
        writeOnLCD(str(sunrise) + " sunsrise")
        talk("Изгревът е към " + str(sunrise))
        lcd.clear()
        
        print("Залезът е към " + str(sunset))
        writeOnLCD(str(sunset) + " sunset")
        talk("Залезът е към " + str(sunset))
        lcd.clear()
        
    else:
        print("Error in HTTP request")
        writeOnLCD("Error in HTTP request")
        lcd.clear()
