__author__ = 'lk'

from socket import *
from select import *
import sys
from time import ctime
from threading import Thread
from functools import wraps
import Malm as malm

# 호스트, 포트와 버퍼 사이즈를 지정
BUFSIZE = 1024
HOST = ''
PORT = 56789
ADDR = (HOST, PORT)
# 소켓 객체를 만들고..
serverket = socket(AF_INET, SOCK_STREAM)

# 서버 정보를 바인딩
serverket.bind(ADDR)  # bind returns noting

# 요청을 기다림(listen)
serverket.listen(10)
msglist = []
connection_list = [serverket]
print('==============================================')
print('채팅 서버를 시작합니다. %s 포트로 접속을 기다립니다.' % str(PORT))
print('==============================================')

# 무한 루프를 시작
while connection_list:
    try:
        print('[INFO] 요청을 기다립니다...', len(connection_list))

        # select 로 요청을 받고, 10초마다 블럭킹을 해제하도록 함
        read_socket, write_socket, error_socket = select(connection_list, [], [], 10)

        for sock in read_socket:
            # 새로운 접속
            if sock == serverket:
                clientSocket, addr_info = serverket.accept()
                connection_list.append(clientSocket)
                print('[INFO][%s] 클라이언트(%s)가 새롭게 연결 되었습니다.' % (ctime(), addr_info[0]))

                # 클라이언트로 응답을 돌려줌
                for socket_in_list in connection_list:
                    if socket_in_list != serverket and socket_in_list != sock:
                        try:
                            msg = '[%s] 새로운 방문자가 대화방에 들어왔습니다. 반가워요~ 짝짝짝!' % ctime()
                            socket_in_list.send(msg.encode())
                        except Exception as e:
                            socket_in_list.close()
                            connection_list.remove(socket_in_list)
            # 접속한 사용자(클라이언트)로부터 새로운 데이터 받음
            else:
                data = sock.recv(BUFSIZE)
                if data:
                    print('[INFO][%s] 클라이언트로부터 데이터를 전달 받았습니다.' % ctime())
                    for socket_in_list in connection_list:
                        if socket_in_list != serverket and socket_in_list != sock:
                            try:
                                msg = '[%s] %s' % (ctime(), data)
                                socket_in_list.send(msg.encode())
                                print('[INFO][%s] 클라이언트로 데이터를 전달합니다.' % ctime())
                            except Exception as e:
                                print(e)
                                socket_in_list.close()
                                connection_list.remove(socket_in_list)
                                continue
                else:
                    connection_list.remove(sock)
                    sock.close()
                    print('[INFO][%s] 사용자와의 연결이 끊어졌습니다.' % ctime())
    except error as e:
        # 부드럽게 종료하기
        serverket.close()
        sys.exit()
