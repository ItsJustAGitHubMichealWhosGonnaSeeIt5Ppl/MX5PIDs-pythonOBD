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




TPMS1Pr = OBDCommand("TPMS",         # name
               "Engine RPM",   # description
               b"22c901",        # command
               0,            # number of return bytes to expect
               TPMS,            # decoding function
               ECU.ALL,     
               True,
               b'720')             # (optional) allow a "01" to be added for speed

MX5_BRK_SW = OBDCommand("MX5 Brake Switch",# - Needs testing
               "Check if Brake is pressed/engaged",   # description
               b"221101",        # command
               4,            # number of return bytes to expect
               raw,            # decoding function
               ECU.ALL,     
               True,       
               b'7e0')        # 7E0 is default  

MX5_NEUTRAL_SW = OBDCommand("Park/Neutral Position Switch",# - Needs testing
    "On/Off Park/Neutral detection",  # description
    b"22a211",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        
    True,           
    b'7e0')         

MX5_TIRE_TEMP = OBDCommand("Tire Temperture sensor",# - Needs testing
    "Tire temp reading for all 4 wheels",  # description
    b"22c902",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        
    True,           
    b'720')         

MX5_CC_V = OBDCommand("Cruise Control Voltage",# - Needs testing
    "Cruise Control voltage reading",  # description
    b"22a216",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        
    True,           
    b'7e0')         

MX5_AC_REFRG_SW = OBDCommand("AC Refrigerant Switch ",# - Needs testing
    "On/Off A/C Refrigerant Pressure Switch",  # description
    b"221104",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        
    True,           
    b'7e0')         

MX5_AC_RELAY = OBDCommand("AC Relay",# - Needs testing
    "On/Off A/C Relay",  # description
    b"221101",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        
    True,           
    b'7e0')         

MX_5_ACCL_PDL = OBDCommand("Full range accelerator pedal",# - Needs testing
    "Accel Pedal Position (full range)",  # description
    b"221340",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        
    True,           
    b'7e0')         

MX5_BRKCLTCH_PRES_SW = OBDCommand("Brake Pressure Applied Switch + Clutch position switch",# - Needs testing
    "On/Off Brake Pressure Applied + Clutch Pedal Position Switch. Clutch is Byte 0, Brake is byte 1",  # description
    b"22a211",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        
    True,           
    b'7e0') 

MX5_INGEAR_SW = OBDCommand("In gear switch",# - Needs testing
    "On/Off In gear switch",  # description
    b"221101",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        # (optional) ECU filter
    True,           # (optional) allow a "01" to be added for speed 
    b'7e0')         # Header if not 7E0, no 0x

MX5_TIRE_RPM = OBDCommand("Tire Revolutions Per Mile(I have no idea)",# - Needs testing
    "Revolutions Per Mile, alleged math ((A*256)+B)",  # description
    b"2216f0",        # Mode+PID, no 0x
    5,              # number of return bytes to expect and grab
    raw,            # decoder function
    ECU.ALL,        # (optional) ECU filter
    True,           # (optional) allow a "01" to be added for speed 
    b'7e0')         # Header if not 7E0, no 0x