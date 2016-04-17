#! /usr/bin/python

# Import and init an XBee device
from model import *



if __name__ == '__main__':
    ser = serial.Serial('COM7', 9600)
    xa = XbeeAttender(ser)

    # Use an XBee 802.15.4 device
    # To use with an XBee ZigBee device, replace with:
    #xbee = ZigBee(ser)
    xbee = XBee(ser)

    # Set remote DIO pin 2 to low (mode 4)
    xbee.remote_at(
        dest_addr=b'\x56\x78',
        command=b'D2',
        parameter=b'\x04')

    xbee.remote_at(
        dest_addr=b'\x56\x78',
        command=b'WR')