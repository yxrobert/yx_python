#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import os

def get_onlines():
	cmd = "ssh -p 36000 root@152.136.22.243 tail -n 1 /data/home/user00/log/chatlog/Info.2020-04-* | grep \"client connected\""
	f = os.popen(cmd)
	return f.readlines()[-1]

def get_charge():
	cmd = "ssh -p 14036 game@39.96.244.26 cat /home/game/input/log/server_1003/loc/Info.2019-10-* | grep \"pay success\" | wc -l"
	f = os.popen(cmd)
	return f.readlines()[-1]

def main():
	s = get_onlines()
	print(s)
	s = get_charge()
	print(s)



if __name__ == "__main__":
	main()