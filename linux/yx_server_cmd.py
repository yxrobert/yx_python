#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import os

def get_onlines():
	cmd = "ssh -p 14036 game@39.96.244.26 tail -n 100 input/log/server_1003/chat/Info.2019-10-17_* | grep \"client connected\""
	f = os.popen(cmd)
	return f.readlines()[-1]


def main():
	s = get_onlines()
	print(s)



if __name__ == "__main__":
	main()