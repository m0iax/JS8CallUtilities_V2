import configparser
import os
import sys
import time
from datetime import datetime

gpslogfilename="gps.log"

# determine if application is a script file or standalone exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

config_path = os.path.join(application_path, gpslogfilename)

class Log():
#    def createLogFIle(self, logfileName):
#         if not os.path.isfile(logfileName):
#            #create the file
#            with open(logfileName, 'w') as file:
#                file.write("")
#                file.close()
    
#    def openlogfile(self, logFileName):
#        if not os.path.isfile(logFileName):
#             self.createLogFIle(logFileName)
        
#        with open(logFileName, 'w') as file:
#                config.write(configfile)
#                configfile.close()
    
    def writeToFile(self, fileName, logmessage):
        with open(fileName, 'a+') as file:
                file.write(logmessage+"\n")
                file.close()
                
        
    def writeToGPSLog(self, text):
        
            # datetime object containing current date and time
            now = datetime.now()
            
            print("now =", now)

            # dd/mm/YY H:M:S
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
           # datetime = time.datetime()
            text = dt_string+": "+text
            self.writeToFile(gpslogfilename,text)
        
            
    


    