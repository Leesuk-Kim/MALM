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
    def NI(self, **kwargs):
        """
        Node Identifier
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def IC(self, **kwargs):
        """
        IO Digital Change Detection
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def P0(self, **kwargs):
        """
        PWM0 Configuration
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def P1(self, **kwargs):
        """
        DIO11 Configuration
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def P2(self, **kwargs):
        """
        DIO12 Configuration
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def P3(self, **kwargs):
        """
        DIO13 Configuration
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def D0(self, **kwargs):
        """
        AD0/DIO0 Configuration
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def D1(self, **kwargs):
        """
        AD1/DIO1 Configuration
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def D2(self, **kwargs):
        """
        AD2/DIO2 Configuration
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def D3(self, **kwargs):
        """
        AD3/DIO3 Configuration
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def D4(self, **kwargs):
        """
        DIO4 Configuration
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def D5(self, **kwargs):
        """
        DIO5 Configuration
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def D8(self, **kwargs):
        """
        DIO8 Configuration
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def PR(self, **kwargs):
        """
        Pull-up Resistor.
        :param kwargs:
        :return:
        """
        raise NotImplementedError
    pass


class ZigbeeLocal:
    def __init__(self, xbee: ZigBee):
        self._zigbee = xbee
    pass


class ZigbeeRemote(ZigbeeBase):
    """
    communicates xbee who communicates with Coordinator
    """

    def __init__(self, ni, sh, sl, dh, dl):
        self._ni = ni
        self._serial = HighLowAddr(sh, sl)
        self._destination = HighLowAddr(dh, dl)
        pass

    def P1(self, zb: ZigBee, cmd, param):
        pass

    def D8(self, zb: ZigBee, cmd, param):
        pass

    def PR(self, zb: ZigBee, cmd, param):
        pass

    def P3(self, zb: ZigBee, cmd, param):
        pass

    def P2(self, zb: ZigBee, cmd, param):
        pass

    def NI(self, zb: ZigBee, cmd, param):
        zb.remote_at(
            dest_addr=byteUTF8(self._serial.addr),
            command=b'NI')
        pass

    def D3(self, zb: ZigBee, cmd, param):
        pass

    def D0(self, zb: ZigBee, cmd, param):
        pass

    def D2(self, zb: ZigBee, cmd, param):
        pass

    def D5(self, zb: ZigBee, cmd, param):
        pass

    def P0(self, zb: ZigBee, cmd, param):
        pass

    def IC(self, zb: ZigBee, cmd, param):
        pass

    def D1(self, zb: ZigBee, cmd, param):
        pass

    def D4(self, zb: ZigBee, cmd, param):
        zb.remote_at(
            dest_addr=byteUTF8(self._serial.addr),
            command=b'D4',
            parameter=byteUTF8(param))
        pass