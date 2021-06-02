from bg_tts import talk
from voice import speech_recognition
from temp import read_temp
import random
import conversations
import wikipedia_check
import alarm
import schedule
import weather
import sys
import music
import youtube_music
from RPLCD import CharLCD
import RPi.GPIO as GPIO
from LCD import writeOnLCD
from pynotifier import Notification
import time

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23], numbering_mode=GPIO.BOARD, auto_linebreaks=True)

def read_input(speech_input):
    def if_match(cons):
        split = speech_input.split()
        if set(cons).issubset(set(split)):
            return True
        else:
            return False
        
    if if_match(["представи", "се"]):
         conversations.introduction()
         
    elif if_match(["кой", "си", "ти"]):
         conversations.introduction()
    
    elif if_match(["здрасти"]) or if_match(["здравей"]):
        conversations.hello_rep()
        
    elif if_match(["мерси"]) or if_match(["благодаря"]):
        conversations.thanks()
        
    elif if_match(["какво", "е"]):
        writeOnLCD("Wikipedia")
        wikipedia_check.search_in_wiki(speech_input)
       
    
    elif if_match(["какво", "можеш", "да", "правиш"]):
        conversations.i_can()
       
    elif if_match(["колко", "е", "температурата"]):
        conversations.temperature()

    elif if_match(["кажи", "температурата", "в"]) or if_match(["температурата", "в"]):
        weather.give_me_the_weather(speech_input)
        
    elif if_match(["дай", "прогнозата", "за"]):
        weather.give_me_the_weather(speech_input)
        
    elif if_match(["музика", "ютуб"]):
        writeOnLCD("Playing music from YT")
        youtube_music.play()
        
    elif if_match(['направи', 'аларма', 'за']):
        print("Това е демо за аларма.")
        talk("Това е демо за аларма.")
        alarm.alarm()
        
    elif if_match(["пусни", "музика"]):
        print("Търся песни!")
        writeOnLCD("Music () ) )")
        talk("Търся песни!")
        music.player(".")
        
    elif if_match(["спри", "се"]):
        talk("Дочуване")
        sys.exit()
         
    else:
        writeOnLCD(":(")
        conversations.problem()
        
    lcd.clear()
        
    

def main():
    writeOnLCD("Edwin Project")
    lcd.cursor_pos = (1, 0)
    writeOnLCD("ELSYS @ 2021")
    time.sleep(5)
    
    Notification(
	title='Edwin',
	description='Едвин стартира',
	duration=5,                          
	urgency='normal'
    ).send()
    
    lcd.clear()
    while True:
        try:
            writeOnLCD("Edwin is waiting.")
            speech_input = speech_recognition()
            print("Ти каза : " + speech_input)
            lcd.clear()
            read_input(speech_input)
            
        except KeyboardInterrupt:
            writeOnLCD("Bye Bye!")
            time.sleep(2)
            lcd.clear()
            sys.exit()
    
if __name__ == "__main__":
    main()
     
