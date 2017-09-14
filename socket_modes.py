# -*- coding: utf-8 -*-
#!/usr/bin/env python
# This program is optimized for Python 2.7.
import socket

def socket_modes():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(("127.0.0.1", 0))

    socket_address = s.getsockname()
    print "运行在socket上的服务器: %s" %str(socket_address)
    while(1):
        s.listen(1)

if __name__ == '__main__':
    socket_modes()