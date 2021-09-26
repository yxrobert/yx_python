#! /usr/bin/env pythontools
#coding=utf-8

# from future import unicode_literals
import sys
from pyecharts.charts import Bar


def process_line(l):
	head = l.rfind("[")
	end = l.rfind("WHERE")

	raw = l[head+1 : end].split(",")
	tabc = {}
	for r in raw:
		l = r.split("=")
		tabc[l[0]] = l[1]
	return tabc


def main():
	file = "dstat.txt"
	if len(sys.argv) > 1:
		file = sys.argv[1]

	tab = {}
	count = 0
	old = []
	with open(file, "r") as f:
		lines = f.readlines()
		for l in lines:
			t = process_line(l)
			# print(t)
			old.append(t)
			if count > 0:
				for k in t:
					# print("%d:%s  %s|%s" % (count, k, t[k], old[count-1][k]))
					if t[k] != old[count-1][k]:
						print("Find %d:%s" % (count, k))
			count += 1
	print(len(old))




if __name__ == '__main__':
	main()