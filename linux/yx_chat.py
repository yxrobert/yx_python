#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import yx_search_movie as movie
import yx_weather as weather
from imp import reload
import sys
import itchat
import time
import threading
import os
# from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import yx_voice as voice
import yx_word_to_voice as word

reload(sys)


#
movie_list = {
	u"小偷家族": "magnet:?xt=urn:btih:047FCD07C11D153A8B7A724D4C253BF373AEF115",
	u"太空漫步2001": "thunder://QUFlZDJrOi8vfGZpbGV8MjAwMSVFNSVBNCVBQSVFNyVBOSVCQSVFNiVCQyVBQiVFNiVCOCVCOC5CRDEyODAlRTglQjYlODUlRTYlQjglODUlRTQlQjglQUQlRTglOEIlQjElRTUlOEYlOEMlRTUlQUQlOTcubXA0fDMxMzIwODgwNTh8NzYxMzUwQTJGOEFBOTI1RDNDODk5RTY0RTI1Q0IwRDB8aD1SRU0yREhIUUJDV1lEUlpQVFg1UFJEUjIzSE1SMkFNVHwvWlo=",
	u"2001太空漫步": "thunder://QUFlZDJrOi8vfGZpbGV8MjAwMSVFNSVBNCVBQSVFNyVBOSVCQSVFNiVCQyVBQiVFNiVCOCVCOC5CRDEyODAlRTglQjYlODUlRTYlQjglODUlRTQlQjglQUQlRTglOEIlQjElRTUlOEYlOEMlRTUlQUQlOTcubXA0fDMxMzIwODgwNTh8NzYxMzUwQTJGOEFBOTI1RDNDODk5RTY0RTI1Q0IwRDB8aD1SRU0yREhIUUJDV1lEUlpQVFg1UFJEUjIzSE1SMkFNVHwvWlo=",
	u"2001太空漫游": "thunder://QUFlZDJrOi8vfGZpbGV8MjAwMSVFNSVBNCVBQSVFNyVBOSVCQSVFNiVCQyVBQiVFNiVCOCVCOC5CRDEyODAlRTglQjYlODUlRTYlQjglODUlRTQlQjglQUQlRTglOEIlQjElRTUlOEYlOEMlRTUlQUQlOTcubXA0fDMxMzIwODgwNTh8NzYxMzUwQTJGOEFBOTI1RDNDODk5RTY0RTI1Q0IwRDB8aD1SRU0yREhIUUJDV1lEUlpQVFg1UFJEUjIzSE1SMkFNVHwvWlo=",
	u"太空漫游2001": "thunder://QUFlZDJrOi8vfGZpbGV8MjAwMSVFNSVBNCVBQSVFNyVBOSVCQSVFNiVCQyVBQiVFNiVCOCVCOC5CRDEyODAlRTglQjYlODUlRTYlQjglODUlRTQlQjglQUQlRTglOEIlQjElRTUlOEYlOEMlRTUlQUQlOTcubXA0fDMxMzIwODgwNTh8NzYxMzUwQTJGOEFBOTI1RDNDODk5RTY0RTI1Q0IwRDB8aD1SRU0yREhIUUJDV1lEUlpQVFg1UFJEUjIzSE1SMkFNVHwvWlo=",
	u"太空漫步": "thunder://QUFlZDJrOi8vfGZpbGV8MjAwMSVFNSVBNCVBQSVFNyVBOSVCQSVFNiVCQyVBQiVFNiVCOCVCOC5CRDEyODAlRTglQjYlODUlRTYlQjglODUlRTQlQjglQUQlRTglOEIlQjElRTUlOEYlOEMlRTUlQUQlOTcubXA0fDMxMzIwODgwNTh8NzYxMzUwQTJGOEFBOTI1RDNDODk5RTY0RTI1Q0IwRDB8aD1SRU0yREhIUUJDV1lEUlpQVFg1UFJEUjIzSE1SMkFNVHwvWlo=",
	}
err_log = "err.log"


#
def find_movie(msg, key, idx):
	name = msg['Text'][idx + len(key):].strip()
	print(name)
	# content = 'Good 稍等一下 亲爱的 %s 马上送达' % name
	content = 'Good 稍等一下 %s 马上送达' % name
	itchat.send('%s: %s' % (msg['Type'], content), msg['FromUserName'])

	content = movie.get_movie(name)
	if len(content) < 5:
		content = '没有找到资源！'
		# content = '没有找到资源哦，没关系，可以带你去电影院去看！'
		itchat.send('%s: %s' % (msg['Type'], content), msg['FromUserName'])

		if name in movie_list:
			time.sleep(10)
			content = "找到了！\n"
			itchat.send('%s: %s' % (msg['Type'], content), msg['FromUserName'])
			time.sleep(3)
			content = movie_list[name] + "\n"
			itchat.send('%s: %s' % (msg['Type'], content), msg['FromUserName'])
			time.sleep(5)
			content = "看在我这么辛苦的份上，做我的女朋友吧!老婆。"
			itchat.send('%s: %s' % (msg['Type'], content), msg['FromUserName'])

			return True

		return False
	else:
		itchat.send('%s: %s' % (msg['Type'], content), msg['FromUserName'])

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
	try:
		for k, v in enumerate(day_desc):
			if desc.find(v) != -1:
				return len(day_desc) - k - 1
	except Exception:
		return 0
	return 0

def get_xy(msg):
	l = msg.split(' ')
	return int(l[1]), int(l[2])

def get_content(msg):
	idx = msg.find(' ')
	if idx > 0:
		return msg[idx + 1 : ]
	else:
		return ''

def get_user_city(msg):
	try:
		return dear_list[msg['User']['NickName']]["zone"], dear_list[msg['User']['NickName']]["area"]
	except Exception:
		return 101010300, "beijing/chaoyang-district"
	

def get_user_cons(msg):
	return dear_list[msg['User']['NickName']]["cons"]


def get_weather(msg, key, idx):
	city_code, area = get_user_city(msg)
	d = get_day_desc(msg['Text'])
	content = weather.get_weather_info(city_code, area, d)
	itchat.send('%s: %s' % (msg['Type'], content), msg['FromUserName'])


def get_more_weather(msg, key, idx):
	city_code, area = get_user_city(msg)
	d = get_day_desc(msg['Text'])
	content = weather.get_t_weather_info(city_code, d)
	itchat.send('%s: %s' % (msg['Type'], content), msg['FromUserName'])	


def get_one(msg, key, idx):
	content = weather.get_dictum_info()
	itchat.send('%s: %s' % (msg['Type'], content), msg['FromUserName'])


def get_cons(msg, key, idx):
	cons = get_user_cons(msg)
	content = weather.constellation(cons)
	itchat.send('%s: %s' % (msg['Type'], content), msg['FromUserName'])

def get_gua(msg, key, idx):
	time.sleep(5)
	content = u"无事不起卦!"
	itchat.send('%s: %s' % (msg['Type'], content), msg['FromUserName'])
	time.sleep(9)
	x, y = get_xy(msg['Text'])
	content = weather.get_gua(x, y)
	itchat.send('%s: %s' % (msg['Type'], content), msg['FromUserName'])


def get_somewhere(msg, key, idx):
	city_code, area = get_user_city(msg)
	d = get_day_desc(msg['Text'])
	content = weather.get_weather_info(city_code, area, d)
	itchat.send('%s: %s' % (msg['Type'], content), msg['FromUserName'])


def get_voice(msg, key, idx):
	content = get_content(msg['Text'])
	if len(content) > 0:
		tmp_file = word.word.text_to_voice(content)
		if tmp_file != '':
			# itchat.send_file(tmp_file, msg['FromUserName'])
			itchat.send_video(tmp_file, msg['FromUserName'])
			os.remove(tmp_file)




#
func_list = {}
func_list[u"我想看电影"] = find_movie
func_list[u"天气怎么样"] = get_weather
func_list[u"看天气"] = get_more_weather
func_list[u"天气好"] = get_more_weather
func_list[u"下雨"] = get_weather
func_list[u"One"] = get_one
func_list[u"运气怎么样"] = get_cons
func_list[u"运势怎么样"] = get_cons
func_list[u"运气好"] = get_cons
func_list[u"运势好"] = get_cons
func_list[u"起卦"] = get_gua
func_list[u"占卜"] = get_gua
func_list[u"算卦"] = get_gua
func_list[u"算命"] = get_gua
func_list[u"海淀区"] = get_somewhere
func_list[u"转语音"] = get_voice


def do_respons(request_word, msg):
	for key in func_list:
		idx = request_word.find(key)
		if idx == -1:
			continue
		ret = func_list[key](msg, key, idx)

		if ret != True:
			with open(err_log, "a") as f:
				f.write(request_word + "\n")


def notice_me(msg):
	user_info = itchat.search_friends(name='陈鹏')
	if len(user_info) > 0:
		user_name = user_info[0]['UserName']
		itchat.send_msg(msg, user_name)
		

@itchat.msg_register(['Recording'])
def voice_reply(msg):
	msg.download(msg.fileName)
	trans_msg = voice.translate(msg.fileName)
	msg['Text'] = trans_msg
	do_respons(trans_msg, msg)
	# print(trans_msg)
	# notice_me(trans_msg)

@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):

	do_respons(msg['Text'], msg)
	# itchat.send('%s: %s'%(msg['Type'], msg['FromUserName']), msg['FromUserName'])
	# if msg['FromUserName'] in dear_list:
	# print(msg['User'])
	# print(dear_list[msg['User']['NickName']])

	# for key in func_list:
	# 	idx = msg['Text'].find(key)
	# 	if idx == -1:
	# 		continue
	# 	ret = func_list[key](msg, key, idx)

	# 	if ret != True:
	# 		with open(err_log, "a") as f:
	# 			f.write(msg['Text'] + "\n")


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


def get_weather_info(name, info):
	# print(name)
	today_msg = weather.get_weather_info(info["zone"], info["area"])
	name_uuid = get_uuid_by_name(name)
	# print(name_uuid)
	itchat.send(today_msg, toUserName=name_uuid)


def get_weather_info_ex(name, info):

	name_uuid = get_uuid_by_name(name)

	today_msg = weather.get_dictum_info()
	itchat.send(today_msg, toUserName=name_uuid)

	today_msg = weather.get_weather_info(info["zone"], info["area"])
	itchat.send(today_msg, toUserName=name_uuid)

	today_msg = weather.constellation(info["cons"])
	itchat.send(today_msg, toUserName=name_uuid)



def get_nothing(name, info):
	# nonthing was happen, and I wonder
	pass


day_func = {}
day_func[0] = get_weather_info
day_func[1] = get_weather_info_ex
day_func[2] = get_nothing


def start_today_info(name, info):
	day_func[info["day_func"]](name, info)

# 济南 101120101 朝阳区 101010300
dear_list = {
	u"单文博" : {"hour":7, "minite":30, "zone":101010300, "wx":u"swb123aa", "day_func":2, "cons":"Leo", "area":"beijing/chaoyang-district"},
	u"陈鹏": {"hour": 0, "minite": 15, "zone": 101010300, "wx": u"yanxie1103", "day_func": 1, "cons": "Taurus", "area":"beijing/chaoyang-district"},
	u'王洋🐳' : {"hour":6, "minite":15, "zone":101010300, "wx":u"wxid_4070450704312", "day_func":2, "cons":"Leo", "area":"beijing/chaoyang-district"},
	u'Ada  阿哒哒💭': {"hour": 7, "minite": 30, "zone": 101021300, "wx": u"doria3159", "day_func": 1, "cons": "Leo", "area":"shanghai/nanhui-district"},
	u'孟小毛': {"hour": 7, "minite": 30, "zone": 101120101, "wx": u"mengyuan9059", "day_func": 1, "cons": "Aquarius", "area":"shandong/jinan"},
	u'小布丁': {"hour": 6, "minite": 15, "zone": 101010200, "wx": u"wxid_ezndyt05p2an21", "day_func": 2, "cons": "Capricorn", "area":"beijing/haidian-district"},
}

def run_daily_job():
	scheduler= BackgroundScheduler()
	for k in dear_list:
		arg= (k, dear_list[k])
		# scheduler.add_job(start_today_info, 'interval', seconds=20, args=arg)
		scheduler.add_job(start_today_info, 'cron', hour=dear_list[k]["hour"], minute=dear_list[k]["minite"], args=arg)
	scheduler.start()


#+
# itchat.auto_login(enableCmdQR=2)

run_daily_job()
itchat.auto_login(True)
itchat.run()
