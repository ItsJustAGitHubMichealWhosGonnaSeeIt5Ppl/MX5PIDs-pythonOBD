from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int
from MX5NC2Decoders import *

#MX5 NC extra PIDs
# 7E0 and 7e0 might be different
# Steering wheel (ABS thing) is 760, not 720


TPMS1Pr = OBDCommand("TPMS",         # name
               "Engine RPM",   # description
               b"22c901",        # command
               0,            # number of return bytes to expect
               TPMS,            # decoding function
               ECU.ALL,     # (optional) ECU filter
               True,
               b'720')             # (optional) allow a "01" to be added for speed

MX5_BRK_SWC = OBDCommand("MX5 Brake Switch",# - Needs testing
               "Check if Brake is pressed",   # description
               b"221101",        # command
               4,            # number of return bytes to expect
               raw,            # decoding function
               ECU.ALL,     # (optional) ECU filter
               True,       # (optional) allow a "01" to be added for speed 
               b'7e0')        # 7E0 is default  

MX5_WHL_ANG = OBDCommand("MX5 Steering Wheel Position",# - Works
               "Check if Brake is pressed",   # description
               b"223201",        # command (no 0x needed)
               5,            # number of return bytes to expect
               raw,            # decoding function
               ECU.ALL,     # (optional) ECU filter
               True,       # (optional) allow a "01" to be added for speed 
               b'720')        # 7E0 is default, must be in byte format with b''
