import wikipedia
from bg_tts import talk
wikipedia.set_lang("bg")

def search_in_wiki(speech_input):
    string = speech_input.split()
    string.remove('какво')
    string.remove('е')
    search = ' '.join(string)

    try:
        output = wikipedia.summary(search, sentences=2)
        print(output)
        talk(output)
    except wikipedia.exception.DisambiguationError as error:
        print("Има ерор в Уикипедия!")
        talk("Има еррор в Уикипедия!")