#! /usr/bin/env pythontools
#coding=utf-8

# from future import unicode_literals
import sys
from pyecharts.charts import Bar

# [10253 | 0x7efe17ff9b00 | 2020-12-23 10:42:48:10086] MysqlCache [Pktsc_login]Update! 16788:6


type_str = ["sec", "min"]
interval = 0


def cache_process_line(line):
	key = "Cache:38"
	def get_value(line):
		return int(line[line.rfind(":")+1:].strip())

	def get_time(line):
		idx = line.find("]")
		end = line[:idx].rfind(" ") + 1
		return line[end : end+8].replace(":", "")

	def get_type(line):
		if line.find("Insert") != -1:
			return 0
		else:
			return 1
		# l = line.find("]")
		# r = line.rfind("!")
		# return line[l+1 : r]

	return get_time(line), get_type(line), get_value(line)


def main():
	global interval
	file = "reg_sql.txt"
	if len(sys.argv) > 1:
		file = sys.argv[1]
	if len(sys.argv) > 2:
		interval = int(sys.argv[2])

	tab_min = {}
	with open(file, "r") as f:
		lines = f.readlines()
		for l in lines:
			t, tsql, count = cache_process_line(l)

			tm = t[:-2]
			if tm in tab_min:
				tab_min[tm][tsql] += count
			else:
				tab_min[tm] = [0, 0]
				tab_min[tm][tsql] = count

		
	total_insert = 0
	total_update = 0
	# sorted(tab.keys())
	sorted(tab_min.keys())

	insert_list = []
	update_list = []
	for k in tab_min:
		insert_list.append(tab_min[k][0])
		update_list.append(tab_min[k][1])
		total_insert = tab_min[k][0]
		total_update = tab_min[k][1]


	print("%s total %d|%d" % (file, total_insert, total_update))

	#
	barm = Bar()
	name = "%s_min_iu(%d_%d).html" % (file.replace(".txt", "") ,total_insert, total_update)
	barm.add_xaxis(list(tab_min.keys()))
	barm.add_yaxis("insert", insert_list)
	barm.add_yaxis("update", update_list)
	barm.render(name)

	# if not b_sec:
	# 	return

	# # 
	# bar = Bar()
	# name = "%s_sec_total(%d).html" % (file.replace(".txt", "") , total)
	# bar.add_xaxis(list(tab.keys()))
	# bar.add_yaxis(name, list(tab.values()))
	# bar.render(name)

if __name__ == '__main__':
	main()