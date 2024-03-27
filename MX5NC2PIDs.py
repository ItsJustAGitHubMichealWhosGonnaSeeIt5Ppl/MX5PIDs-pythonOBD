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
    4,# number of return bytes to expect
    OneZero,# decoding function
    ECU.ALL,     
    True,       
    b'7e0')        # 7E0 is default   

MX5_NEUTRAL_SW = OBDCommand("Park/Neutral Position Switch",# - Works
    "On/Off Park/Neutral detection.  Returns 0 (False) if NOT in neutral, else 4",  # description
    b"22a211",        # Mode+PID, no 0x
    4,
    OneZero,
    ECU.ALL,
    True,
    b'7e0')

MX5_WHL_ANG = OBDCommand("MX5 Steering Wheel Position",# - Works
    "Check if Brake is pressed",   # description
    b"223201",# command (no 0x needed)
    5,# number of return bytes to expect
    raw,# decoding function
    ECU.ALL,# (optional) ECU filter
    True,# (optional) allow a "01" to be added for speed 
    b'720')# 7E0 is default, must be in byte format with b''

MX_5_ACCL_PDL = OBDCommand("Full range accelerator pedal",# - Works
    "Accel Pedal Position (full range)",  # description
    b"221340", 
    5,
    acclPercent,
    ECU.ALL,
    True,
    b'7e0')

MX5_BRKCLTCH_PRES_SW = OBDCommand("Brake Pressure Applied Switch + Clutch position switch",# - Works 
    """ On/Off Brake Pressure Applied + Clutch Pedal Position Switch. 
    0 no pedal, 
    1 clutch, 
    2 brake, 
    3 brake+clutch """,  # description
    b"22a211",
    5,
    brakeClutch,
    ECU.ALL,
    True,
    b'7e0')

MX5_INGEAR_SW = OBDCommand("In gear switch",
    "On/Off In gear switch", 
    b"221101",
    4,
    OneZero,
    ECU.ALL,
    True,
    b'7e0')

MX5_AC_REFRG_SW = OBDCommand("AC Refrigerant Switch ",
    "On/Off A/C Refrigerant Pressure Switch",
    b"221104",# Mode+PID, no 0x
    5,
    OneZero,
    ECU.ALL,
    True,
    b'7e0')

MX5_AC_RELAY = OBDCommand("AC Relay",
    "On/Off A/C Relay",
    b"221101",
    5,
    OneZero,
    ECU.ALL,
    True,
    b'7e0')
MX5_CC_V = OBDCommand("Cruise Control Voltage (resistance)",
    "Cruise Control voltage resistance reading.  Can be used to view button presses",
    b"22a216",
    5,              
    raw,            
    ECU.ALL,        
    True,           
    b'7e0')        