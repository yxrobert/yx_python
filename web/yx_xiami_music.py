#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from datetime import datetime
import time
import requests
import json, sys
from lxml import etree

reload(sys)
sys.setdefaultencoding('UTF-8')


url = 'https://www.xiami.com/collect/100901693'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"}


def main():
	req = requests.get(url, headers=headers)

	# req.encoding = 'gbk'
	root = etree.HTML(req.text)

	with open("music_web.txt", 'w') as f:
		f.write(req.text)


if __name__ == '__main__':
	main()