#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from datetime import datetime
import time
import requests
import json, sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('UTF-8')

weather_url = 'http://t.weather.sojson.com/api/weather/city/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"}

weather_moji_url = 'https://tianqi.moji.com/weather/china'


def get_weather_info_moji(position):
	url = weather_url + str(city_code)
	resp = requests.get(url, headers=headers)

	if resp.status_code == 200 and resp.json().get('status') == 200:
		root = etree.HTML(resp.text)


day_desc = [
	u"今天",
	u"明天",
	u"后天",
	u"大后天",
	u"大大后天",
	u"大大大后天",
	u"大大大大后天",
]

def get_dictum_info():
	user_url = 'http://wufazhuce.com/'
	resp = requests.get(user_url, headers=headers)
	soup_texts = BeautifulSoup(resp.text, 'lxml')
	# 『one -个』 中的每日一句
	every_msg = soup_texts.find_all('div', class_='fp-one-cita')[0].find('a').text
	return every_msg

def constellation(cons):
	url = 'http://www.xzw.com/fortune/' + cons
	resp = requests.get(url, headers=headers)
	soup_texts = BeautifulSoup(resp.text, 'lxml')

	# print soup.find_all('dl')
	html2 = soup_texts.find('div', class_='c_cont')
	html2 = str(html2)
	soup_texts = BeautifulSoup(html2)
	text = cons + '今日运势：' + '\n'
	text = text + '整体运势：' + soup_texts.find_all('span')[0].string + '\n\n'
	text = text + '事业运势：' + soup_texts.find_all('span')[2].string + '\n\n'
	text = text + '财富运势：' + soup_texts.find_all('span')[3].string + '\n\n'
	text = text + '健康运势：' + soup_texts.find_all('span')[4].string + '\n\n'
	return text


def get_weather_info(city_code, idx = 0):
	
	url = weather_url + str(city_code)
	resp = requests.get(url, headers=headers)

	if idx >= len(day_desc):
		idx = 0

	if resp.status_code == 200 and resp.json().get('status') == 200:
		weatherJson = resp.json()
		# 天气
		today_weather = weatherJson.get('data').get('forecast')[idx]
		# 日期
		today_time = datetime.now().strftime('%Y年%m月%d日 ') + weatherJson.get('data').get('forecast')[0].get('week')
		# today_time += ('%d日 ') % today_weather.get('date')
		# today_time += today_weather.get('week')

		# 今日天气注意事项
		notice = today_weather.get('notice')
		# 温度
		high = today_weather.get('high')
		high_c = high[high.find(' ') + 1:]
		low = today_weather.get('low')
		low_c = low[low.find(' ') + 1:]

		temperature = u"温度 : %s/%s" % (low_c, high_c)

		# PM
		pm = weatherJson.get('data').get('pm25')
		aqi = weatherJson.get('data').get('quality')
		ganmao = weatherJson.get('data').get('ganmao')
		pm = "今日空气质量 : %s\npm2.5 : %s\n%s" % (aqi, pm, ganmao)


		# 风
		fx = today_weather.get('fx')
		fl = today_weather.get('fl')
		wind = "%s : %s" % (fx, fl)

		# # 空气指数
		# aqi = today_weather.get('aqi')
		# aqi = u"空气质量 : %s" % aqi

		# 天气
		tianqi = today_weather.get('type')
		tianqi = day_desc[idx] + u"天气 : %s" % tianqi

		# 在一起，一共多少天了
		# start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
		# day_delta = (datetime.now() - start_datetime).days
		# delta_msg = f'宝贝这是我们在一起的第 {day_delta} 天'

		content = today_time + "\n"
		content += pm + "\n"
		content += tianqi + "\n"
		# content += delta_msg + "\.\n"
		content += temperature + "\n"
		content += wind + "\n"
		content += notice + "\n"
		
		# content += dictum_msg + "\n"
		# content += sweet_words + "\n"
		# content += "\n"
		# content += get_dictum_info()

		print(content)
		return content


def main():
	s = constellation('taurus')
	# s = get_weather_info(101010300)
	# s = get_weather_info(101010300, 1)
	# s = get_weather_info(101010300, 2)
	# s = get_weather_info(101010300, 3)
	print(s)




if __name__ == "__main__":
	main()