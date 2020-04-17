#PIP install pyserial
#PIP install maidenhead
# 
 
import threading
import configparser
import time
import serial
import maidenhead as mh
import os
import platform
import sys
import traceback
import settings
#from OSGridConverter import latlong2grid 

platform_windows='Windows'
platform_linux='Linux'

configfilename=sys.path[0]+"/gps.cfg"

sentence = "$GPRMC"
alt_sentence = "$GPGGA"
time_sentence = "$GPZDA"


south='S'
west='W'

readGPS=True
class GPSListener(threading.Thread):
    def __init__(self, comportName, comportSpeed, precision, showoutput):
        threading.Thread.__init__(self)
        self.readGPS=False
        try:
            
            self.status="GPS Running"
           
            self.location_precision=int(precision)

            self.comPort = comportName
            
            self.comPortSpeed = comportSpeed

            self.showOutput=showoutput
            #set COM3 for testing. the config should have loaded 
            #and the correct com port sent in which will be set later.
        
            print('Location Precision is %s' % (self.location_precision,))
            print('Initializing GPS on '+self.comPort+'. Com port speed='+self.comPortSpeed+'. Please wait....')
            
            self.current_ngr = None
            self.current_epoch = None
            self.current_lon = None
            self.current_lat = None
            self.altitude = None
            self.mhGrid = None

            self.mh_grid = None

            #comportspeed=self.getComPortSpeed()
            
            self.gps = serial.Serial(self.comPort,self.comPortSpeed)
            #self.gps = Serial(port=self.comPort, baudrate=self.comPortSpeed)
            
            
            self.readGPS=True
        except:
            print("I'm having a problem getting data from your GPS, error message below:")
            traceback.print_exc()
            self.setStatus("Error initilizing GPS, check com port and restart this app.")
    def setStatus(self, statusString):
        self.status=statusString  
    def getStatus(self):
        return self.status
    def setPrecision(self, precision):
        self.location_precision = precision
    def getAltitude(self):
        return self.altitude
    def getCurrentLat(self):
        return self.current_lat
    def getCurrentLon(self):
        return self.current_lon
    def get_current_latlon(self):
        self.current_latlon = str(self.current_lat)+" "+str(self.current_lon)
        return self.current_latlon
    def get_current_epoch(self):
        return self.current_epoch
    def get_ngr(self):
        return ""
        #return self.current_ngr
    def getMaidenhead(self):
        return self.mhGrid
    def setReadGPS(self, read):
        self.readGPS = read
    def setShowDebug(self, show):
        self.showOutput=show
        
    def run(self):
        showoutput=self.showOutput
        
        try:
            while self.readGPS:
                line = self.gps.readline()
    
                gpsData = line.decode().split(",")

                if showoutput==1:
                    print(gpsData)
                
                if gpsData[0]==time_sentence:
                    gpsTime=gpsData
                    self.current_epoch=1
                    print(gpsTime)
                if gpsData[0]==alt_sentence:
                    #$GPGGA
                    gpsAlt = gpsData[9]
                    gpsUnit = gpsData[10]
                    self.altitude = gpsAlt+gpsUnit
                if gpsData[0]==sentence:
                    if gpsData[2]=='A':
                        gpsTime = gpsData[1]
                        #print(gpsTime)
                        gpsLat=float(gpsData[3])
                        gpsN=gpsData[4] 
                        gpsLon=float(gpsData[5])
                        gpsE=gpsData[6]

                        if (gpsN==south):
                            gpsLat = -gpsLat

                        latDeg = int(gpsLat/100)
                        latMin = gpsLat-latDeg*100
                        lat=latDeg+latMin/60

                        if (gpsE==west):
                            gpsLon = -gpsLon

                        lonDeg = int(gpsLon/100)
                        lonMin = gpsLon-lonDeg*100
                        lon=lonDeg+lonMin/60

                        self.mhGrid = mh.toMaiden(lat,lon,precision=self.location_precision)
                        #g=latlong2grid(lat,lon)
                        #self.current_ngr = str(g)
                        self.current_lat = lat
                        self.current_lon = lon
                        
                        #print('Location: %s, %s, %s, %s' % (lat,lon,self.mhGrid,g))
                        #self.setReadGPS(False)
                        #time.sleep(1)
                    #else:
                    #    print("GPS Active but no Fix")
                    #    print(gpsData)
        except (KeyboardInterrupt, SystemExit):
            self.setReadGPS(False)
            self.join()
            print("Done.\nClosing GPS Listener.")

#no longer support running standalone. may re-implement later
#if __name__ == "__main__":
#    try:
#        gpsl = GPSListener()
#        gpsl.start()    
#        #gpsl.setReadGPS(False)
#    except (KeyboardInterrupt, SystemExit):
#        gpsl.setReadGPS(False)
#        print("Done.\nClosing GPS Listener.")

