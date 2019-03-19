#! /usr/bin/env python
# -*- coding: UTF-8 -*-


import itchat, time
import sys
import yx_web_search


reload(sys)
sys.setdefaultencoding('utf-8')

dear_list = [u'王洋', u'老妹3', u'老园']
key = u"我想看电影"

@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
    if msg['FromUserName'] in dear_list:
        idx = msg['Text'].find(key)
        name = msg['Text'][idx:].strip()
        if idx != -1:
            itchat.send('%s: %s'%(msg['Type'], msg['Text']), msg['FromUserName'])



itchat.auto_login()
itchat.run()