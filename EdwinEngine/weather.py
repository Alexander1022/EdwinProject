import requests, json
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "fbb0126317878e1dd873d7d0326efb6d"

def give_me_the_weather(speech_input):
    string = speech_input.split()
    string.remove('колко')
    string.remove('е')
    string.remove('температурата')
    string.remove('в')
    location = ' '.join(string)
    
    URL = BASE_URL + "q=" + location + "&appid=" + API_KEY
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']

        cels = round(temperature - 273.15)

        print(cels)

    else:
        print("Error in HTTP request")
