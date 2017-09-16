# -*- coding: utf-8 -*-
#!/usr/bin/env python
# This program is optimized for Python 2.7

import socket
import select
import argparse

SERVER_HOST = 'localhost'
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
SERVER_RESPONSE = b"""HTTP/1.1 200 OK\r\nDate: Mon, 1 Apr 2017
01:01:01 GMT\r\nContent-Type: text/plain\r\nContent-Length: 25\r\n\r\n
Hello from Epoll Server!"""


class EpollServer(object):
    def __init__(self, host=SERVER_HOST, port=0):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen(1)
        self.sock.setblocking(0)  # 非阻塞模式
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        print "启动Epoll服务器"
        self.epoll = select.epoll()
        self.epoll.register(self.sock.fileno(), select.EPOLLIN)

    def run(self):
        """执行epoll服务器操作"""
        try:
            connections = {}; requests = {}; responses = {}
            while True:
                events = self.epoll.poll(1)
                for fileno, event in events:
                    if fileno == self.sock.fileno():
                        connection, address = self.sock.accept()
                        connection.setblocking(0)
                        self.epoll.register(connection.fileno(), select.EPOLLIN)
                        connections[connection.fileno()] = connection
                        requests[connection.fileno()] = b''
                        responses[connection.fileno()] = SERVER_RESPONSE
                    elif event & select.EPOLLIN:
                        requests[fileno] += connections[fileno].recv(1024)
                        if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                            self.epoll.modify(fileno, select.EPOLLOUT)
                            print '-'*40 + '\n' + requests[fileno].decode()[:-2]
                    elif event & select.EPOLLOUT:
                        byteswritten = connections[fileno].send(responses[fileno])
                        responses[fileno] = responses[fileno][byteswritten:]
                        if len(responses[fileno]) == 0:
                            self.epoll.modify(fileno, 0)
                            connections[fileno].shutdown(socket.SHUT_RDWR)
                    elif event & select.EPOLLHUP:
                        self.epoll.unregister(fileno)
                        connections[fileno].close()
                        del connections[fileno]
        finally:
            self.epoll.unregister(self.sock.fileno())
            self.epoll.close()
            self.sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Socket Server emaple with epoll")
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    server = EpollServer(host=SERVER_HOST, port=port)
    server.run()