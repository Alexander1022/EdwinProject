from bg_tts import talk
import random
import temp
from RPLCD import CharLCD
import RPi.GPIO as GPIO
from LCD import writeOnLCD
import time

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23], numbering_mode=GPIO.BOARD, auto_linebreaks=True)

def hello_rep():
    hello = ["Здрасти!", "Хей, радвам се да те чуя!"]
    c = random.choice(hello)
    print(c)
    writeOnLCD("Hi :)")
    talk(c)
    
def introduction():
    intros = ["Здрасти! Името ми е Едвин. Приятно ми е!", "Аз съм Едвин.", "За пореден път ти казвам, че се казвам Едвин!", "Едвин, казвам се Едвин."]
    c = random.choice(intros)
    print(c)
    writeOnLCD("Edwin :)")
    talk(c)

def i_can():
    print("Аз мога да говоря, да измервам температура в стаята, в която сте, да търся в Уикипедия, да пускам музика, да проверявам времето и още много.")
    talk("Аз мога да говоря, да измервам температура в стаята, в която сте, да търся в Уикипедия, да пускам музика, да проверявам времето и още много.")
    
def thanks():
    thanks_answers = ["Винаги съм тук.", "Няма защо.", "Винаги съм до теб."]
    c = random.choice(thanks_answers)
    print(c)
    writeOnLCD("<3")
    talk(c)
    
def problem():
    problem = ["Не разбрах това!", "Не знам какво да кажа, не разбрах!", "Стана проблем!"]
    c = random.choice(problem)
    print(c)
    talk(c)
    
def temperature():
    print("Температурата е: " + temp.read_temp() + " градуса")
    writeOnLCD(str(temp.read_temp()))
    talk("Температурата е" + temp.read_temp() + " градуса")
    