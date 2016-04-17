"""
Xbee와 관련된 model을 정의합니다.
"""
from controller import *
from xbee import XBee
import serial


class XbeeAttender(XBee):
    """
    특정 Xbee device에게 보낼 수 있는 AT command를 생성합니다.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def factory(port: str, bandwidth: int):
        """

        :param port:
        :param bandwidth:
        :return:
        """
        xa = XbeeAttender(serial.Serial(port, bandwidth))
        return xa
    pass


class MALM:
    """
    MALM: peasant를 관리하는 모듈. 이 모듈은 지그비를 두개나 처먹는다.
    """
    def __init__(self, xb1: XBee):
        self._peasants = []
        self._ack_buf = []  # acknownledge buffer
        self._xb_main = xb1
        # self._xb_sub  # sub XBee
    pass


class XbeeLocal:
    def __init__(self, xbee: XBee):
        self._xbee = xbee

    def at(self, cmd, param):
        pass
    pass


class XbeeRemote:
    """
    communicates xbee who communicates with Coordinator
    """
    def __init__(self, parent: XBee, ni, sh, sl, dh, dl):
        self._ni = ni
        self._serial = HighLowAddr(sh, sl)
        self._destination = HighLowAddr(dh, dl)
        self._parent = parent
        pass

    def at(self, cmd, param):
        """
        send at commen to remote xbee
        :param cmd:
        :param param:
        :return:
        """
        self._parent.remote_at(
            dest_addr=b'\x56\x78',
            command=format(cmd, 'binary'),
            parameter=format(param, 'binary'))

    @staticmethod
    def factory(xb: XBee):
        rmt = XbeeRemote(xb.remote_at())

    pass
