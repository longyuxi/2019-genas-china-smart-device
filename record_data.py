import sys, os, imp, time
import RPi.GPIO as GPIO
import threading

OUTPUT_FOLDER = os.path.expanduser("/home/pi/genas-data")
print("Welcome to the GENAS hardware data collection software.")

# Import LCD
# home_dir = os.path.expanduser("/home/pi/2019-genas-china-smart-device")
# lcd_file = os.path.join(home_dir, "LCD1602/lcd.py")
# lcd = imp.load_source('lcd', lcd_file)
try:
   import lcd
   lcd.setup()
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
   print("TCS34725 FAIL")
   exit()

# Import LED
try:
   import led
except:
   print("LED FAIL")
   exit()

# Import DS18B20
try:
   from w1thermsensor import W1ThermSensor
   temp_sensor = W1ThermSensor()
except:
   print("DS18B20 FAIL")
   exit()

# Import TSL2561
try:
   import TSL2561
except:
   print("TSL2561 FAIL")
   exit()

# raw_input("Startup complete. Make sure the box is empty, close the lid and press the ENTER key.")

OUTPUT_FILE = ""
OUTPUT_FILE_NAME = ""
# R = -1
# G = -1
# B = -1
# LuxFull = -1
# LuxVisible = -1
# Temperature = -1

def prep():
    """ Run before capturing data

    Create a new data file
    """
    global OUTPUT_FILE
    global OUTPUT_FILE_NAME
    filename = "data_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".csv"
    OUTPUT_FILE_NAME = os.path.join(OUTPUT_FOLDER, filename)
    OUTPUT_FILE = open(OUTPUT_FILE_NAME, 'w')
    print("Data file at " + OUTPUT_FILE.name)
    OUTPUT_FILE.write("Concentration,LuxFull,LuxVisible,R,G,B,Temperature\n")
    OUTPUT_FILE.close()
    writeData(0)

def writeData(concentration):
    led.emitter(True)
    time.sleep(1) # To wait for I2C Bus to update
    R, G, B, c = tcs.get_raw_data()
    LuxFull = TSL2561.fullSpectrumValue()
    LuxVisible = TSL2561.visibleValue()
    print(LuxVisible)
    Temperature = temp_sensor.get_temperature()
    line = str(concentration) + "," + str(LuxFull) + "," + str(LuxVisible) + "," + str(R) + "," + str(G) + "," + str(B) + "," + str(Temperature) + "\n"
    OUTPUT_FILE = open(OUTPUT_FILE_NAME, 'a')
    OUTPUT_FILE.write(line)
    OUTPUT_FILE.close()
    led.emitter(False)

try:
    prep()
    while True:
        conc = input("Please close the lid, then input the concentration of the next sample. Ctrl + C to quit. \n")
        try:
            writeData(conc)
        except:
            print("Data not written successfully. Try again. \n")
except KeyboardInterrupt:
    print("Exit")
finally:
    print("Goodbye. See your file at " + OUTPUT_FILE_NAME)