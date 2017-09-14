# -*- coding: utf-8 -*-
#!/usr/bin/env python
# This program is optimized for Python 2.7

import os
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0  # 告诉内核动态选择端口
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'


class ForkedClient():
    """客户端用来测试forking 服务器"""
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def run(self):
        #  发送数据到服务器
        current_process_id = os.getpid()
        print "PID %s 发送消息到服务器 : '%s'" %(current_process_id, ECHO_MSG)
        send_data_length = self.sock.send(ECHO_MSG)
        print "发送了: %d 个字符..." %send_data_length
        #  显示服务器响应
        response = self.sock.recv(BUF_SIZE)
        print "PID %s 接受了: %s" %(current_process_id, response[5:])

    def shutdown(self):
        """清除连接"""
        self.sock.close()


class ForkServerRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # 发送消息给客户端
        data = self.request.recv(BUF_SIZE)
        current_process_id = os.getpid()
        response = '%s: %s' %(current_process_id, data)
        print "服务器发送响应 [current_process_id: data] = [%s]" %response
        self.request.send(response)
        return


class ForkingServer(SocketServer.ForkingMixIn,
                    SocketServer.TCPServer,):
    pass


def main():
    # 运行服务器
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkServerRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    print "服务器循环运行PID： %s" %os.getpid()

    # 运行客户端
    client1 = ForkedClient(ip, port)
    client1.run()

    client2 = ForkedClient(ip, port)
    client2.run()

    # 清除
    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    server.socket.close()

if __name__ == '__main__':
    main()