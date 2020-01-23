# -*- coding: utf-8 -*-
#!/usr/bin/env python
# This program is optimized for Python 2.7

import argparse
import os
import select
import socket
import struct
import time

ICMP_ECHO_REQUEST = 8
DEFAULT_TIMEOUT = 2
DEFAULT_COUNT = 4

class Pinger(object):
    """ping a host, pythonic way"""
    def __init__(self, target_host, count=DEFAULT_COUNT,
                 timeout=DEFAULT_TIMEOUT):
        self.target_host = target_host
        self.count = count
        self.timeout = timeout

    def do_checksum(self, source_string):
        """验证packet完整性"""
        sum = 0
        max_count = (len(source_string)/2)*2
        count = 0
        while count < max_count:
            val = ord(source_string[count+1])*256 + ord(source_string[count])
            sum = sum + val
            sum = sum & 0xffffffff
            count = count + 2
            if max_count<len(source_string):
                sum = sum + ord(source_string[len(source_string)]-1)
                sum = sum & 0xffffffff
            sum = (sum >> 16) + (sum & 0xffff)
            sum = sum + (sum >> 16)
            answer = ~sum
            answer = answer & 0xffff
            answer = answer >> 8 | (answer << 8 & 0xff00)
            return answer

    def receive_pong(self, sock, ID, timeout):
        """
        receive ping from socket
        :param sock:
        :param ID:
        :param timeout:
        :return:
        """
        time_remaining = timeout
        while True:
            start_time = time.time()
            readable = select.select([sock], [], [], time_remaining)
            time_spent = (time.time() - start_time)
            if readable[0] == []:  # Timeout
                return
            time_received = time.time()
            recv_packet, addr = sock.recvfrom(1024)
            icmp_header = recv_packet[20:28]
            type, code, cheksum, packet_ID, sequence = \
            struct.unpack("bbHHh", icmp_header)
            if packet_ID == ID:
                bytes_In_double = struct.calcsize("d")
                time_spent = struct.unpack("d", recv_packet[20:28 + bytes_In_double])[0]
                return time_received - time_spent
            time_remaining = time_remaining - time_spent
            if time_remaining <= 0:
                return

    def send_ping(self, sock, ID):
        """
        send ping to target host
        :param sock:
        :param ID:
        :return:
        """
        target_addr = socket.gethostbyname(self.target_host)
        my_checksum = 0
        # Create a dummy header with a 0 checksum.
        header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
        bytes_In_double = struct.calcsize("d")
        data = (192 - bytes_In_double) * "Q"
        data = struct.pack("d", time.time()) + data
        my_checksum = self.do_checksum(header + data)
        header = struct.pack(
            "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1
        )
        packet = header + data
        sock.sendto(packet, (target_addr, 1))

    def ping_once(self):
        icmp = socket.getprotobyname("icmp")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        except socket.error, (errno, msg):
            if errno == 1:
                msg += "ICMP messages can only be sent from root user processes"
            raise socket.error(msg)
        except Exception, e:
            print "Exception: %s" %e
        my_ID = os.getpid() & 0xFFFF
        self.send_ping(sock, my_ID)
        delay = self.receive_pong(sock, my_ID, self.timeout)
        sock.close()
        return delay

    def ping(self):
            print "ping to %s..."% self.target_host
            try:
                delay = self.ping_once()
            except socket.gaierror, e:
                print "Ping failed. (socket error: %s)" %e[1]
                break
            if delay == None:
                print "Ping Failed. (timeout within %ssec)" %self.timeout
            else:
                delay = delay * 1000
                print "Get pong in %0.4fms" % delay

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Python ping")
    parser.add_argument('--target-host', action="store", dest='target_host',
                        required=True)
    given_args = parser.parse_args()
    target_host = given_args.target_host
    pinger = Pinger(target_host=target_host)
    pinger.ping()