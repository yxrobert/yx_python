#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from lxml import etree
import requests
import sys
import re
from urllib import quote
from urllib import unquote  
import string

# https://blog.csdn.net/findhappy117/article/details/83748374

reload(sys)
sys.setdefaultencoding('UTF-8')


main_rul = "https://www.ygdy8.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"}


def request_url(url):
	while True:
		try:
			r = requests.get(url,headers=header)
			if r.status_code == 200:
				r.encoding = 'gbk'
				return r.text
		except:
			pass


def get_search_result(film_name):

	film_name = film_name.encode('gb2312')
	name = quote(film_name, safe=string.printable)
	url = "http://s.ygdy8.com/plus/so.php?typeid=1&keyword=%s" % name
	req = requests.get(url, headers=headers)

	req.encoding = 'gbk'
	root = etree.HTML(req.text)

	# with open("web.txt", 'w') as f:
	# 	f.write(req.text)

	addr_list = root.xpath(
	    '//div[@class="co_content8"]/ul/tr/td[@valign="top"]/table/tr/td[@width="55%"]/b/a/@href')
	name_list = root.xpath(
	    '//div[@class="co_content8"]/ul/tr/td[@valign="top"]/table/tr/td[@width="55%"]/b/a/text()')
	
	# print(addr_list)
	# print(name_list)

	# l = parse_name_list(name_list)
	# print(name_list)
	l = []
	for i in name_list:
		s = "%s" % i
		l.append(s)
	# for i in name_list:
	# 	print(i)
	# print l
	return addr_list, l


def get_movie_addr(url_addr):
	url_addr = main_rul + url_addr
	# print(url_addr)
	req = requests.get(url_addr, headers=headers)
	req.encoding = 'gbk'
	root = etree.HTML(req.text)

	# 
	head = url_addr.rfind('/')
	tail = url_addr.rfind('.')
	save_name = url_addr[head+1:tail] + '.txt'
	# print(save_name)
	# with open(save_name, 'w') as f:
	# 	f.write(req.text)

	# 
	addr_list = root.xpath(
	    '//table[@align="center"]/tbody/tr/td/a/@href')

	# print addr_list
	l = []
	for i in addr_list:
		s = "%s" % i
		l.append(s)

	return l


def get_movie(movie_name):
	movie_list, name_list = get_search_result(movie_name)
	addr_list = []
	for i in movie_list:
		addr_list.append(get_movie_addr(i))

	if len(movie_list) <= 0:
		return ""
	
	content = "电影列表：\n"
	n = 0
	for i in name_list:
		if n%2 == 0:
			content += str(i)
			content += movie_name
		else:
			content += str(i) + "\n"
		n += 1
	content += "\n\n"
	content += "下载链接：\n"
	for i in addr_list:
		content += str(i[0].strip()) + "\n\n"
	content += "\n"

	print(content)
	return content

def main():

	file_name = "复仇者联盟"
	# file_name = "小偷家族"
	get_movie(file_name)



if __name__ == "__main__":
	main()