from bg_tts import talk
import random

def hello_rep():
    hello = ["Здрасти!", "Хей, радвам се да те чуя!"]
    c = random.choice(hello)
    print(c)
    talk(c)
    
def introduction():
    intros = ["Здрасти! Името ми е Едвин. Приятно ми е!", "Аз съм Едвин.", "За пореден път ти казвам, че се казвам Едвин!", "Едвин, казвам се Едвин."]
    c = random.choice(intros)
    print(c)
    talk(c)
    
def problem():
    problem = ["Не разбрах това!", "Не знам какво да кажа, не разбрах!", "Стана проблем!"]
    c = random.choice(problem)
    print(c)
    talk(c)