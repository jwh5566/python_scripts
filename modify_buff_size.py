#!/usr/bin/env python
# This program is optimized for Python 2.7.

import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

# def modify_buff_size():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # get size of the sock send buffer
#     bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
#     print "Buffer "