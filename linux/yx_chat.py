#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import yx_search_movie as movie
import yx_weather as weather
from imp import reload
import sys
import itchat, time
from apscheduler.schedulers.blocking import BlockingScheduler


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
def get_uuid(name):
	friends = itchat.search_friends(name)
	if not friends:
		print('昵称错误')
		return ""
	else:
		name_uuid = friends[0].get('UserName')
		return name_uuid

def start_today_info(name, city_code):
	print(name)
	today_msg = weather.get_weather_info(city_code)
	name_uuid = get_uuid(name)
	print(name_uuid)

	itchat.send(today_msg, toUserName=name_uuid)

dear_list = {
	u"祖拉" : [9, 30, 101010300],
	# u"Lifecoach" : [9, 30, 101010300],
	# u"王洋" : [6, 15, 101010300],
}


# 
def run_daily_job():
	scheduler = BlockingScheduler()
	for k in dear_list:
		print(k)
		scheduler.add_job(start_today_info, 'interval', seconds=20, args=(k,dear_list[k][2],))
		# scheduler.add_job(start_today_info, 'cron', hour=dear_list[k][0], minute=dear_list[k][1], args=(k,dear_list[k][2],))
	# 每隔2分钟发送一条数据用于测试。
	# scheduler.add_job(self.start_today_info, 'interval', seconds=120)
	scheduler.start()
	print("scheduler.start")


# 
#itchat.auto_login(enableCmdQR=2)

run_daily_job()
itchat.auto_login(True)
itchat.run()
print("itchat.run")
