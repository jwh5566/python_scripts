# -*- coding: utf-8 -*-
#!/usr/bin/env python
# This program is optimized for Python 2.7

import os
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024


def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(BUF_SIZE)
        print "客户端接收: %s" %response
    finally:
        sock.close()


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(BUF_SIZE)
        current_thread = threading.current_thread()
        response = "%s: %s" %(current_thread.name, data)
        self.request.sendall(response)


class ThreadedTCPServer(SocketServer.ThreadingMixIn,
                        SocketServer.TCPServer):
    pass

if __name__ == '__main__':
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT),
                               ThreadedTCPRequestHandler)
    ip, port = server.server_address
    # 开启线程
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print "服务器循环运行线程： %s" %server_thread.name
    client(ip, port, "HEllo form client 1")
    client(ip, port, "Hello form client 2")
    client(ip, port, "Hello form client 3")
    server.shutdown()