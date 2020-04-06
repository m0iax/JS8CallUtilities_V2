from sys import platform

def getOs():
    
   # os = "Unknown"
    
    if platform == "linux" or platform == "linux2":
        os="Linux"
    elif platform == "Darwin":
        os="MAC OSX"
    elif platform == "win32":
        os="Windows"
        
    return os


#if __name__ == '__main__':
#    print("This library is not intended to run stadnalone. Include in your project.")

   # print ("I am running on: "+getOs())