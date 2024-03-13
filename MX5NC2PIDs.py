from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int
from MX5NC2Decoders import *

#MX5 NC extra PIDs
# 7E0 and 7e0 might be different
# Steering wheel (ABS thing) is 760, not 720


MX5_BRK_SW = OBDCommand("MX5 Brake Switch",# - Tested, returns 2 if brake is pressed at all.
               "On/Off Check if brake oedak is pressed/engaged",   # description
               b"221101",        # command
               4,            # number of return bytes to expect
               OneZero,            # decoding function
               ECU.ALL,     
               True,       
               b'7e0')        # 7E0 is default   

MX5_NEUTRAL_SW = OBDCommand("Park/Neutral Position Switch",# - Needs testing
    "On/Off Park/Neutral detection.  Returns 0 (False) if in gear, else 4",  # description
    b"22a211",        # Mode+PID, no 0x
    4,              
    OneZero,            
    ECU.ALL,        
    True,           
    b'7e0') 

MX5_WHL_ANG = OBDCommand("MX5 Steering Wheel Position",# - Works
               "Check if Brake is pressed",   # description
               b"223201",        # command (no 0x needed)
               5,            # number of return bytes to expect
               raw,            # decoding function
               ECU.ALL,     # (optional) ECU filter
               True,       # (optional) allow a "01" to be added for speed 
               b'720')        # 7E0 is default, must be in byte format with b''
