import itertools
import logging
import serial
import time
import platform
from serial.tools import list_ports
if platform.system() == 'Windows':
    import _winreg as winreg
else:
    import glob
    
log = logging.getLogger(__name__)
    
class Arduino(object):
  def getPort():
