# -*- coding: utf-8 -*-
#!/usr/bin/env python
# This program is optimized for Python 2.7

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
    """a simple echo server"""
    # 创建一个 TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 打开端口重用
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定socket到端口
    server_address = (host, port)
    print "starting on %s port %s" % server_address
    sock.bind(server_address)

    # 监听客户端，backlog参数指定最大队列连接数
    sock.listen(backlog)
    while True:
        print "waiting client..."
        client, address = sock.accept()
        data = client.recv(data_payload)
        if data:
            print "Data: %s" %data
            client.send(data)
            print "send %s bytes to %s" % (data, address)
            # 结束连接
            client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket server example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)



