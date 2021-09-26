#! /usr/bin/env pythontools
#coding=utf-8

# from future import unicode_literals
import sys
from pyecharts import options as opts
from pyecharts.charts import Pie

# [6587 | 0x7f34b1574b00 | 2020-12-22 12:50:07:651698] MysqlCache [serverLogicTick]Count! 505233:14


def cache_process_line(line):
	key = "Cache:38"
	def get_value(line):
		# idx = line.find(key)
		# return int(line[idx+len(key)+1 : ].strip())
		return int(line[line.rfind(":")+1:].strip())

	def get_key(line):
		end = line.find("]C")
		head = line[ : end].rfind("[")
		return line[head+1 : end]
		# idx = line.find("]")
		# end = line[:idx].rfind(" ") + 1
		# return line[end : end+8].replace(":", "")	

	return get_key(line), get_value(line)



def main():
	global interval
	file = "reg_sql.txt"
	if len(sys.argv) > 1:
		file = sys.argv[1]
	if len(sys.argv) > 2:
		interval = int(sys.argv[2])

	tab = {}
	b_sec = True
	with open(file, "r") as f:
		lines = f.readlines()
		for l in lines:
			# try:
			t, count = cache_process_line(l)
			if t in tab:
				tab[t][1] += count
				tab[t][0] += 1
			else:

				tab[t] = [1, count]
				
	total = 0
	# sorted(tab.values()[1])
	# sorted(tab_min.keys())
	count_list = []
	speed_list = []
	for k in tab:
		print("%s |times:%d |count:%d |average:%2f" % (k, tab[k][0], tab[k][1], tab[k][1]/tab[k][0]))
		total += tab[k][1]
		count_list.append(opts.PieItem(name=k, value=tab[k][1]))
		speed_list.append(opts.PieItem(name=k, value=tab[k][1]/tab[k][0]))
	print("%s total %d" % (file, total))

	count_list = sorted(count_list, key=lambda i: int(i.get("value")))
	speed_list = sorted(speed_list, key=lambda i: float(i.get("value")))
	# count_list.sort()
	# speed_list.sort()

	#
	pie = Pie()
	name = "%s_total(%d)" % (file.replace(".txt", "") , total)
	pie.add(name, count_list)
	pie.render(name + ".html")

	pie2 = Pie()
	name = "%s_average" % (file.replace(".txt", ""))
	pie2.add(name, speed_list)
	pie2.render(name + ".html") 

if __name__ == '__main__':
	main()