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


# main_rul = "http://s.ygdy8.com/plus/so.php?typeid=1&keyword=%s"
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

# def crawls_home(film_name):
# 	name = quote(film_name, safe=string.printable)
# 	print name
# 	url = "http://s.ygdy8.com/plus/so.php?typeid=1&keyword=%s" % name
# 	html = request_url(url)
# 	soup = BeautifulSoup(html,'lxml')
# 	print soup
# 	div = soup.find('div',class_="co_content8")
# 	if div is None:
# 		return ['没有搜到相应电影']
# 	film_list = div.find_all('table',border="0",width="100%")
# 	return film_list

save_file = "web.txt"
def get_movie(film_name):

	film_name = film_name.encode('gb2312')
	name = quote(film_name, safe=string.printable)
	url = "http://s.ygdy8.com/plus/so.php?typeid=1&keyword=%s" % name
	req = requests.get(url, headers=headers)
	# print req.encoding
	# print req.text

	req.encoding = 'gbk'
	root = etree.HTML(req.text)

	with open(save_file, 'w') as f:
		f.write(req.text)

	name_list = root.xpath(
	    '//div[@class="co_content8"]/ul/tr/td/text()')
	    # '//div[@class="co_content8"]/ul/tr/td[@width="55%"]/b/a/@href')
	for i in name_list:
		print i


	# name_list = root.xpath(
	#     '//a[contains(@href, "forum.php?") and @onclick="atarget(this)"]/text()')
	# url_list = root.xpath(
	#     '//a[contains(@href, "forum.php?") and @onclick="atarget(this)"]/@href')

 # 	mvsearch_list = root.xpath(
 #                '//div[@class="co_content8"]/ul/tr/td/table[@width="100%"]')

	# if len(mvsearch_list) == 0:
	# 	print("未搜索到任何内容")
	# 	return -1


	# mvcontent_url = []
	# mvcontent_title = []

 #    # 提取搜索结果中的电影链接
	# mvsearch_list_len = len(mvsearch_list)
	# for idx in range(1, mvsearch_list_len+1):
 #        # 提取链接
	# 	mv_title_url = etree_html.xpath(
	# 		mvsearch_xpath + '[{0}]//a[@href]/@href'.format(idx))
	# 	# print(mv_title_url)

	# 	if mv_title_url == None:
	# 		print("解析出错!")
	# 		return -1

	# 	# 过滤掉游戏
	# 	if mv_title_url[0].find("/html/game/") < 0:
	# 		mv_title_url = "{0}{1}".format(MOVIE_URL, mv_title_url[0])
	# 		mvcontent_url.insert(idx-1, mv_title_url)
	# 		# 提取标题
	# 		mv_title_str_lst = etree_html.xpath(
	# 			mvsearch_xpath + '[{0}]//a[@href]//text()'.format(idx))
	# 		if mv_title_str_lst == None:
	# 			print("解析出错!")
	# 			return -1
	# 		mv_title_str = "".join(mv_title_str_lst)
	# 		mvcontent_title.insert(idx-1, mv_title_str)
	# 		# print("\t{0}, {1}, {2}".format(idx, mv_title_str, mv_title_url))

	# mvcontent_len = len(mvcontent_url)





def main():

	file_name = "蝙蝠侠"
	# file_name = "触不可及"
	# print file_name
	# movie_list = crawls_home(file_name)
	get_movie(file_name)


	# with open(save_file, 'w') as f:
	# 	for i in movie_list:
	#  		f.write(i[0] + '\n')
	# 		f.write(i[1] + '\n\n')
	# 	f.close()


if __name__ == "__main__":
	main()