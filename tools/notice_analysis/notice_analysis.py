#! /usr/bin/env pythontools
#coding=utf-8

# from future import unicode_literals
import sys
from pyecharts.charts import Bar

# [10253 | 0x7efe17ff9b00 | 2020-12-23 10:42:48:10086] MysqlCache [Pktsc_login]Update! 16788:6


# type_str = ["sec", "min"]
# interval = 0

# def hash_process_line(line):
# 	def get_value(line):
# 		idx = line.find("=")
# 		end = line[idx:].find(",")
# 		return (int(line[idx+1 : idx + end].strip()) + 1)/2

# 	def get_time(line):
# 		idx = line.find(" ")
# 		end = line.find(".")
# 		return line[idx+1 : end].replace(":", "")	

# 	return get_time(line), get_value(line)


# def list_process_line(line):
# 	def get_value(line):
# 		idx = line.find("=")
# 		return int(line[idx+1 : ].strip())

# 	def get_time(line):
# 		idx = line.find(" ")
# 		end = line.find(".")
# 		return line[idx+1 : end].replace(":", "")

# 	return get_time(line), get_value(line)

# def cache_process_line(line):
# 	key = "Cache:38"
# 	def get_value(line):
# 		# idx = line.find(key)
# 		# return int(line[idx+len(key)+1 : ].strip())
# 		return int(line[line.rfind(":")+1:].strip())

# 	def get_time(line):
# 		idx = line.find("]")
# 		end = line[:idx].rfind(" ") + 1
# 		return line[end : end+8].replace(":", "")	

# 	return get_time(line), get_value(line)


# def select_processor(line):
# 	if line.find("list") != -1:
# 		return list_process_line, True
# 	elif line.find("MysqlCache") != -1:
# 		return cache_process_line, False
# 	else:
# 		return hash_process_line, True

# def main():
# 	global interval
# 	file = "reg_sql.txt"
# 	if len(sys.argv) > 1:
# 		file = sys.argv[1]
# 	if len(sys.argv) > 2:
# 		interval = int(sys.argv[2])

# 	tab = {}
# 	tab_min = {}
# 	b_sec = True
# 	with open(file, "r") as f:
# 		lines = f.readlines()
# 		func_process_line, b_sec = select_processor(lines[0])
# 		for l in lines:
# 			# try:
# 			t, count = func_process_line(l)
# 			# print(t)
# 			# print(count)
# 			# return
# 			tm = t[:-2]
# 			if tm in tab_min:
# 				tab_min[tm] += count
# 			else:
# 				tab_min[tm] = count

# 			if not b_sec:
# 				continue
# 			if t in tab:
# 				tab[t] += count
# 			else:
# 				tab[t] = count

# 			# except:
# 			# 	pass
				
# 	total = 0
# 	sorted(tab.keys())
# 	sorted(tab_min.keys())

# 	# for k in tab:
# 	# 	total += tab[k]
# 	for k in tab_min:
# 		total += tab_min[k]

# 	print("%s total %d" % (file, total))

# 	#
# 	barm = Bar()
# 	name = "%s_min_total(%d).html" % (file.replace(".txt", "") , total)
# 	barm.add_xaxis(list(tab_min.keys()))
# 	barm.add_yaxis(name, list(tab_min.values()))
# 	barm.render(name)

# 	if not b_sec:
# 		return

# 	# 
# 	bar = Bar()
# 	name = "%s_sec_total(%d).html" % (file.replace(".txt", "") , total)
# 	bar.add_xaxis(list(tab.keys()))
# 	bar.add_yaxis(name, list(tab.values()))
# 	bar.render(name)

def filter_key(line):
	idx = line.find("]")
	head = line[:idx].rfind(" ")
	end = line[:idx].rfind(":")
	return int(line[head+1 : end].replace(":", ""))

def filter_data(line):
	frame_key = "frame_handle_call_times"
	idx = line.find(frame_key)
	if idx < 0:
		return idx
	else:
		return int(line[idx + len(frame_key) + 1 : ])

force_key_list = [
	"Pktsc_world_chat",
	"Pktsc_get_user_force_rank",
	"Pktsc_login",
	"Pktsc_jump_point_search_req",
	"Pktsc_corps_home",
	"process_one_event_type=[1]",
	"Pktsc_corps_move",
]
add_key = "addtimes="

def filter_force_data(line):
	for k in force_key_list:
		if line.find(k) > 0:
			idx = line.find(add_key)
			if idx < 0: return "", 0
			end = line[idx : ].find(",")
			# print(k)
			return k, int(line[idx + len(add_key) : idx + end])
	return "", 0

def gen_html(name, tab):
	barm = Bar()
	name = "%s.html" % (name)
	barm.add_xaxis(list(tab.keys()))
	barm.add_yaxis(name, list(tab.values()))
	barm.render(name)

def main():
	file = "9.150.53.189_data_home_user00_woc_log_Notice.2021-01-12_07.log"
	if len(sys.argv) > 1:
		file = sys.argv[1]
	if len(sys.argv) > 2:
		interval = int(sys.argv[2])

	# 
	data_tab = {}
	tab = {}
	t = -1
	count = 0
	with open(file, "r") as f:
		lines = f.readlines()

		for l in lines:
			if l.find("-GameStatistics:-") != -1:
				t = filter_key(l)
				continue

			if t < 0:
				continue

			#
			count = filter_data(l)
			if count > 0:
				if t in tab:
					tab[t] += count
				else:
					tab[t] = count

			# 
			k, add = filter_force_data(l)
			if k != "" and add > 0:
				if k not in data_tab:
					print(k)
					data_tab[k] = {}

				if t in data_tab[k]:
					data_tab[k][t] += add
				else: 
					data_tab[k][t] = add


	sorted(tab.keys())

	#
	end = file.rfind(".")
	head = file[ : end].rfind(".")
	name = "notice_%s" % (file[head+1 : end])
	gen_html(name, tab)


	for k in data_tab:
		sorted(data_tab[k].keys())
		gen_html(k, data_tab[k])



if __name__ == '__main__':
	main()