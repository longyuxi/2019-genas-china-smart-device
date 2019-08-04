import RPi.GPIO as GPIO
import time
import threading

RED_LED_PIN = 20
YELLOW_LED_PIN = 16
GREEN_LED_PIN = 19
BLUE_LED_PIN = 5
WHITE_LED_PIN = 6
EMITTER_LED_PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED_COLLECTION = [RED_LED_PIN, YELLOW_LED_PIN, GREEN_LED_PIN, BLUE_LED_PIN, WHITE_LED_PIN, EMITTER_LED_PIN]
GPIO.setup(LED_COLLECTION,GPIO.OUT)

dont_blink = False
def blink_led(pin, uptime, downtime):
    global dont_blink
    while not dont_blink:
        GPIO.output(pin, True)
        time.sleep(uptime)
        GPIO.output(pin, False)
        time.sleep(downtime)

def stop_blinking():
    global dont_blink
    dont_blink = True

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
