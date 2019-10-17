#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import commands

def get_onlines():
	cmd = "ssh -p 14036 game@39.96.244.26 tail -n 29 input/log/server_1003/chat/Info.2019-10-17_* | grep \"client connected\""
	ret, output = commands.getstatusoutput(cmd)
	return output


def main():
	s = get_onlines()
	print(s)



if __name__ == "__main__":
	main()