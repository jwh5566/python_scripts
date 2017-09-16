# -*- coding: utf-8 -*-
#!/usr/bin/env python
# This program is optimized for Python 2.7
"""
聊天室
"""

import select
import socket
import sys
import signal
import cPickle
import struct
import argparse

SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'


# 工具方法
def send(channel, *args):
    buffer = cPickle.dumps(args)  # 序列化 用于传输给客户端
    value = socket.htonl(len(buffer))  # 转换成网络字节序，用于网络传输
    size = struct.pack("L", value)  # 按照给定的格式(fmt)，把数据封装成字符串(实际上是类似于c结构体的字节流)
    channel.send(size)
    channel.send(buffer)


def receive(channel):
    size = struct.calcsize("L")  # 计算无符号长整型占用多少字节内存
    size = channel.recv(size)
    try:
        size = socket.ntohl(struct.unpack("L", size)[0])    # 解包，并且转换成主机字节序，
                                                            # unpack要求size的长度必须要等于calcsize的大小，所以上面recv(fmt的大小)
                                                            # unpack的返回值是元祖，即使只有一个值
    except struct.error, e:
        return ''
    buf = ""
    while len(buf) < size:
        buf = channel.recv(size - len(buf))
    return cPickle.loads(buf)[0]    # 这里只返回client发送的第一个对象


class ChatServer(object):
    def __init__(self, port, backlog=5):
        self.clients = 0  # 客户端数量
        self.clientmap = {}   # 客户端的映射关系
        self.outputs = []     # fork 的sockets
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((SERVER_HOST, port))
        print "服务器监听在端口: %s" %port
        self.server.listen(backlog)   # 最大连接队列数

        # 捕获键盘中断信号
        signal.signal(signal.SIGINT, self.sighandler)  # 类型 和 动作

    def sighandler(self, signum, frame):
        """清除客户端输出"""
        # 关闭服务器
        print "关闭服务器..."
        # 关闭存在的客户端sockets
        for output in self.outputs:
            output.close()
        self.server.close()

    def get_client_name(self, client):   # 这里的client表示与client发送数据的socket对象
        info = self.clientmap[client]
        host, name = info[0][0], info[1]
        return '@'.join((name, host))

    def run(self):
        inputs = [self.server, sys.stdin]
        self.outputs = []
        running = True
        while True:
            try:
                readable, writeable, exceptional = select.select(inputs, self.outputs, [])
            except select.error, e:
                break
            for sock in readable:
                if sock == self.server:
                    # 服务端socket
                    client, address = self.server.accept()
                    print "聊天室: 获取连接 %d 来自 %s" %(client.fileno(), address)  # fileno socket的文件描述符
                    # 获取客户端发送的名字
                    cname = receive(client).split('NAME: ')[1]
                    # 计算客户端数并且返回给客户端
                    self.clients += 1
                    send(client, 'CLIENT: ' + str(address[0]))
                    inputs.append(client)
                    self.clientmap[client] = (address, cname)
                    # 发送信息给其他客户端
                    msg = "\n(新客户端连接: (%d) from %s)" %(self.clients, self.get_client_name(client))
                    for output in self.outputs:
                        send(output, msg)
                    self.outputs.append(client)
                elif sock == sys.stdin:
                    # 处理标准输入
                    junk = sys.stdin.readline()
                    running = False
                else:
                    # 处理其他sockets
                    try:
                        data = receive(sock)
                        if data:
                            msg = '\n#[' + self.get_client_name(sock) + ']>>' + data
                            for output in self.outputs:
                                if output != sock:
                                    send(output, msg)
                        else:
                            print "聊天室: %d 离开" %sock.fileno()
                            self.clients -= 1
                            sock.close()
                            inputs.remove(sock)
                            self.outputs.remove(sock)
                            # 发送客户端离开信息
                            msg = "\n(客户端离开: %s)" %self.get_client_name(sock)
                            for output in self.outputs:
                                send(output, msg)
                    except socket.error, e:
                        inputs.remove(sock)
                        self.outputs.remove(sock)
        self.server.close()


class ChatClient(object):
    def __init__(self, name, port, host=SERVER_HOST):
        self.name = name
        self.connected = False
        self.host = host
        self.port = port
        self.prompt = '[' + '@'.join((name, socket.gethostname().split('.')[0])) + ']> '
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print "连接到聊天室@ port %d" % self.port
            self.connected = True
            # 发送自己的名字
            send(self.sock, 'NAME: ' + self.name)
            data = receive(self.sock)
            addr = data.split('CLIENT: ')[1]
            self.prompt = '[' + '@'.join((self.name, addr)) + ']> '
        except socket.error, e:
            print "连接聊天室失败 @ port %d" %self.port
            sys.exit(1)

    def run(self):
        while self.connected:
            try:
                sys.stdout.write(self.prompt)
                sys.stdout.flush()
                # 等待stdin输入
                readable, writeable, exceptional = select.select(
                    [0, self.sock],
                    [],
                    []
                )
                for sock in readable:
                    if sock == 0:
                        data = sys.stdin.readline().strip()
                        if data: send(self.sock, data)
                    elif sock == self.sock:
                        data = receive(self.sock)
                        if not data:
                            print "客户端关闭"
                            self.connected = False
                            break
                        else:
                            sys.stdout.write(data + '\n')
                            sys.stdout.flush()
            except KeyboardInterrupt:
                print " 客户端中断 "
                self.sock.close()
                break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Socket server with select library")
    parser.add_argument('--name', action="store", dest="name", required=True)
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    name = given_args.name
    if name == CHAT_SERVER_NAME:
        server = ChatServer(port)
        server.run()
    else:
        client = ChatClient(name=name, port=port)
        client.run()
