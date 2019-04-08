#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import time
import random

# 
GUA_LEN = 3
GUA64_LEN = 64
GUA_NUM = 8
YAO_NUM = 6
shang = 0
xia = 1
bian = 2

GUA = [
	[True, True, True],		# 乾/天/0
	[False, True, True],	# 兑/泽/1
	[True, False, True],	# 离/火/2
	[False, False, True],	# 震/雷/3
	[True, True, False],	# 巽/风/4
	[False, True, False],	# 坎/水/5
	[True, False, False],	# 艮/山/6
	[False, False, False],	# 坤/地/7
]

GUA_64 = [
	[0, 0],
	[7, 7],
	[5, 3],
	[6, 5],
	[5, 0],
	[0, 5],
	[7, 5],
	[5, 7],
	[4, 0],
	[0, 1],

	[7, 0],
	[0, 7],
	[0, 2],
	[2, 0],
	[7, 6],
	[3, 7],
	[1, 3],
	[6, 4],
	[7, 1],
	[4, 7],

	[2, 3],
	[6, 2],
	[6, 7],
	[7, 3],
	[0, 3],
	[6, 0],
	[6, 3],
	[1, 4],
	[5, 5],
	[2, 2],

	[1, 6],
	[3, 4],
	[0, 6],
	[3, 0],
	[2, 7],
	[7, 2],
	[4, 2],
	[2, 1],
	[5, 6],
	[3, 5],

	[6, 1],
	[4, 3],
	[1, 0],
	[0, 4],
	[1, 7],
	[7, 4],
	[1, 5],
	[5, 4],
	[1, 2],
	[2, 4],

	[3, 3],
	[6, 6],
	[4, 6],
	[3, 1],
	[3, 2],
	[2, 6],
	[4, 4],
	[1, 1],
	[4, 5],
	[5, 1],

	[4, 1],
	[3, 6],
	[5, 2],
	[2, 5],
] 


# url = "https://m.k366.com/gua/"

#
def get_gua(val):
	val = val % GUA_NUM
	if val == 0:
		return GUA_NUM
	else:
		return val


def get_yao(val):
	val = val % YAO_NUM
	if val == 0:
		return YAO_NUM
	else:
		return val


def get_hour():
	localtime = time.localtime(time.time())
	return int(localtime.tm_hour / 2) + 1

def print_yin():
	pass

def print_yang():
	pass



class YI():
	def __init__(self, _x = -1, _y = -1):
		if _x == -1:
			_x = random.randint(1, 100)
		if _y == -1:
			_y = random.randint(1, 100)

		self.x = _x
		self.y = _y


	def QiGua(self, x, y, data):
		data[shang] = get_gua(x)
		data[xia] = get_gua(y)
		data[bian] = get_yao(x + y + get_hour())


	def ChengGua(self, data, gua):
		gua[shang] = GUA[data[shang] - 1]
		gua[xia] = GUA[data[xia] - 1]

	def BianGua(self, data, gua):
		idx = YAO_NUM - data[bian]
		hf = int(YAO_NUM / 2)
		if idx < hf:
			gua[shang][idx] = not(gua[shang][idx])
		else:
			gua[xia][idx - hf] = not(gua[xia][idx - hf])

	def PrintGua(self, data, gua):
		print(gua)
		# print(data[bian])

	def get_gua_idx(self, gua):
		shang_idx = GUA.index(gua[shang])
		print(shang_idx)
		xia_idx = GUA.index(gua[xia])
		print(xia_idx)
		idx = GUA_64.index([shang_idx, xia_idx])
		print(idx)
		return(idx)

	def go(self):
		# 
		data = []
		data.append(True)
		data.append(True)
		data.append(True)
		gua = []
		gua.append(GUA[0])
		gua.append(GUA[0])


		self.QiGua(self.x, self.y, data)
		self.ChengGua(data, gua)
		self.BianGua(data, gua)
		self.PrintGua(data, gua)

		return(self.get_gua_idx(gua))



def get_yi_idx(x, y):
	yi = YI(x, y)
	return yi.go()

def main():
	# for i in range(0, len(GUA_64)):
	# 	for j in range(i+1, len(GUA_64)):
	# 		if GUA_64[i] == GUA_64[j]:
	# 			print(GUA_64[i])
	yi = YI()
	print(yi.go())

if __name__ == "__main__":
	main()