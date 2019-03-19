#! /usr/bin/env python
# -*- coding: UTF-8 -*-


import itchat, time
import sys
import yx_web_search as yx


reload(sys)
sys.setdefaultencoding('utf-8')

dear_list = [u'王洋', u'老妹3', u'老园', u'美好']
key = u"我想看电影"

@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):

	# itchat.send('%s: %s'%(msg['Type'], msg['FromUserName']), msg['FromUserName'])
	# if msg['FromUserName'] in dear_list:

	idx = msg['Text'].find(key)
	# content = 'good 进入第二步了 %d' % idx
	# itchat.send('%s: %s'%(msg['Type'], content), msg['FromUserName'])

	if idx != -1:
		name = msg['Text'][idx + len(key):].strip()
		print name
		content = 'Good 稍等一下 亲爱的 %s 马上送达' % name
		itchat.send('%s: %s'%(msg['Type'], content), msg['FromUserName'])

		content = yx.get_movie(name)
		if len(content) < 5:
			content = '没有找到资源哦，没关系，可以带你去电影院去看！'
			itchat.send('%s: %s'%(msg['Type'], content), msg['FromUserName'])
		else:
			itchat.send('%s: %s'%(msg['Type'], content), msg['FromUserName'])
		



itchat.auto_login(True)
itchat.run()