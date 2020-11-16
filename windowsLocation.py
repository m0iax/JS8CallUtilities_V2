import threading
import subprocess as sp
import re
import time
import maidenhead as mh


class locationservices(threading.Thread):
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
        self.setLocationFromWindows()
        return self.mhGrid
    def setReadGPS(self, read):
        self.readGPS = read
    def setShowDebug(self, show):
        self.showOutput=show
    def setLocationFromWindows(self):
        wt = 5 # Wait time -- I purposefully make it wait before the shell command
        accuracy = 3 

        #while True:
        #time.sleep(wt)
        pshellcomm = ['powershell']
        pshellcomm.append('add-type -assemblyname system.device; '\
                              '$loc = new-object system.device.location.geocoordinatewatcher;'\
                              '$loc.start(); '\
                              'while(($loc.status -ne "Ready") -and ($loc.permission -ne "Denied")) '\
                              '{start-sleep -milliseconds 100}; '\
                              '$acc = %d; '\
                            'while($loc.position.location.horizontalaccuracy -gt $acc) '\
                            '{start-sleep -milliseconds 100; $acc = [math]::Round($acc*1.5)}; '\
                            '$loc.position.location.latitude; '\
                            '$loc.position.location.longitude; '\
                            '$loc.position.location.horizontalaccuracy; '\
                            '$loc.stop()' %(accuracy))

        p = sp.Popen(pshellcomm, stdin = sp.PIPE, stdout = sp.PIPE, stderr = sp.STDOUT, text=True)
        (out, err) = p.communicate()
        out = re.split('\n', out)

        lat = float(out[0])
        lon = float(out[1])
        radius = int(out[2])

        if self.showOutput:
            print(lat, lon, radius)

        self.current_lat=lat
        self.current_lon=lon
        self.mhGrid = mh.to_maiden(lat,lon,precision=self.location_precision)

        if self.showOutput:
            print(self.mhGrid) 

    def __init__(self, precision, showoutput):
        print("Init using windows location services")
        threading.Thread.__init__(self)
        
        if precision==None:
            precision=6
        self.location_precision=int(precision)
        self.current_ngr = None
        self.current_epoch = None
        self.current_lon = None
        self.current_lat = None
        self.altitude = None
        self.mhGrid = None
        self.status= ""
        self.mh_grid = None
        self.showOutput=showoutput
        self.getMaidenhead()


if __name__ == "__main__":

    locservice = locationservices(None,6)

