#! /usr/bin/env pythontools
#coding=utf-8

import os.path

_id = 0

# INSERT INTO `res_log` VALUES ('11', '222', '3313', '5', '6', '7', '78');
# [14798 | 0x7f20d6a89820 | 2018-05-10 11:41:30] {"user_id":4526408887477624832,"uniqueid":"6553792349036544000","approach_type":49,"change_count":5,"current_count":255}

def get_value(line, left, right=','):
	pos = line.find(left) + len(left)
	tail = line[pos:].find(right)
	return line[pos : pos + tail]


def get_time(line):
	pos = line.find(']')
	return line[pos - 19 : pos ]

def process_line(line, t):
	global _id
	l = 'INSERT INTO `res_log` VALUES ('
	l += str(_id) + ','
	_id += 1

	l += get_value(line, 'user_id":', ',') + ', '
	l += '\'' + get_time(line) + '\', '
	l += get_value(line, 'uniqueid":', ',') + ', '
	l += str(t) + ', '
	l += get_value(line, 'approach_type":', ',') + ', '
	l += get_value(line, 'change_count":', ',') + ', '
	l += get_value(line, 'current_count":', '}') + ');\n'
	return l


file_type = {'fame' : 0
			, 'gold_coin' : 1
			, 'grian' : 2
			, 'iron' : 3
			, 'silver_coin' : 4
			, 'stone' : 5
			, 'wood' : 6
			, 'copper' : 7}


def main():

	f_save = open('res.sql', 'w')
	
	for parent, dirnames, filenames in os.walk('.'):
		for filename in filenames:
			if filename.find('.log') != -1:

				fname = os.path.join(parent,filename)
				k = 'op_'
				pos = filename.find(k) + len(k)
				tail = filename[pos:].find('.')
				val = filename[pos: pos + tail]

				if file_type.has_key(val) == False:
					continue

				with open(fname, 'r') as f:
					line = f.readline()
					while line:
						log = process_line(line, file_type[val])
						f_save.write(log)
						# break
						line = f.readline()

				# break


	f_save.close()




if __name__ == '__main__':
	main()