from bg_tts import talk
from voice import speech_recognition
from temp import read_temp
import led_indicators
import random
import conversations
import wikipedia_check


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
        
    elif if_match(["какво", "е"]):
       wikipedia_check.search_in_wiki(speech_input)
         
    else:
        conversations.problem()
        
    

def main():
    speech_input = speech_recognition()
    print("Ти каза : " + speech_input)
    read_input(speech_input)
    
if __name__ == "__main__":
    main()
     

#print("А, да не забравя температурата е " + read_temp() + " градуса")
#talk("А, да не забравя температурата е " + read_temp() + " градуса")
