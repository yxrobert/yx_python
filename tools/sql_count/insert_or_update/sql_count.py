#! /usr/bin/env pythontools
#coding=utf-8

# from future import unicode_literals
import sys
from pyecharts.charts import Bar

# [10253 | 0x7efe17ff9b00 | 2020-12-23 10:42:48:10086] MysqlCache [Pktsc_login]Update! 16788:6


type_str = ["sec", "min"]
interval = 0

def hash_process_line(line):
	def get_value(line):
		idx = line.find("=")
		end = line[idx:].find(",")
		return (int(line[idx+1 : idx + end].strip()) + 1)/2

	def get_time(line):
		idx = line.find(" ")
		end = line.find(".")
		return line[idx+1 : end].replace(":", "")	

	return get_time(line), get_value(line)


def list_process_line(line):
	def get_value(line):
		idx = line.find("=")
		return int(line[idx+1 : ].strip())

	def get_time(line):
		idx = line.find(" ")
		end = line.find(".")
		return line[idx+1 : end].replace(":", "")

	return get_time(line), get_value(line)

def cache_process_line(line):
	key = "Cache:38"
	def get_value(line):
		# idx = line.find(key)
		# return int(line[idx+len(key)+1 : ].strip())
		return int(line[line.rfind(":")+1:].strip())

	def get_time(line):
		idx = line.find("]")
		end = line[:idx].rfind(" ") + 1
		return line[end : end+8].replace(":", "")	

	return get_time(line), get_value(line)


def select_processor(line):
	if line.find("list") != -1:
		return list_process_line, True
	elif line.find("MysqlCache") != -1:
		return cache_process_line, False
	else:
		return hash_process_line, True

def main():
	global interval
	file = "reg_sql.txt"
	if len(sys.argv) > 1:
		file = sys.argv[1]
	if len(sys.argv) > 2:
		interval = int(sys.argv[2])

	tab = {}
	tab_min = {}
	b_sec = True
	with open(file, "r") as f:
		lines = f.readlines()
		func_process_line, b_sec = select_processor(lines[0])
		for l in lines:
			# try:
			t, count = func_process_line(l)
			# print(t)
			# print(count)
			# return
			tm = t[:-2]
			if tm in tab_min:
				tab_min[tm] += count
			else:
				tab_min[tm] = count

			if not b_sec:
				continue
			if t in tab:
				tab[t] += count
			else:
				tab[t] = count

			# except:
			# 	pass
				
	total = 0
	sorted(tab.keys())
	sorted(tab_min.keys())

	# for k in tab:
	# 	total += tab[k]
	for k in tab_min:
		total += tab_min[k]

	print("%s total %d" % (file, total))

	#
	barm = Bar()
	name = "%s_min_total(%d).html" % (file.replace(".txt", "") , total)
	barm.add_xaxis(list(tab_min.keys()))
	barm.add_yaxis(name, list(tab_min.values()))
	barm.render(name)

	if not b_sec:
		return

	# 
	bar = Bar()
	name = "%s_sec_total(%d).html" % (file.replace(".txt", "") , total)
	bar.add_xaxis(list(tab.keys()))
	bar.add_yaxis(name, list(tab.values()))
	bar.render(name)

if __name__ == '__main__':
	main()