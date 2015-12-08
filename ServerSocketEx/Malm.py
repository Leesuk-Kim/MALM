"""
The MIT License (MIT)

Copyright (c) 2015 Leesuk-Kim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import ThingsManager


class Malm:
    def __init__(self, host, port, sendqueue: list):
        self.name = 'powerstrip'
        self.sendqueue = sendqueue
        self.tm = ThingsManager

    def announce(self, msg_user):
        """
        서버에서 받은 메시지를 thing들에게 보냄
        """
        self.tm.announce(msg_user)

    def synthesize(self, msg_thing):
        """
        thing에게서 받은 받은 메시지를 사용자에게 보냄
        sendqueue에 메시지를 저장하면 네트워크쪽에서 알아서 보냄
        """
        self.sendqueue.append(msg_thing)
