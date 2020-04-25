JS8CallUtils_v2

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
Before running for the first time install the required python modules:
<br>
<b>LINUX (including Raspberry Pi)<br>
pip3 install maidenhead<br>
pip3 install serial<br>
pip3 install configparser<br>
pip3 install gps<br>
<br></b>
<b>Windows<br>
py -m pip install maidenhead<br>
py -m pip install serial<br>
py -m pip install pyserial<br>
py -m pip install configparser<br>
py -m pip install gps<br></b>

<br>
on unix now enter<br><b> chmod +x js8callutilsGPSD.py</b><br>

you should now be ready to run the app
<br>
Linux:<br>
<b>./JS8CallUtils_v2.py</b>
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
You can find my social media contact info here: http:m0iax.com/findme

73!

Mark


