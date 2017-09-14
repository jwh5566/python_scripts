# -*- coding: utf-8 -*-
#!/usr/bin/env python
# This program is optimized for Python 2.7.\

import ntplib
from time import ctime # 用来打印response

def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print ctime(response.tx_time)

if __name__ == '__main__':
    print_time()