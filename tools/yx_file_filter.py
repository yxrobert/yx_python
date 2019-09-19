#! /usr/bin/env pythontools
#coding=utf-8

import os.path

file_dir = "/home/game/GameServer/server/log"
filter_name = 'Warning.2019-'
# redis_log = "redis statistics cmd="
check_redis_lv = 20
check_mem_get_lv = 10
check_mem_mget_lv = 5


table_record = {}

def process_map(name, val):
	if table_record.has_key(name):
		if table_record[name] < val:
			table_record[name] = val
	else:
		table_record[name] = val

# def process_line(line):
# 	idx = line.find(redis_log)
# 	idx_head = line.find(']')
# 	if idx != -1:
# 		head = line.find('=')
# 		if head != -1:
# 			val = int(line[head + 1: ])
# 			if val > check_lv:
# 				table_name = line[idx_head + 2 : idx]
# 				process_map(table_name, val)
# 				return line
# 	return "" 

def get_head_str(line):
	# Pktsc_get_land_info
	head_begin = line.find(']') + 2
	head_end = line[head_begin : ].find(" ")
	return line[head_begin : head_begin + head_end]

def check_redis(line, key):
	head_str = get_head_str(line)
	val_key = 'cmd='
	head = line.find(val_key)
	if head != -1:
		val = int(line[head + len(val_key): ])
		if val > check_redis_lv:
			head_str += ':' + key + ':' + val_key
			process_map(head_str, val)
			return line
	return "" 

def check_memcache(line, key):
	head_str = get_head_str(line)
	val_key = 'get='
	head = line.find(val_key)
	if head != -1:
		head += len(val_key)
		end = line[head + 1 : ].find(' ')
		if end != -1:
			val = int(line[head : head + end + 1])
			if val >= check_mem_get_lv:
				head_str += ':' + key + ':' + val_key
				process_map(head_str, val)
				# return line
			else:
				# print('mget=')
				val_key = 'mget='
				head = line.find(val_key)
				if head != -1:
					head += len(val_key)
					end = line[head : ].find('\n')
					if end != -1:
						# print(line[head : head + end + 1])
						val = int(line[head : head + end + 1])
						if val >= check_mem_mget_lv:
							head_str += ':' + key + ':' + val_key
							process_map(head_str, val)
							# return line
	return ""

check_table = {"redis statistics" : [check_redis]
	, "memcached statistics" : [check_memcache]}

def process_line(line):
	for k in check_table:
		if line.find(k) != -1:
			return check_table[k][0](line, k)


def main():

	with open(filter_name + '_all_filter.txt', 'w') as f_save:
		# print(file_dir)
		for parent, dirnames, filenames in os.walk(file_dir):
			for filename in filenames:
				if filename.find(filter_name) != -1:
					fname = os.path.join(parent,filename)
					# print(fname)
					with open(fname, 'r') as f:
						line = f.readline()
						while line:
							log = process_line(line)
							# if log != "":
							# 	f_save.write(log)
							# break
							line = f.readline()
					# break

		for k in table_record.keys():
			f_save.write(k + " : " + str(table_record[k]) + "\n")

if __name__ == '__main__':
	main()