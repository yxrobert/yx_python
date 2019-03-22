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
movie_list = {u"小偷家族":"magnet:?xt=urn:btih:047FCD07C11D153A8B7A724D4C253BF373AEF115"}
err_log = "err.log"


#
def find_movie(msg, key, idx):
	name = msg['Text'][idx + len(key):].strip()
	print(name)
	content = 'Good 稍等一下 亲爱的 %s 马上送达' % name
	itchat.send('%s: %s'%(msg['Type'], content), msg['FromUserName'])

	content = movie.get_movie(name)
	if len(content) < 5:
		content = '没有找到资源哦，没关系，可以带你去电影院去看！'
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

# 
func_list = {}
func_list[u"我想看电影"] = find_movie


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):

	# itchat.send('%s: %s'%(msg['Type'], msg['FromUserName']), msg['FromUserName'])
	# if msg['FromUserName'] in dear_list:

	for key in func_list:
		idx = msg['Text'].find(key)
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


def start_today_info(name, city_code):
	print(name)
	today_msg = weather.get_weather_info(city_code)
	name_uuid = get_uuid_by_name(name)
	print(name_uuid)

	itchat.send(today_msg, toUserName=name_uuid)

dear_list = {
	u"单文博" : [13, 2, 101010300, u"swb123aa"],
	u"Lifecoach🐳": [13, 12 101010300, u"yanxie1103"],
	# u"王洋" : [6, 15, 101010300, u"wxid_4070450704312"],
}


# 
def run_daily_job():
	scheduler = BackgroundScheduler()
	for k in dear_list:
		arg = (dear_list[k][3], dear_list[k][2],)
		scheduler.add_job(start_today_info, 'interval', seconds=20, args=(k,dear_list[k][2],))
		# scheduler.add_job(start_today_info, 'cron', hour=dear_list[k][0], minute=dear_list[k][1], args=arg)
	scheduler.start()


# 
#itchat.auto_login(enableCmdQR=2)

run_daily_job()
itchat.auto_login(True)
itchat.run()
