#! /usr/bin/python

# Import and init an XBee device
from model import *
from xbee import ZigBee



if __name__ == '__main__':
    srlc = serial.Serial('COM7', 9600)
    xbc = ZigBee(srlc)
    srle = serial.Serial('COM5', 9600)
    xbe = XBee(srle)

    xbc.at(command=b'NI')

    resc = xbc.wait_read_frame()
    xbc.remote_at(
        dest_addr=b'\x56\x78',
        command=b'D2',
        parameter=b'\x04')

    xbc.remote_at(
        dest_addr=b'\x56\x78',
        command=b'WR')

    # Use an XBee 802.15.4 device
    # To use with an XBee ZigBee device, replace with:
    #xbee = ZigBee(ser)
    # resc = xbc.wait_read_frame()

    # Set remote DIO pin 2 to low (mode 4)
    xbee.remote_at(
        dest_addr=b'\x56\x78',
        command=b'D2',
        parameter=b'\x04')
    resc = xbc.wait_read_frame()

    xbee.remote_at(
        dest_addr=b'\x56\x78',
        command=b'WR')