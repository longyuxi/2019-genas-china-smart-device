# Features

Startup script checks if all interfaces can be instantiated and print out the currently connected Wi-Fi network and its IP address for easy SSH.

*To be written*

# To set up the hardware and software
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