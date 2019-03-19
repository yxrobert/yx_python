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
# sys.setdefaultencoding('gb2312')
sys.setdefaultencoding('UTF-8')
# sys.setdefaultencoding('ISO-8859-1')


main_rul = "https://www.ygdy8.com"
# url = 'http://www.hello.world/你好世界'
# url_encode = quote(url, safe=string.printable)
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

	with open("web.txt", 'w') as f:
		f.write(req.text)

	addr_list = root.xpath(
	    '//div[@class="co_content8"]/ul/tr/td[@valign="top"]/table/tr/td[@width="55%"]/b/a/@href')
	name_list = root.xpath(
	    '//div[@class="co_content8"]/ul/tr/td[@valign="top"]/table/tr/td[@width="55%"]/b/a/text()')
	
	# print(addr_list)
	# print(name_list)
	# for i in name_list:
	# 	print(i)

	return addr_list, name_list


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
	with open(save_name, 'w') as f:
		f.write(req.text)

	# 
	addr_list = root.xpath(
	    '//table[@align="center"]/tbody/tr/td/a/@href')

	# print name_list
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

	content = ""
	# print len(name_list), len(addr_list)
	count = min(len(name_list), len(addr_list))
	# print count
	for i in range(count):
		print i
		content += str(name_list[i]) + "\n"
		content += str(name_list[i+1]) + "\n"
		content += str(addr_list[i]) + "\n\n"

	print content
	return content

def main():

	# file_name = "蝙蝠侠"
	file_name = "触不可及"
	get_movie(file_name)

	# addr_list, name_list = get_search_result(file_name)
	# for i in addr_list:
	# 	get_movie_addr(i)
	# 	# break
	# get_movie_addr("/html/gndy/dyzz/20120326/36995.html")


	# with open(save_file, 'w') as f:
	# 	for i in movie_list:
	#  		f.write(i[0] + '\n')
	# 		f.write(i[1] + '\n\n')
	# 	f.close()


if __name__ == "__main__":
	main()