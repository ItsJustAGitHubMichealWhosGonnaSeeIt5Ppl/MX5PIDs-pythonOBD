from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int


#MX5 NC extra PIDs
# 7E0 and 7e0 might be different

def raw(messages):
    """ Not really a decoder """
    d = messages[0].data # only operate on a single message
    d = d[3:] # chop off mode and PID bytes
    v = bytes_to_int(d) # helper function for converting byte arrays to ints
    print(v)
    return d# construct a Pint Quantity
# Returns bytearray

def TPMS(messages): # Untested
    """ decoder for TMPS messages """
    fr = messages[0].data # only operate on a single message
    fl = messages[1].data
    rr = messages[2].data
    rl = messages[3].data
    d = d[3:] # chop off mode and PID bytes
    v = bytes_to_int(d) / 4.0  # helper function for converting byte arrays to ints
    return v * 0.199136814274 # construct a Pint Quantity

def acclPercent(messages):
    """ Not really a decoder """
    d = messages[0].data # only operate on a single message
    d = d[3:] # chop off mode and PID bytes
    v = bytes_to_int(d) / 652.80  # helper function for converting byte arrays to ints
    return v# construct a Pint Quantity

def brakeClutch(messages):
    """ 
    0 = no pedals pressed
    1 = clutch pressed
    2 = brake pressed
    3 = both pressed"""
    d = messages[0].data # only operate on a single message
    d = d[4:] # chop off mode and PID bytes
    v = bytes_to_int(d) # helper function for converting byte arrays to ints
    return v# construct a Pint Quantity

def steeringAngDecode(messages):
    """ Decode steering wheel pos """
    d = messages[0].data # only operate on a single message
    d = d[3:] # chop off mode and PID bytes
    v = (bytes_to_int(d) -23048) / 20 # In theory cleans up output
    return v 

def OneZero(messages):
    """ For True/False outputs """
    d = messages[0].data # only operate on a single message
    dTrim = d[3:] #Example of data b\x11\x01\x00 - This is unneeded > b\x11\x01\
    dInt = bytes_to_int(dTrim) 
    v = True if dInt is not 0 else False
    return v  # Return True/False