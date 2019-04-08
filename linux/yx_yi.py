#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import time
import random

# 
GUA_LEN = 3
GUA_NUM = 8
YAO_NUM = 6
shang = 0
xia = 1
bian = 2

GUA = [
	[True, True, True],		# 乾/天
	[False, True, True],	# 兑/泽
	[True, False, True],	# 离/火
	[False, False, True],	# 震/雷
	[True, True, False],	# 巽/风
	[False, True, False],	# 坎/水
	[True, False, False],	# 艮/山
	[False, False, False],	# 坤/地
]

url = "https://m.k366.com/gua/"

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
	return localtime.tm_hour / 2 + 1

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
		hf = YAO_NUM / 2
		if idx < hf:
			gua[shang][idx] = not(gua[shang][idx])
		else:
			gua[xia][idx - hf] = not(gua[xia][idx - hf])

	def PrintGua(self, data, gua):
		print(gua)
		print(data[bian])


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


def main():
	yi = YI()
	yi.go()

if __name__ == "__main__":
	main()