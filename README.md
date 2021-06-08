JS8CallUtils_v2

<b>Note to existing users or users that already have python installed</b>
ensure you have the latest maidenhead python code using the command<br>
<b>pip install --upgrade maidenhead</b>
<br>
maidenhead 1.5.0 had chnaged the call to convert lat,lon to maidenhead so if you see and error then please ensure you update.
<br>

<b>NOTE</b>
In order to use SOTA Spot Option for APRS you need to register. Please see https://www.sotaspots.co.uk/Aprs2Sota_Info.php for more details
<br>

This project is designed for use with JS8Call by Jordan KN4CRD - http://js8call.com

GPS Functions in this version will work on a Windows, Linux (Including Raspberry Pi) and Mac OS computer.

If you have a GPS connected to your computer it will allow you to send your maidenhead grid to JS8Call to set its locator and/or to transmit to @APRSIS<br>
For raspberry pi please ensure you have installed and configured the GPSD service, searial connection does not currently work on the Pi.. I will investigate and fix that in future releases.

It also allows you to send messages into the ARRS system, APRS, Email or SMS message types.

To use, download the files, ensure you have python version 3 installed and install the follwoing dependencies enter the following on the command line:

<b>Note that you require Python to be installed version 3.7 and above. Other versions may not work correctly for all the functions</b>
<br>
Clone or download and unzip the code. NOw run a command prompt and cd to the downloaded directory.
<br>
<b>cd JS8CallUtilities _V2</b><br>
<br>
to ensure you have the correct versions of the required python modules run the following command:

<br>

<b>LINUX (including Raspberry Pi)<br>
pip3 install -r requirements.txt

<b>Windows<br>
py -m pip3 install -r requirements.txt

<br>
on Linux now enter<br><b> chmod +x JS8CallUtils_v2.py</b><br>

<p>Note, I found that on the <b>raspberry pi</b> at least if I had the serial package installed I was not able to use the serial GPS option. I was able to resolve this problem by removing it 
  
pip3 uninstall serial
  
(note that you should install pyserial as in the above instructions if you want to use gps in serial port mode)
the comport value to enter should be
/dev/ttyACM0

</p>

you should now be ready to run the app
<br>
Linux:<br>
  <b>./JS8CallUtils_v2.py</b><br>
  <p>If that does not work try</p>
<b>python3 JS8CallUtils_v2.py</b>
<br>
Windows<br>
<b>py JS8CallUtils_v2.py</b>

When running click on settings and select the GPS Interface type. On Windows select coim port, on Raspberry Pi select GPSD and on Linux
select either GPSD or com port. Select 'None' if you do not have a GPS attached.
<br>
Enter the correct name for the com port that your GPS is using. on windows this will be something like 'COM4' (the number after COM on your system 
will probably be different)
on Linux it will be something like /dev/ttyAMA0 for example.
<br>
Set the other options you want (the default ones work nicely) and click Save. 
If you have configured the GPS correctly you should now be able to use the GPS functions on the GPS page (note it may take a few seconds on 
some systems to start the GPS and get a fix)
<br>
The APRS functions should be self explanatory. But if you need help please let me know.
<br>
The new networkGPS option has been tested with the Andoid App "GPS Tether". It may work with other NMEA output apps/devices. Please report any problems and I will address them as soon as I can.
<br>
You can find my social media contact info here: http:m0iax.com/findme

73!

Mark


