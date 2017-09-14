# -*- coding: utf-8 -*-
#!/usr/bin/env python
# This program is optimized for Python 2.7

import socket
import sys
import argparse

host = 'localhost'

def echo_client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print "connect server %s port %s" % server_address
    sock.connect(server_address)

    # 发送数据
    try:
        message = "This is a test message"
        print "sending %s" % message
        sock.sendall(message)
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)  # buffer size
            amount_received += len(data)
            print "received: %s" % data
    except socket.error, e:
        print "Socket error: %s" % str(e)
    except Exception, e:
        print "other exception: %s" % str(e)
    finally:
        print "closed connection"
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket server example')
    parser.add_argument('--port', action="store", dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)


