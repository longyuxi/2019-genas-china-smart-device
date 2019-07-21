import RPi.GPIO as GPIO
import time
import threading

RED_LED_PIN = 20
YELLOW_LED_PIN = 16
GREEN_LED_PIN = 19
EMITTER_LED_PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED_LED_PIN,GPIO.OUT)
GPIO.setup(YELLOW_LED_PIN,GPIO.OUT)
GPIO.setup(GREEN_LED_PIN,GPIO.OUT)
GPIO.setup(EMITTER_LED_PIN,GPIO.OUT)

def redLight(t):
    GPIO.output(RED_LED_PIN, True)
    time.sleep(t)
    GPIO.output(RED_LED_PIN, False)

def yellowLight(t):
    GPIO.output(YELLOW_LED_PIN, True)
    time.sleep(t)
    GPIO.output(YELLOW_LED_PIN, False)

def greenLight(t):
    GPIO.output(GREEN_LED_PIN, True)
    time.sleep(t)
    GPIO.output(GREEN_LED_PIN, False)

def welcome():
    threading.Thread(target=redLight, args=(0.3, )).start()
    time.sleep(0.1)
    threading.Thread(target=yellowLight, args=(0.3, )).start()
    time.sleep(0.1)    
    threading.Thread(target=greenLight, args=(0.3, )).start()
    time.sleep(0.1)
    threading.Thread(target=yellowLight, args=(0.3, )).start()
    time.sleep(0.1)
    threading.Thread(target=redLight, args=(0.3, )).start()
    time.sleep(0.1)

    threading.Thread(target=redLight, args=(0.1, )).start()
    threading.Thread(target=yellowLight, args=(0.1, )).start()
    threading.Thread(target=greenLight, args=(0.1, )).start()
    time.sleep(0.2)

    threading.Thread(target=redLight, args=(0.1, )).start()
    threading.Thread(target=yellowLight, args=(0.1, )).start()
    threading.Thread(target=greenLight, args=(0.1, )).start()
    time.sleep(0.2)

    threading.Thread(target=redLight, args=(0.1, )).start()
    threading.Thread(target=yellowLight, args=(0.1, )).start()
    threading.Thread(target=greenLight, args=(0.1, )).start()
    time.sleep(0.2)

def emitter(status):
    GPIO.output(EMITTER_LED_PIN, status)

welcome()