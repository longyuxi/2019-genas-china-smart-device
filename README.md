# 2019-genas-china-smart-device
 
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

4. Use an IP scanner (such as the "Advanced IP Scanner" for Windows) to scan the network of the Pi. Once you find a device with the special name that you set in step 3, copy down its IP Address. Then use PuTTY to connect to the Pi. 

