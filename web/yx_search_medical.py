#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import json, sys
# import urllib.request
import requests
from lxml import etree

reload(sys)
sys.setdefaultencoding('UTF-8')

#

url_addr = "http://12333.qingdao.gov.cn/grcx2/public/f10030110/index.action?resourceId=10030110&_t=873404&_winid=w7561&cxtj1=1&cxtj2=&cxtj3=1&pageIndex=1&pageSize=10&sortField=&sortOrder="
# url_addr = "http://12333.qingdao.gov.cn/grcx2/public/f10030110/queryYlbxMlcx.action"
# url_addr = "http://12333.qingdao.gov.cn/grcx2/"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

data = {
	'cxtj1' : 1, 
	'cxtj2' : "",
	'cxtj3' : 1,
	'pageIndex' : 1,
	'pageSize' : 10,
	'sortField' : "",
	'sortOrder' : "",
}

def main():
	# req = requests.get(url_addr, headers=headers)
	# print(req.encoding)
	# req.encoding = 'gbk'
	# root = etree.HTML(req.text)

	req = requests.get(url_addr, headers=headers, data=data)
	print(req.text)


if __name__ == "__main__":
	main()


