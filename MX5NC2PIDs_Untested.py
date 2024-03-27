from obd import OBDCommand, Unit
from obd.protocols import ECU
from MX5NC2Decoders import *

## MX5 NC extra PIDs
# Source: https://forum.miata.net/vb/showthread.php?t=631418
# Seriously without that I'd be so fucking lost
# 7E0 and 7e0 might be different
# Steering wheel (ABS thing) is 760, not 720
# 

#Template
OBJECT_NAME = OBDCommand("Nice Name",# - Needs testing
    "Description",  # description
    b"0000",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        # (optional) ECU filter
    True,           # (optional) allow a "01" to be added for speed 
    b'7e0')         # Header if not 7E0, no 0x


MX5_TIRE_TEMP = OBDCommand("Tire Temperture sensor",# - Needs testing
    "Tire temp reading for all 4 wheels",  # description
    b"22c902",        # Mode+PID, no 0x
    5,              
    raw,            
    ECU.ALL,        
    True,           
    b'720')         
    
MX5_TIRE_RPM = OBDCommand("Tire Revolutions Per Mile(I have no idea)",# - Needs testing
    "Revolutions Per Mile, alleged math ((A*256)+B)",  # description
    b"2216f0",        # Mode+PID, no 0x
    5,              
    raw,            
    ECU.ALL,        
    True,           
    b'7e0')