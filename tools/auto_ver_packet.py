#! /usr/bin/env python
#coding=utf-8

import os, sys, time

def do_command(cmd):
	print(cmd)
	with os.popen(cmd) as ret:
		ret.readlines()

def do_command_result(cmd):
	print(cmd)
	with os.popen(cmd) as ret:
		return ret.readlines()[0]

def replace_md5(file):
	cmd = "md5sum " + file
	md5_str = do_command_result(cmd)
	print("new " + md5_str)

	cmd = "egrep " + file + " md5.txt" 
	old_str = do_command_result(cmd)
	print("old " + old_str)

	cmd = "sed -i s/\"%s\"/\"%s\"/g md5.txt" % (old_str.strip(), md5_str.strip())
	do_command(cmd)

def packet(packet, version, files):
	d = time.strftime("%Y%m%d%H%M")
	name = "loc_%s_v%s_%s.tar.gz" % (packet, version, d)
	cmd = "tar zcvf %s md5.txt %s" % (name, " ".join(files))
	do_command(cmd)

def get_val(filed):
	cmd = "egrep " + filed + " version.conf"
	ret = do_command_result(cmd)
	return ret[ret.find(" ") + 1 : ].strip()

def get_version():
	s = ""
	s += get_val("MT_MajorVer")
	s += get_val("MT_ProtoVer")
	s += get_val("MT_MinorVer")
	s += get_val("MT_ReserVer")
	return s


files = [
	"version.conf",
]

def main():

	packet_name = "pr3"
	if len(sys.argv) > 1:
		packet_name = sys.argv[1]

	for f in files:
		replace_md5(f)

	ver_str = get_version()
	packet(packet_name, ver_str, files)


if __name__ == '__main__':
    main()
