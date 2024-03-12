from obd import OBDCommand, Unit
from obd.protocols import ECU
from MX5NC2Decoders import *

#MX5 NC extra PIDs
# 7E0 and 7e0 might be different
# Steering wheel (ABS thing) is 760, not 720


#Template
OBJECT_NAME = OBDCommand("Nice Name",# - Needs testing
    "Description",  # description
    b"0000",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        # (optional) ECU filter
    True,           # (optional) allow a "01" to be added for speed 
    b'7e0')         # Header if not 7E0, no 0x




TPMS1Pr = OBDCommand("TPMS",         # name
               "Engine RPM",   # description
               b"22c901",        # command
               0,            # number of return bytes to expect
               TPMS,            # decoding function
               ECU.ALL,     # (optional) ECU filter
               True,
               b'720')             # (optional) allow a "01" to be added for speed

MX5_BRK_SW = OBDCommand("MX5 Brake Switch",# - Needs testing
               "Check if Brake is pressed/engaged",   # description
               b"221101",        # command
               4,            # number of return bytes to expect
               raw,            # decoding function
               ECU.ALL,     # (optional) ECU filter
               True,       # (optional) allow a "01" to be added for speed 
               b'7e0')        # 7E0 is default  

MX5_NEUTRAL_SW = OBDCommand("Park/Neutral Position Switch",# - Needs testing
    "On/Off Park/Neutral detection",  # description
    b"22a211",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        # (optional) ECU filter
    True,           # (optional) allow a "01" to be added for speed 
    b'7e0')         # Header if not 7E0, no 0x

MX5_TIRE_TEMP = OBDCommand("Tire Temperture sensor",# - Needs testing
    "Tire temp reading",  # description
    b"22c902",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        # (optional) ECU filter
    True,           # (optional) allow a "01" to be added for speed 
    b'720')         # Header if not 7E0, no 0x

MX5_CRUISE_CONTROL = OBDCommand("Cruise Control Voltage",# - Needs testing
    "Cruise Control voltage reading",  # description
    b"22a216",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        # (optional) ECU filter
    True,           # (optional) allow a "01" to be added for speed 
    b'7e0')         # Header if not 7E0, no 0x