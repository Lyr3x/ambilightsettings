import colorsys
import sys
import socket

logger=None

class Logger:
  logfile=None
  def __init__(self,activateLogging,path):
    if(activateLogging):
      self.logfile = file(path, "wb")

  def writeLine(self,msg):
    if(self.logfile!=None):
      self.logfile.write(str(msg))
      self.logfile.flush()


class boblightMilightConnector:
  def __init__(self):
    self.readInputStream()

  def readInputStream(self):
    milight=milightController("192.168.1.3",8899)
    while True:
      input = sys.stdin.readline()
      logger.writeLine("Input: "+input)
      inputData=input.split(' ')
      if(len(inputData)>3):
        r = float(inputData[0])
        g = float(inputData[1])
        b = float(inputData[2])
        milight.setRGB(r,g,b)


class milightController:
  ip=None
  port=None
  sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
  def __init__(self,IP,Port):
    self.ip=IP
    self.port=Port
  def setRGB(self,r,g,b):
    h, s, v = colorsys.rgb_to_hsv(float(r), float(g), float(b))
    logger.writeLine("H: "+str(h)+" S: "+str(s)+" v: "+str(v))
    if(s<0.02):
      MESSAGE1 = "\xC2\x00\x55"
      if(h>0.3333):
        htmp=h-0.3333
        logger.writeLine("Vk1: "+str(htmp))
        vtmp=htmp/0.6666
        logger.writeLine("Vk2: "+str(vtmp))
        vtmp=(2*vtmp)
        logger.writeLine("Vk3: "+str(vtmp))
        v=v/vtmp
        logger.writeLine("Vk4: "+str(v))
    else:
      #Korrektur Gelb
      if (h < 0.33333):
        h= h *0.5
      #Korrektur Cyan
      if (h > 0.33333 and h < 0.5):
        h= h*0.9
      if(h>0.3333):
        htmp=h-0.3333
        logger.writeLine("Vk1: "+str(htmp))
        vtmp=htmp/0.6666
        logger.writeLine("Vk2: "+str(vtmp))
        vtmp=(2*vtmp)
        logger.writeLine("Vk3: "+str(vtmp))
        v=v/vtmp
        logger.writeLine("Vk4: "+str(v))
      h = int((h) * 256)
      #Korrektur Farbverschiebung
      h=h+85
      if(h>256):
        h=256-(h%256)
      else:
        h=abs(h-256)
      h=int(h)
      MESSAGE1 = "\x40" + chr(h) + "\x55"
    if (v>=0.75):
      v=0.75
    v=v*25
    v=int(round(v))
    v=v+2
    v=min(27,v)
    v = max(2,v)
    MESSAGE2 = "\x4E" + chr(v) + "\x55"
    logger.writeLine("H2: "+str(h)+" S2: "+str(s)+" v2: "+str(v))
    self.sock.sendto(MESSAGE1, (self.ip, self.port))
    self.sock.sendto(MESSAGE2, (self.ip, self.port))
    
logger=Logger(False,"/storage/milight.log")
boblightMilightConnector(