#-*- coding=utf8 -*-
import sys
# import MySQLdb

reload(sys)
sys.setdefaultencoding( "utf-8" )

import urllib2
from bs4 import BeautifulSoup
import time

def download(url,headers):
	try:
		request = urllib2.Request(url,headers=headers)
		html = urllib2.urlopen(request).read()
		# html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print "error"
		print e.code   #可以打印出来错误代号如404。
		print e.reason  #可以捕获异常
		html = None
	return html

def save(html):
	f = open('thefile.txt', 'w')
	f.write(html)
	f.close()

def read_file():
	f = open('thefile.txt', 'r')
	html = f.read()
	f.close()
	return html

def get_html(url):
	User_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
	headers = {'User_agent': User_agent}
	html = download(url, headers)
	save(html)

def constellation(cons):
	url = 'http://www.xzw.com/fortune/' + cons
	get_html(url)
	html = read_file()
	soup = BeautifulSoup(html)
	# print soup.find_all('dl')
	html2 = soup.find('div', class_='c_cont')
	html2 = str(html2)
	soup = BeautifulSoup(html2)
	text = '双鱼座明日运势：' + '\n'
	text = text + '整体运势：' + soup.find_all('span')[0].string + '\n'
	text = text + '事业学业：' + soup.find_all('span')[2].string + '\n'
	text = text + '健康运势：' + soup.find_all('span')[4].string + '\n'
	return text
	# html = urllib2.urlopen(url)
	# print html
if __name__=='__main__':
	weather_text = weather()
