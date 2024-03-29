#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from datetime import datetime
import time
import requests
import json, sys
from bs4 import BeautifulSoup
import yx_yi as YI

# reload(sys)
# sys.setdefaultencoding('UTF-8')

weather_url = 'http://t.weather.sojson.com/api/weather/city/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"}

weather_moji_url = 'https://tianqi.moji.com/weather/china/'


day_desc = [
	u"今天",
	u"明天",
	u"后天",
	u"大后天",
	u"大大后天",
	u"大大大后天",
	u"大大大大后天",
]


def get_gua_ex(x=-1, y=-1):
	idx = str(YI.get_yi_idx(x, y) + 1)
	idx.zfill(2)
	gua_url = "https://m.k366.com/gua/1200000-11-%s.htm" % idx
	resp = requests.get(gua_url, headers=headers)
	resp.encoding = 'utf-8'
	soup_texts = BeautifulSoup(resp.text, 'lxml')

	s = ""
	title = ""
	con = ""
	for i in soup_texts.find_all('meta'):
		if i.get('name') == 'description':
			con = i.get('content')
		elif i.get('name') == 'keywords':
			title = i.get('content')
			idx = title.find('-')
			title = title[:idx]
	s += title + '\n'
	s += con + '\n\n'

	for i in soup_texts.find_all('span', class_='f16 pink'):
		s += i.get_text() + '\n\n'

	for i in soup_texts.find_all('p', class_='f14 l150'):
		s += i.get_text() + '\n'
	# print(s)
	return s


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
	text = text + '爱情运势：' + soup_texts.find_all('span')[1].string + '\n\n'
	text = text + '事业运势：' + soup_texts.find_all('span')[2].string + '\n\n'
	text = text + '财富运势：' + soup_texts.find_all('span')[3].string + '\n\n'
	text = text + '健康运势：' + soup_texts.find_all('span')[4].string + '\n\n'
	return text

def get_weather_info_moji(area):
	url = weather_moji_url + area
	resp = requests.get(url, headers=headers)
	# htmlData = requests.urlopen(url).read().decode('utf-8')
	soup = BeautifulSoup(resp.text, 'lxml')

	weather = soup.find('div',attrs={'class':"wea_weather clearfix"})
	temp1 = weather.find('em').get_text()
	temp2 = weather.find('b').get_text()

	# 空气质量AQI
	AQI = soup.select(".wea_alert.clearfix > ul > li > a > em")[0].get_text()
	#湿度
	H = soup.select(".wea_about.clearfix > span")[0].get_text()
	#风速
	S = soup.select(".wea_about.clearfix > em")[0].get_text()

	#今日天气提示
	A = soup.select(".wea_tips.clearfix em")[0].get_text()
	#紫外线强度
	U = soup.select(".live_index_grid > ul > li")[-3].find('dt').get_text()
	#获取当天日期
	DATE = datetime.now().strftime('%Y年%m月%d日 %A')

	info = DATE + '\n'
	info += '实时温度：' + temp1 + '℃' + ',' + temp2 + '\n'  
	info += '湿度：' + H + '\n' 
	info += '风速：' + S + '\n' 
	info += '紫外线：' + U +'\n' 
	info += '今日提示：' + A +'\n\n'

	#获取明日天气
	tomorrow = soup.select(".days.clearfix ")[1].find_all('li')
	#明日温度
	temp_t = tomorrow[2].get_text().replace('°','℃')+ ','  + tomorrow[1].find('img').attrs['alt']
	S_t1 = tomorrow[3].find('em').get_text()
	S_t2 = tomorrow[3].find('b').get_text()
	#明日风速
	S_t = S_t1 + S_t2
	#明日空气质量
	AQI_t = tomorrow[-1].get_text().strip()

	info += '\n明日天气：\n' 
	info += '温度：' + temp_t + '\n'
	info += '风速：' + S_t + '\n' 
	info += '空气质量：' + AQI_t + '\n'

	print(info)
	return info


def get_weather_info_moji_ex(area):
	url = weather_moji_url + area
	resp = requests.get(url, headers=headers)
	soup = BeautifulSoup(resp.text, 'lxml')

	#获取当天日期
	DATE = datetime.now().strftime('%Y年%m月%d日 %A')
	# 空气质量AQI
	AQI = soup.select(".wea_alert.clearfix > ul > li > a > em")[0].get_text()
	# print(soup.head)
	weather = soup.head.find('meta',attrs={'name':"description"})
	desc = weather["content"]
	idx = desc.find("墨迹天气") - 1
	desc = desc[:idx] + '，空气质量:' + str(AQI) + '，关心你的人' + desc[idx + 5:]
	# desc.replace("墨迹天气", "chenpeng")

	info = DATE + '\n'
	info += desc + '\n'

	#获取明日天气
	tomorrow = soup.select(".days.clearfix ")[1].find_all('li')
	#明日温度
	temp_t = tomorrow[2].get_text().replace('°','℃')+ ','  + tomorrow[1].find('img').attrs['alt']
	S_t1 = tomorrow[3].find('em').get_text()
	S_t2 = tomorrow[3].find('b').get_text()
	#明日风速
	S_t = S_t1 + S_t2
	#明日空气质量
	AQI_t = tomorrow[-1].get_text().strip()

	info += '\n明日天气：\n' 
	info += '温度：' + temp_t + '\n'
	info += '风速：' + S_t + '\n' 
	info += '空气质量：' + AQI_t + '\n'

	print(info)
	return info



def get_t_weather_info(city_code, idx = 0):
	
	url = weather_url + str(city_code)
	resp = requests.get(url, headers=headers)
	print(url)
	print(resp)
	if idx >= len(day_desc):
		idx = 0

	if resp.status_code == 200 and resp.json().get('status') == 200:
		weatherJson = resp.json()
		# 天气
		today_weather = weatherJson.get('data').get('forecast')[idx]
		# 日期
		today_time = datetime.now().strftime('%Y年%m月%d日 %A')
		 # + weatherJson.get('data').get('forecast')[0].get('week')
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

def get_weather_info(city_code, area, idx = 0):
	try:
		return get_weather_info_moji_ex(area)
	except Exception:
		return get_t_weather_info(city_code, idx = 0)
	


# https://www.guoyi360.com/64gua03/
def get_gua(x=-1, y=-1):
	idx = str(YI.get_yi_idx(x, y) + 1)
	idx.zfill(2)
	# print(idx)
	gua_url = "https://www.guoyi360.com/64gua%s/" % idx
	resp = requests.get(gua_url, headers=headers)
	# print(resp.encoding)
	# resp.encoding = 'gb2312'
	soup_texts = BeautifulSoup(resp.text, 'lxml', fromEncoding="utf-8")

	s = ""
	con = ""
	con = soup_texts.select('div[class="pddh-list64gua"]')[0].text
	print(con)
	s += con + '\n\n'

	# print(s)
	return s


def main():
	# s = get_gua()
	# s = constellation('taurus')
	# s = get_weather_info(101010300)
	# s = get_weather_info(101010300, 1)
	# s = get_weather_info(101010300, 2)
	# s = get_weather_info(101010300, 3)

	# s = get_weather_info_moji_ex("beijing/chaoyang-district")
	s = get_gua_ex(10, 10)
	print(s)




if __name__ == "__main__":
	main()
