import sys, os, imp, time
import RPi.GPIO as GPIO
import threading

# Import LCD
# home_dir = os.path.expanduser("/home/pi/2019-genas-china-smart-device")
# lcd_file = os.path.join(home_dir, "LCD1602/lcd.py")
# lcd = imp.load_source('lcd', lcd_file)
try:
   import lcd
   lcd.setup()
   lcd_welcome = threading.Thread(target=lcd.lcd_success_message)
   lcd_welcome.start()
except:
   print("FATAL: LCD IMPORT FAILURE")
   exit()

# Import TCS34725
try:
   
   # tcs_file = os.path.join(home_dir, "TCS34725/Adafruit_TCS34725.py")
   # Adafruit_TCS34725 = imp.load_source('TCS34725', tcs_file)
   import Adafruit_TCS34725
   import smbus
   tcs = Adafruit_TCS34725.TCS34725()
   r, g, b, c = tcs.get_raw_data()
   lux = Adafruit_TCS34725.calculate_lux(r, g, b)
   print('Current color in box: red={0} green={1} blue={2} clear={3}. Lux={4}'.format(r, g, b, c, lux))
   # TCS34725 functions
   # # Read the R, G, B, C color data.
   # r, g, b, c = tcs.get_raw_data()

   # # Calculate color temperature using utility functions.  You might also want to
   # # check out the colormath library for much more complete/accurate color functions.
   # color_temp = Adafruit_TCS34725.calculate_color_temperature(r, g, b)

   # # Calculate lux with another utility function.
   # lux = Adafruit_TCS34725.calculate_lux(r, g, b)
   # lcd.lcd_text('R={0} G={1} B={2} C={3} L={4}'.format(r, g, b, c, lux), lcd.LCD_LINE_2)
   # time.sleep(1)
   # lcd.lcd_clear_screen()
except:
   lcd.lcd_text("TCS34725 FAIL", lcd.LCD_LINE_2)
   exit()

# Import LED
try:
   import led
except:
   lcd.lcd_text("LED FAIL", lcd.LCD_LINE_2)
   exit()

# Import DS18B20
try:
   from w1thermsensor import W1ThermSensor
   temp_sensor = W1ThermSensor()
except:
   lcd.lcd_text("DS18B20 FAIL", lcd.LCD_LINE_2)
   exit()

# Import TSL2561
try:
   import TSL2561
except:
   lcd.lcd_text("TSL2561 FAIL", lcd.LCD_LINE_2)
   exit()

lcd_welcome.join()
lcd.lcd_text("All OK", lcd.LCD_LINE_1)
lcd.lcd_text("Lux={0}".format(TSL2561.visibleValue()), lcd.LCD_LINE_2)
time.sleep(1)
lcd.lcd_clear_screen()