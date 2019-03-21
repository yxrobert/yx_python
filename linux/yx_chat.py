#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import yx_search_movie
from imp import reload
import sys
import itchat, time


reload(sys)


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
    itchat.send('%s: %s'%(msg['Type'], msg['Text']), msg['FromUserName'])

#itchat.auto_login(enableCmdQR=2)
itchat.auto_login(True)
itchat.run()
