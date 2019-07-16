import RPi.GPIO as GPIO
import time


## LED
# Surface LED pins
RED_LED = 20
YELLOW_LED = 16
GREEN_LED = 19
# Emitter
BLUELIGHT_EMITTER_LED = 26

## LCD
# GPIO to LCD mapping
LCD_RS = 7 # Pi pin 26
LCD_E = 8 # Pi pin 24
LCD_D4 = 25 # Pi pin 22
LCD_D5 = 24 # Pi pin 18
LCD_D6 = 23 # Pi pin 16
LCD_D7 = 18 # Pi pin 12

# LCD constants
LCD_CHR = True # Character mode
LCD_CMD = False # Command mode
LCD_CHARS = 16 # Characters per line (16 max)
LCD_LINE_1 = 0x80 # LCD memory location for 1st line
LCD_LINE_2 = 0xC0 # LCD memory location 2nd line

# Define main program code
def main():
 
 GPIO.setwarnings(False)
 GPIO.setmode(GPIO.BCM) # Use BCM GPIO numbers
 GPIO.setup(LCD_E, GPIO.OUT) # Set GPIO's to output mode
 GPIO.setup(LCD_RS, GPIO.OUT)
 GPIO.setup(LCD_D4, GPIO.OUT)
 GPIO.setup(LCD_D5, GPIO.OUT)
 GPIO.setup(LCD_D6, GPIO.OUT)
 GPIO.setup(LCD_D7, GPIO.OUT)

# Initialize display
 lcd_init()


 while True:
    lcd_text("Hello World!",LCD_LINE_1)
    lcd_text("",LCD_LINE_2)

    lcd_text("Rasbperry Pi",LCD_LINE_1)
    lcd_text("16x2 LCD Display",LCD_LINE_2)

    time.sleep(3) # 3 second delay

    lcd_text("ABCDEFGHIJKLMNOP",LCD_LINE_1)
    lcd_text("1234567890123456",LCD_LINE_2)

    time.sleep(3) # 3 second delay

    lcd_text("I love my",LCD_LINE_1)
    lcd_text("Raspberry Pi!",LCD_LINE_2)

    time.sleep(3)

    lcd_text("MBTechWorks.com",LCD_LINE_1)
    lcd_text("For more R Pi",LCD_LINE_2)

    time.sleep(3)

# End of main program code


# LCD functions
def lcd_init():
 lcd_write(0x33,LCD_CMD) # Initialize
 lcd_write(0x32,LCD_CMD) # Set to 4-bit mode
 lcd_write(0x06,LCD_CMD) # Cursor move direction
 lcd_write(0x0C,LCD_CMD) # Turn cursor off
 lcd_write(0x28,LCD_CMD) # 2 line display
 lcd_write(0x01,LCD_CMD) # Clear display
 time.sleep(0.0005) # Delay to allow commands to process

def lcd_write(bits, mode):
# High bits
 GPIO.output(LCD_RS, mode) # RS

 GPIO.output(LCD_D4, False)
 GPIO.output(LCD_D5, False)
 GPIO.output(LCD_D6, False)
 GPIO.output(LCD_D7, False)
 if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
 if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
 if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
 if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)

# Toggle 'Enable' pin
 lcd_toggle_enable()

# Low bits
 GPIO.output(LCD_D4, False)
 GPIO.output(LCD_D5, False)
 GPIO.output(LCD_D6, False)
 GPIO.output(LCD_D7, False)
 if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
 if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
 if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
 if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)

# Toggle 'Enable' pin
 lcd_toggle_enable()

def lcd_toggle_enable():
 time.sleep(0.0005)
 GPIO.output(LCD_E, True)
 time.sleep(0.0005)
 GPIO.output(LCD_E, False)
 time.sleep(0.0005)

def lcd_text(message,line):
 # Send text to display
 message = message.ljust(LCD_CHARS," ")

 lcd_write(line, LCD_CMD)

 for i in range(LCD_CHARS):
    lcd_write(ord(message[i]),LCD_CHR)


#Begin program
try:
 main()
 
except KeyboardInterrupt:
 pass
 
finally:
 lcd_write(0x01, LCD_CMD)
 lcd_text("So long!",LCD_LINE_1)
 lcd_text("MBTechWorks.com",LCD_LINE_2)
 GPIO.cleanup()