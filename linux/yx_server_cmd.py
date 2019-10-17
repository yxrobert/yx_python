#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import os

def get_onlines():
	cmd = "ssh -p 14036 game@39.96.244.26 tail -n 100 input/log/server_1003/chat/Info.2019-10-* | grep \"client connected\""
	f = os.popen(cmd)
	return f.readlines()[-1]

def get_charge():
	cmd = "ssh -p 14036 game@39.96.244.26 cat input/log/server_1003/loc/Info.2019-10-* | grep \"pay success\" | wc -l"
	f = os.popen(cmd)
	return f.readlines()[-1]

def main():
	s = get_onlines()
	print(s)



if __name__ == "__main__":
	main()