from bg_tts import talk  
from voice import speech_recognition
from temp import read_temp
import random

hello = ["Здрасти, как си?", "Хей, радвам се да те чуя!", "Здрасри! Името ми е Едвин. Приятно ми е!"]
speech_input = speech_recognition()

print(speech_input)

if "здрасти" in speech_input:
    talk(random.choice(hello))

print("А, да не забравя температурата е " + read_temp() + " градуса")
talk("А, да не забравя температурата е " + read_temp() + " градуса")
