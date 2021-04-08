import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)

def startup():
	GPIO.output(17, GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(17, GPIO.LOW)
	GPIO.output(27, GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(22, GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(22, GPIO.LOW)
	time.sleep(0.2)
	GPIO.output(22, GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(22, GPIO.LOW)
	GPIO.output(27, GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(17, GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(17, GPIO.LOW)
	time.sleep(0.2)
	
def problem():
	GPIO.output(22, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(22, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(22, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(22, GPIO.LOW)
	
def success():
	GPIO.output(17, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(17, GPIO.LOW)
