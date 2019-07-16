import RPi.GPIO as GPIO  # Import GPIO Module
from time import sleep  # Import sleep Module for timing

BUTTON_PIN = 21
LED_PIN = 20

GPIO.setmode(GPIO.BCM)  # Configures pin numbering to Broadcom reference
GPIO.setwarnings(False)  # Disable Warnings
GPIO.setup(LED_PIN, GPIO.OUT)  #Set our GPIO pin to output 
GPIO.output(LED_PIN, False)  #Set output to off
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set GPIO to input with a  pull-down resistor
GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, bouncetime=200)


def main():
    while (True):
        if GPIO.event_detected(BUTTON_PIN):  # Check to see if button has been pushed
            activate = True
            while (activate is True):  # Execute this code until the button is pushed again
                GPIO.output(LED_PIN, True)  # Turn LED on
                sleep(0.01)
                GPIO.output(LED_PIN, False) # Turn LED off
                sleep(0.01)
                if GPIO.event_detected(BUTTON_PIN):  # Check for a 2nd button push
                    activate = False
        else:
            GPIO.output(LED_PIN, False)  # Turn LED off

try:
    main()
 
except KeyboardInterrupt:
    pass
 
finally:
    GPIO.output(LED_PIN, True)  # Turn LED on
    sleep(0.5)
    GPIO.cleanup()