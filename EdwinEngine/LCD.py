from RPLCD import CharLCD
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)



lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23], numbering_mode=GPIO.BOARD, auto_linebreaks=False)

def writeOnLCD(string):
    lcd.write_string(string)