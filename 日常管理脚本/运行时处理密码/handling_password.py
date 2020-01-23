# -*- coding: utf-8 -*-
# @Time : 2020/1/23 14:21
# @Author : jwh5566
# @Email : jwh5566@aliyun.com
# @File : handling_password.py

import paramiko

ip_address = "192.168.18.82"
username = "admin"
password = "admin123"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()
ssh_client.connect(hostname=ip_address,
                   username=username,
                   password=password
                   )
print("成功连接服务器", ip_address)
ssh_client.invoke_shell()
remote_connection = ssh_client.exec_command('cd /tmp; mkdir test123\n')
remote_connection = ssh_client.exec_command('mkdir test_folder\n')
# print(remote_connection.read())
ssh_client.close()
