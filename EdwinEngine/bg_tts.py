import pyttsx3

def talk(sentence):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'bulgarian')
    engine.setProperty('rate', 155)
    engine.say(sentence)    
    engine.runAndWait()
