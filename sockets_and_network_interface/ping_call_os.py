# -*- coding: utf-8 -*-
#!/usr/bin/env python
# This program is optimized for Python 2.7

import subprocess
import shlex

command_line = "ping -c 1 www.baidu.com"
args = shlex.split(command_line)
try:
    subprocess.check_call(args, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    print "能ping通百度!"
except subprocess.CalledProcessError:
    print "不能ping通百度."