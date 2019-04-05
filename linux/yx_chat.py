#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import yx_search_movie as movie
import yx_weather as weather
from imp import reload
import sys
import itchat, time, threading
# from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

reload(sys)


# 
movie_list = {
	u"小偷家族":"magnet:?xt=urn:btih:047FCD07C11D153A8B7A724D4C253BF373AEF115",
	u"太空漫步2001":"thunder://QUFlZDJrOi8vfGZpbGV8MjAwMSVFNSVBNCVBQSVFNyVBOSVCQSVFNiVCQyVBQiVFNiVCOCVCOC5CRDEyODAlRTglQjYlODUlRTYlQjglODUlRTQlQjglQUQlRTglOEIlQjElRTUlOEYlOEMlRTUlQUQlOTcubXA0fDMxMzIwODgwNTh8NzYxMzUwQTJGOEFBOTI1RDNDODk5RTY0RTI1Q0IwRDB8aD1SRU0yREhIUUJDV1lEUlpQVFg1UFJEUjIzSE1SMkFNVHwvWlo=",
	u"2001太空漫步":"thunder://QUFlZDJrOi8vfGZpbGV8MjAwMSVFNSVBNCVBQSVFNyVBOSVCQSVFNiVCQyVBQiVFNiVCOCVCOC5CRDEyODAlRTglQjYlODUlRTYlQjglODUlRTQlQjglQUQlRTglOEIlQjElRTUlOEYlOEMlRTUlQUQlOTcubXA0fDMxMzIwODgwNTh8NzYxMzUwQTJGOEFBOTI1RDNDODk5RTY0RTI1Q0IwRDB8aD1SRU0yREhIUUJDV1lEUlpQVFg1UFJEUjIzSE1SMkFNVHwvWlo=",
	u"2001太空漫游":"thunder://QUFlZDJrOi8vfGZpbGV8MjAwMSVFNSVBNCVBQSVFNyVBOSVCQSVFNiVCQyVBQiVFNiVCOCVCOC5CRDEyODAlRTglQjYlODUlRTYlQjglODUlRTQlQjglQUQlRTglOEIlQjElRTUlOEYlOEMlRTUlQUQlOTcubXA0fDMxMzIwODgwNTh8NzYxMzUwQTJGOEFBOTI1RDNDODk5RTY0RTI1Q0IwRDB8aD1SRU0yREhIUUJDV1lEUlpQVFg1UFJEUjIzSE1SMkFNVHwvWlo=",
	u"太空漫步2001":"thunder://QUFlZDJrOi8vfGZpbGV8MjAwMSVFNSVBNCVBQSVFNyVBOSVCQSVFNiVCQyVBQiVFNiVCOCVCOC5CRDEyODAlRTglQjYlODUlRTYlQjglODUlRTQlQjglQUQlRTglOEIlQjElRTUlOEYlOEMlRTUlQUQlOTcubXA0fDMxMzIwODgwNTh8NzYxMzUwQTJGOEFBOTI1RDNDODk5RTY0RTI1Q0IwRDB8aD1SRU0yREhIUUJDV1lEUlpQVFg1UFJEUjIzSE1SMkFNVHwvWlo=",
	}
err_log = "err.log"


#
def find_movie(msg, key, idx):
	name = msg['Text'][idx + len(key):].strip()
	print(name)
	# content = 'Good 稍等一下 亲爱的 %s 马上送达' % name
	content = 'Good 稍等一下 %s 马上送达' % name
	itchat.send('%s: %s'%(msg['Type'], content), msg['FromUserName'])

	content = movie.get_movie(name)
	if len(content) < 5:
		content = '没有找到资源！'
		# content = '没有找到资源哦，没关系，可以带你去电影院去看！'
		itchat.send('%s: %s'%(msg['Type'], content), msg['FromUserName'])

		if name in movie_list:
			time.sleep(10)
			content = "找到了！\n"
			itchat.send('%s: %s'%(msg['Type'], content), msg['FromUserName'])
			time.sleep(3)
			content = movie_list[name] + "\n"
			itchat.send('%s: %s'%(msg['Type'], content), msg['FromUserName'])
			time.sleep(5)
			content = "看在我这么辛苦的份上，做我的女朋友吧!老婆。"
			itchat.send('%s: %s'%(msg['Type'], content), msg['FromUserName'])

			return True

		return False
	else:
		itchat.send('%s: %s'%(msg['Type'], content), msg['FromUserName'])

	return True

day_desc = [
	u"大大大大后天",
	u"大大大后天",
	u"大大后天",
	u"大后天",
	u"后天",
	u"明天",
	u"今天",
]

def get_day_desc(desc):
	for k,v in enumerate(day_desc):
		if desc.find(v) != -1:
			return len(day_desc) - k - 1
	return 0

def get_user_city(msg):
	return dear_list[msg['User']['NickName']]


def get_weather(msg, key, idx):
	city_code = get_user_city(msg)
	d = get_day_desc(msg['Text'])
	content = weather.get_weather_info(city_code, d)
	itchat.send('%s: %s'%(msg['Type'], content), msg['FromUserName'])

def get_one(msg, key, idx):
	content = weather.get_dictum_info()
	itchat.send('%s: %s'%(msg['Type'], content), msg['FromUserName'])

# 
func_list = {}
func_list[u"我想看电影"] = find_movie
func_list[u"天气怎么样"] = get_weather
func_list[u"看天气"] = get_weather
func_list[u"天气好"] = get_weather
func_list[u"One"] = get_one


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):

	# itchat.send('%s: %s'%(msg['Type'], msg['FromUserName']), msg['FromUserName'])
	# if msg['FromUserName'] in dear_list:
	# print(msg['User'])
	# print(dear_list[msg['User']['NickName']])

	for key in func_list:
		idx = msg['Text'].find(key)
		if idx == -1:
			continue
		ret = func_list[key](msg, key, idx)

		if ret != True:
			with open(err_log, "a") as f:
				f.write(msg['Text'] + "\n")



# 
def get_uuid_by_name(name):
	friends = itchat.search_friends(name)
	if not friends:
		print('昵称错误')
		return ""
	else:
		name_uuid = friends[0].get('UserName')
		return name_uuid


def get_uuid_by_account(acc):
	friends = itchat.search_friends(wechatAccount=acc)
	if not friends:
		print('昵称错误')
		return acc
	else:
		name_uuid = friends[0].get('UserName')
		return name_uuid


def get_weather_info(name, city_code):
	print(name)
	today_msg = weather.get_weather_info(city_code)
	name_uuid = get_uuid_by_name(name)
	print(name_uuid)
	itchat.send(today_msg, toUserName=name_uuid)



def get_weather_info_ex(name, city_code):
	print(name)
	today_msg = weather.get_weather_info(city_code)
	name_uuid = get_uuid_by_name(name)
	print(name_uuid)
	itchat.send(today_msg, toUserName=name_uuid)

	today_msg = weather.get_dictum_info()
	itchat.send(today_msg, toUserName=name_uuid)


day_func = {}
day_func[0] = get_weather_info
day_func[1] = get_weather_info_ex

def start_today_info(name, city_code, func_idx):
	day_func[func_idx](name, city_code)


# 济南 101120101 朝阳区 101010300
dear_list = {
	# u"单文博" : [6, 30, 101010300, u"swb123aa", 0],
	u"Lifecoach" : [7, 30, 101010300, u"yanxie1103", 0],
	# u'王洋🐳' : [6, 15, 101120101, u"wxid_4070450704312", 0],
	# u'Ada  阿哒哒💭' : [7, 30, 101021300, u"doria3159", 1],
}

# 
def run_daily_job():
	scheduler = BackgroundScheduler()
	for k in dear_list:
		arg = (k, dear_list[k][2], dear_list[k][4])
		scheduler.add_job(start_today_info, 'interval', seconds=20, args=arg)
		# scheduler.add_job(start_today_info, 'cron', hour=dear_list[k][0], minute=dear_list[k][1], args=arg)
	scheduler.start()


# 
#itchat.auto_login(enableCmdQR=2)

run_daily_job()
itchat.auto_login(True)
itchat.run()
