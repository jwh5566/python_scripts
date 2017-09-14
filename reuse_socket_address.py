# -*- coding: utf-8 -*-
#!/usr/bin/env python
# This program is optimized for Python 2.7.

import socket
import sys

def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 获取修改前的SO_REUSEADDR状态
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "修改前的状态是: %s" %old_state
    # 打开重用选项
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "修改后的状态是: %s" %new_state

    local_port = 8282

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('', local_port))
    srv.listen(1)
    print "监听端口是: %s" %local_port
    while True:
        try:
            connetion, addr = srv.accept()
            print "客户端地址是 %s:%s" % (addr[0], addr[1])
        except KeyboardInterrupt:
            break
        except socket.error, msg:
            print '%s' %(msg,)

if __name__ == '__main__':
    reuse_socket_addr()