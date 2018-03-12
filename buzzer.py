import RPi.GPIO as GPIO
import time
timeout = time.time() + 10
timeout2 = time.time() + 1

BeepPin = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
	GPIO.setup(BeepPin, GPIO.OUT)   # Set BeepPin's mode is output
	GPIO.output(BeepPin, GPIO.HIGH) # Set BeepPin high(+3.3V) to off beep

def loop():
	setup()
	while True:
		GPIO.output(BeepPin, GPIO.LOW)
		time.sleep(0.1)
		GPIO.output(BeepPin, GPIO.HIGH)
		time.sleep(0.1)
		if(time.time()> timeout):
			destroy()
			break

def add_contact():
	while True:
		GPIO.output(BeepPin, GPIO.LOW)
		time.sleep(0.1)
		GPIO.output(BeepPin, GPIO.HIGH)
		time.sleep(0.1)
		if(time.time()> timeout2):
			destroy()
			break

def destroy():
	GPIO.output(BeepPin, GPIO.HIGH)    # beep off
	GPIO.cleanup()                     # Release resource
