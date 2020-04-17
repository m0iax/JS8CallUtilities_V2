JS8CallUtils_v2

This project is designed for use with JS8Call by Jordan KN4CRD - http://js8call.com

GPS Functions in this version will work on a Windows, Linux (Including Raspberry Pi) and Mac OS computer.

If you have a GPS connected to your computer it will allow you to send your maidenhead grid to JS8Call to set its locator and/or to transmit to @APRSIS
For raspberry pi please ensure you have installed and configured the GPSD service, searial connection does not currently work on the Pi.. I will investigate and fix that in future releases.

It also allows you to send messages into the ARRS system, APRS, Email or SMS message types.

To use, download the files, ensure you have python version 3 installed and install the follwoing dependencies enter the following on the command line:

Clone or download and unzip the code. NOw run a command prompt and cd to the downloaded directory.

<b>cd JS8CallUtilities_V2</b>

Before running for the first time install the required python modules:

LINUX (including Raspberry Pi)
pip3 install maidenhead
pip3 install serial
pip3 install configparser
pip3 install gps

Windows
py -m pip install maidenhead
py -m pip install serial
py -m pip install configparser
py -m pip install gps


on unix now enter chmod +x js8callutilsGPSD.py

you should now be ready to run the app

Linux:<br>
<b>./JS8CallUtils_v2.py</b>

Windows<br>
<b>py JS8CallUtils_v2.py</b>

When running click on settings and select the GPS Interface type. On Windows select coim port, on Raspberry Pi select GPSD and on Linux
select either GPSD or com port. Select 'None' if you do not have a GPS attached.

Enter the correct name for the com port that your GPS is using. on windows this will be something like 'COM4' (the number after COM on your system 
will probably be different)
on Linux it will be something like /dev/ttyAMA0 for example.

Set the other options you want (the default ones work nicely) and click Save. 
If you have configured the GPS correctly you should now be able to use the GPS functions on the GPS page (note it may take a few seconds on 
some systems to start the GPS and get a fix)

The APRS functions should be self explanatory. But if you need help please let me know.

You can find my social media contact info here: http:m0iax.com/findme

73!

Mark


