__author__ = 'lk'


from socket import *
from select import *
import sys
from time import ctime
from threading import Thread
from functools import wraps


# 호스트, 포트와 버퍼 사이즈를 지정BUFSIZE = 1024
BUFSIZE = 1024
ADDR = ('', 12345)


class Error(error):
    pass


class BaseMalmServer(Thread):
    def __init__(self, host, port):
        super().__init__()
        self.me = socket(AF_INET, SOCK_STREAM)
        self.me.bind((host, port))
        self.messages = []
        self.backlog = 5
        self.connlist = []
        self.name = 'powerstrip'

    def synthesize(self):
        pass

    def run(self):
        critical = False

        while not critical:

            pass
        pass

    def open(self):
        self.me.listen(self.backlog)
        pass

    def close(self):
        self.me.close()

    def __del__(self):
        self.close()
