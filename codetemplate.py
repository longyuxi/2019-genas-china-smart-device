import RPi.GPIO as GPIO  # Import GPIO Module
import time # Import sleep Module for timing

BUTTON_PIN = 21
LED_PIN = 20

GPIO.setmode(GPIO.BCM)  # Configures pin numbering to Broadcom reference
GPIO.setwarnings(False)  # Disable Warnings
GPIO.setup(LED_PIN, GPIO.OUT)  #Set our GPIO pin to output 
GPIO.output(LED_PIN, False)  #Set output to off
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set GPIO to input with a  pull-down resistor
GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, bouncetime=200)


def main():
    GPIO.output(LED_PIN, False) # Anything



try:
    main()
 
except KeyboardInterrupt:
    pass
 
finally:
    # Print some output message, etc.
    GPIO.cleanup()