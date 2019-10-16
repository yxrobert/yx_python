#! /usr/bin/env python
# -*- coding: UTF-8 -*-


import paramiko


class yXSSH():
    def __init__(self):
        #创建一个ssh的客户端，用来连接服务器
        self.ssh = paramiko.SSHClient()
        #创建一个ssh的白名单
        know_host = paramiko.AutoAddPolicy()
        #加载创建的白名单
        self.ssh.set_missing_host_key_policy(know_host)
 
        #连接服务器
        self.ssh.connect(
            hostname = "39.96.244.26",
            port = 14036,
            username = "game",
            password = "",
            key_filename = "loc_20190727_key"
        )
  

    def do_respons(self, message, userid):
        stdin,stdout,stderr = ssh.exec_command("pwd")
        print(stdout.read().decode())
        return stdout.read().decode()

ssh = yXSSH()


def main():
    ssh.do_respons()

if __name__ == "__main__":
    main()