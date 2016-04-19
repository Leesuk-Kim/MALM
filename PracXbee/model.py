"""
Xbee와 관련된 model을 정의합니다.
"""
from controller import *
from xbee import ZigBee
import serial


class ZigbeeCommander:
    """
    특정 Xbee device에게 보낼 수 있는 AT command를 생성합니다.
    """
    def __init__(self, zb: ZigBee):
        self._zigbee = zb

    @property
    def zigbee(self):
        return self._zigbee
    pass


class MALM:
    """
    MALM: peasant를 관리하는 모듈. 이 모듈은 지그비를 두개나 처먹는다.
    """
    def __init__(self, zb1: ZigBee):
        self._peasants = []
        self._ack_buf = []  # acknownledge buffer
        self._xb_main = zb1
        # self._xb_sub  # sub XBee
    pass


class ZigbeeBase:
    """
    ZogbeeRemote나 ZigbeeLocal의 모체가 되기 위한 supclass
    """
    def __init__(self, zb: ZigBee):
        self._ambassador = ZigbeeCommander(zb)

    def NI(self, **kwargs):
        """
        Node Identifier
        :param kwargs:
        :return:
        """
        raise NotImplementedError
    pass


class ZigbeeLocal:
    def __init__(self, xbee: ZigBee):
        self._zigbee = xbee
    pass


class ZigbeeRemote:
    """
    communicates xbee who communicates with Coordinator
    """
    def __init__(self, parent: ZigBee, ni, sh, sl, dh, dl):
        self._ni = ni
        self._serial = HighLowAddr(sh, sl)
        self._destination = HighLowAddr(dh, dl)
        self._parent = parent
        pass\

    @staticmethod
    def factory(xb: ZigBee):
        rmt = ZigbeeRemote(xb.remote_at())

    pass
