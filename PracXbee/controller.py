"""
controller 파트
구성:
peasant
본체와 지그비로 통신하는 라우터/엔드 디바이스들과 편리하게 통신할 수 있도록 대행하는 객체
MALM: peasant를 관리하는 모듈. 이 모듈은 지그비를 두개나 처먹는다.
:author: Leesuk Kim
"""


class HighLowAddr:
    """
    주소의 high, low, 그리고 주소 자체를 관리합니다.
    """
    def __init__(self, high: str, low: str):
        self._high = high
        self._low = low

    @property
    def high(self):
        """
        :return: the upper 32 bits of the 64-bit address
        """
        return self._high

    @property
    def low(self):
        """
        :return: the lower 32 bits of the 64-bit address
        """
        return self._low

    @property
    def addr(self):
        """
        :return: the 64-bit address
        """
        return self._high + self._low


def byteUTF8(msg: str):
    """
    string to bytes with encoding of UTF-8.
    :param msg:
    :return:
    """
    return bytes(msg, encoding='utf-8')
