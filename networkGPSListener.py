import threading
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import time
import configparser
import os
import traceback
import maidenhead as mh

PACKET_SIZE=256
SENTENCE = "$GPRMC"
ALTERNATE_SENTENCE = "$GNRMC"
ALT_SENTENCE = "$GPGGA"
TIME_SENTENCE = "$GPZDA"

SOUTH='S'
WEST='W'

class netWorkGPS(threading.Thread):
    
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
    def teminate(self):
        self.listening=False   
        if self.sock!=None:
            self.sock.setblocking(False)
    def setShowDebug(self, show):
        self.showOutput=show

    def __init__(self, serverip, serverport, precision, showoutput):
        super().__init__()
        try:
            t = threading.Thread.__init__(self)
            
            self.status="GPS Running"
            self.location_precision=int(precision)
    
            self.showoutput = showoutput
            self.showLogOutput = False
            self.first = False
            self.listen = (serverip, int(serverport))

            self.current_ngr = None
            self.current_epoch = None
            self.current_lon = None
            self.current_lat = None
            self.altitude = None
            self.mhGrid = None
            self.i = 0
        except:
            print("I'm having a problem getting data from your GPS, error message below:")
            traceback.print_exc()
            self.setStatus("Error initilizing GPS, check com port and restart this app.")
    def run(self):
        print('listening on', ':'.join(map(str, self.listen)))
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect(self.listen)
        self.listening = True
        try:
            while self.listening:
               # self.showoutput=True
               # content, addr = self.sock.recvfrom(65500)
                #if self.showoutput:
                #    print(content)
                datalist = self.sock.recv(PACKET_SIZE)
                #if self.showoutput:
                ##    print(datalist)
                self.i=self.i+1
                
                #print(datalist.decode())
                nmeaRows=datalist.decode().split("\r\n")   
                
                for row in nmeaRows:
                    if self.showoutput:
                        print(row)
                
                # print (nmeaRows)
                    
                    gpsData = row.split(",")

                   # self.showoutput=False
                    
                    #if self.showoutput:
                    #    print(str(self.i))
                    #    print(gpsData)
                            
                    if self.showoutput:
                        print(gpsData[0])
                    
                    if len(gpsData)<7:
                        continue        
                    if gpsData[0]==TIME_SENTENCE:
                        gpsTime=gpsData
                        self.current_epoch=1
                        if self.showoutput:
                            print("TIME==="+self.current_epoch)
                    #if gpsData[0]==ALT_SENTENCE:
                    #    #$GPGGA
                    #    gpsAlt = gpsData[9]
                    #    gpsUnit = gpsData[10]
                    #    self.altitude = gpsAlt+gpsUnit
                    #    if self.showoutput:
                    #        print("ALTITUDE==="+self.altitude)
                    if gpsData[0]==SENTENCE or gpsData[0]==ALTERNATE_SENTENCE:
                        if gpsData[2]=='A':
                            if self.showoutput:
                                print(gpsData)
                            gpsTime = gpsData[1]
                            #print(gpsTime)
                            gpsLat=float(gpsData[3])
                            gpsN=gpsData[4] 
                            gpsLon=float(gpsData[5])
                            gpsE=gpsData[6]

                            if (gpsN==SOUTH):
                                gpsLat = -gpsLat

                            latDeg = int(gpsLat/100)
                            latMin = gpsLat-latDeg*100
                            lat=latDeg+latMin/60

                            if (gpsE==WEST):
                                gpsLon = -gpsLon

                            lonDeg = int(gpsLon/100)
                            lonMin = gpsLon-lonDeg*100
                            lon=lonDeg+lonMin/60

                            self.mhGrid = mh.toMaiden(lat,lon,precision=self.location_precision)
                            self.current_lat = lat
                            self.current_lon = lon
                                
                            if self.showoutput:
                                print("Maidenhead Grid "+self.mhGrid)
                            
        except (KeyboardInterrupt, SystemExit):
            self.setReadGPS(False)
            self.join()
            print("Done.\nClosing GPS Listener.")

        finally:
            self.sock.close()
            
if __name__ == "__main__":
    serverip = '192.168.1.105'
    serverport=10110
    #serverport=8080
    precision=6
    
    gps=netWorkGPS(serverip, serverport,precision, True)
    gps.start()
                
      
    
