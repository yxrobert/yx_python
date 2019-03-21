#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from datetime import datetime
import time
import requests
import json

weather_url = 'http://t.weather.sojson.com/api/weather/city/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"}


def get_weather_info(city_code):
	
	url = weather_url + str(city_code)
	resp = requests.get(url, headers=headers)

	if resp.status_code == 200 and resp.json().get('status') == 200:
		weatherJson = resp.json()
		# 今日天气
		today_weather = weatherJson.get('data').get('forecast')[1]
		# 今日日期
		today_time = datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')
		# 今日天气注意事项
		notice = today_weather.get('notice')
		# 温度
		high = today_weather.get('high')
		high_c = high[high.find(' ') + 1:]
		low = today_weather.get('low')
		low_c = low[low.find(' ') + 1:]

		temperature = u"温度 : %s/%s" % (low_c, high_c)

		# 风
		fx = today_weather.get('fx')
		fl = today_weather.get('fl')
		wind = "%s : %s" % (fx, fl)

		# 空气指数
		aqi = today_weather.get('aqi')
		aqi = u"空气 : %s" % aqi

		# 在一起，一共多少天了
		# start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
		# day_delta = (datetime.now() - start_datetime).days
		# delta_msg = f'宝贝这是我们在一起的第 {day_delta} 天'

		content = today_time + "\n"
		# content += delta_msg + "\.\n"
		content += notice + "\n"
		content += temperature + "\n"
		content += wind + "\n"
		content += aqi + "\n"
		content += dictum_msg + "\n"
		# content += sweet_words + "\n"

		print(content)
		return content


def main():
	s = get_weather_info(101010300)
	print(s)



if __name__ == "__main__":
	main()