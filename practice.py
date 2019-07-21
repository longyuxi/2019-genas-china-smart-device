import sys, os, imp, time
import RPi.GPIO as GPIO
import threading

# The threshold used to confirm that blue light emitters are connected. 
# Set to be half of expected value when on.
EMITTER_THRESHOLD_LUX = 1000 

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
   tcs.set_interrupt(True)
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

def testEmitter():
   led.emitter(True)
   blankValue = TSL2561.visibleValue()
   time.sleep(1)
   coloredValue = TSL2561.visibleValue()
   if (coloredValue - blankValue) < EMITTER_THRESHOLD_LUX:
      # Emitter not connected4
      lcd.lcd_text("Emitter FAIL", lcd.LCD_LINE_1)
      sys.exit()
   else:
      led.emitter(False)
      return
   

lcd_welcome.join()
emitterTest = threading.Thread(target=testEmitter)
emitterTest.start()
emitterTest.join()
led.emitter(False)
lcd.lcd_text("All OK", lcd.LCD_LINE_1)
lcd.lcd_text("Lux={0},T={1}".format(TSL2561.visibleValue(), temp_sensor.get_temperature()), lcd.LCD_LINE_2)
time.sleep(1)
lcd.lcd_clear_screen()
count = 0
while True:
   wifi_name = os.popen('iwgetid -r').read()
   wifi_name = wifi_name[0:(len(wifi_name)-1)].strip()
   if(wifi_name == ''):
      time.sleep(1)
      count = count + 1
   elif count > 15:
      break
   else:
      break

if count > 15:
   lcd.lcd_text("Wi-Fi", lcd.LCD_LINE_1)
   lcd.lcd_text("Not connected", lcd.LCD_LINE_2)
else:
   wifi_name = os.popen('iwgetid -r').read()
   wifi_name = wifi_name[0:(len(wifi_name)-1)].strip()
   ipaddr = os.popen('hostname -I').read()
   ipaddr = ipaddr[0:(len(ipaddr)-1)].strip()
   lcd.lcd_text(wifi_name, lcd.LCD_LINE_1)
   lcd.lcd_text(ipaddr, lcd.LCD_LINE_2)
