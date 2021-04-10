from bg_tts import talk
from voice import speech_recognition
from temp import read_temp
import led_indicators
import random
import conversations
import wikipedia_check
import alarm
import schedule
from pynotifier import Notification

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
    
    elif if_match(["здрасти"]):
        conversations.hello_rep()
        
    elif if_match(["мерси"]) or if_match(["благодаря"]):
        conversations.thanks()
        
    elif if_match(["какво", "е"]):
       wikipedia_check.search_in_wiki(speech_input)
       
    elif if_match(["колко", "е", "температурата"]):
        conversations.temperature()
        
    elif if_match(['направи', 'аларма', 'за']):
        print("Това е демо за аларма.")
        talk("Това е демо за аларма.")
        alarm.alarm()
         
    else:
        conversations.problem()
        
    

def main():
    Notification(
	title='Edwin',
	description='Едвин стартира',
	duration=5,                          
	urgency='normal'
    ).send()
    while True:
        speech_input = speech_recognition()
        print("Ти каза : " + speech_input)
        read_input(speech_input)
    
if __name__ == "__main__":
    main()
     