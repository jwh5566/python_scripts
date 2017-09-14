#!/usr/bin/env python
# This program is optimized for Python 2.7.

import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get size of the sock send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    # bufsize1 = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print "Buffer size [Before]:%d" %bufsize
    # print "Buffer size [Before]:%d" % bufsize1

    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SEND_BUF_SIZE
    )
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECV_BUF_SIZE
    )
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    # bufsize1 = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print "Buffer size [After]:%d" %bufsize
    # print "Buffer size [After]:%d" % bufsize1

if __name__ == '__main__':
    modify_buff_size()