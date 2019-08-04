# Features
Startup script checks if all interfaces can be instantiated and print out the currently connected Wi-Fi network and its IP address for easy SSH.

# Design diagrams
[1](https://33b68295032b152c.share.mingdao.net/apps/kcshare/5d46bb28eb60f43138261e44)
[2](https://33b68295032b152c.share.mingdao.net/apps/kcshare/5d46bb28eb60f43138261e44)
[3](https://33b68295032b152c.share.mingdao.net/apps/kcshare/5d46bb2aeb60f43bcc77df6b)

# User mode (model still under development)
## To enter user mode
Push the button when the LCD displays the Wi-Fi information. From there you can use the appliance to get concentration data from samples based on previous models (which are to be built).

## To use user mode
Put in your sample when the screen prompts you to. After you put in the sample, push the button and the machine will start analyzing it. When it is done analyzing, the measured concentration level will be printed out on the LCD screen and one of the LEDs (green, yellow, red) will light up to indicate the status of your sample (good, worse, bad). Then when you are done viewing the results of this sample, push the button again and start over from the beginning of this paragraph.

# Startup sequence
The startup script should detect most of the connection problems. Should there be no connection problems, events that would happen when you plug in are as follows:
- LCD screen prints out "LCD Success".
- LEDs show a light chasing sequence, then all flash three times.
- LCD screen prints out "All OK" on first line, "Lux=...,T=..." on second line.
- As soon as the Pi is connected to the network, LCD screen prints Wi-Fi network name on first line, local IP address on second line (which is the IP address you use to connect to the Pi).

Allow 30 seconds before the Pi starts the startup sequence above. Should the startup not abide to the sequence above, the LCD should print out the error (if the LCD is working in the first place). Refer to the "Errors" section below for more information.

# Setting up the hardware and software
List of sensors currently installed:
- TCS34725 color (RGB) sensor with inaccurate light intensity function
- DS18B20 temperature sensor
 
1. Use Etcher to flash Raspbian image to the Pi.

2. Add an empty file named `ssh` to the **boot partition**.  This enables the ssh daemon when it boots.

3. Edit these files on the **OS partition**:
  * Edit `/etc/hostname` and `/etc/hosts` to change “raspberrypi” to a **unique host name**, like `smart-detector-pi`.
  * Edit `/etc/wpa_supplicant/wpa_supplicant.conf` to add your WiFi authentication (updating "country" if appropriate):

```
country=us
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 scan_ssid=1
 ssid="your WiFi name (SSID)"
 psk="your WiFi password"
}
```

4. Use an IP scanner (such as the "Advanced IP Scanner" for Windows) to scan the network of the Pi. Once you find a device with the special name that you set in step 3, copy down its IP Address. Then use PuTTY to connect to the Pi via SSH by changing the `hostname or IP address` field to the one that you found.

5. Run the following commands to start the setup script.
```
wget https://raw.githubusercontent.com/longyuxi/2019-genas-china-smart-device/master/setup.sh
chmod +x ./setup.sh
sudo ./setup.sh
```

6. Run `crontab -e` and append the line `@reboot sudo python /home/pi/2019-genas-china-smart-device/practice.py &` to run the script at startup. 

# To view the wiring diagram

Download *Fritzing* to open the .fzz file. You possibly need to download the Fritzing parts file for TCS34725.

# To log data

Currently, in order to log the data, you have to SSH into the Pi and run a Python script. This will be improved in the future.

1. When in the `2019-genas-china-smart-device` directory, run `sudo python record_data.py`. Make sure the box is empty.
2. Leave the lid closed until the script prompts you to insert your sample.
3. Open the lid.
4. Put in/replace the sample.
5. Key in the flow cytometry-determined flourescent value and press ENTER.
6. Repeat from step 3. When you are done, hit *CTRL + C* on your keyboard to exit the program.

The file is automatically saved every time you press ENTER, so no worries if the power goes out.

# Errors
1. **There is no output on LCD**: There is probably a connection problem between the Pi and the LCD. Refer to the wiring diagram to correct the connection. If there is no problem in connection, there might be a problem auto-executing the script. Make sure you have followed all the steps in the setup section above.
2. **TCS34725 FAIL, LED FAIL, DS18B20 FAIL, TSL2561 FAIL or Emitter FAIL**: Refer to the wiring diagram to correct the wiring.
3. **Wi-Fi not connected**: Make sure you are in range of the Wi-Fi adapter. The wireless adapter on the Raspberry Pi might be less powerful than your computer or phone's Wi-Fi adapter.

