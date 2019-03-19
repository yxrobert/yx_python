#coding=utf8
import itchat
from itchat.content import *
import xml.etree.ElementTree as ET
from yx_requests import *


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
##自动回复的功能
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg['Text']
'''
# @itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
# def text_reply(msg):
#     itchat.send('%s: %s'%(msg['Type'],msg['Text']),msg['FromUserName'])
#
# @itchat.msg_register([PICTURE,RECORDING,ATTACHMENT,VIDEO])
# def download_files(msg):
#     msg['Text'](msg['FileName'])
#     return '@%s@%s'%({'Picture':'img','Video':'vid'}.get(msg['Type'],'fil'),msg['FileName'])
#
# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     itchat.add_friend(**msg['Text'])# 该操作将自动将好友的消息录入，不需要重载通讯录
#     itchat.send_msg('Nice to meet you!',msg['RecommendInfo']['UserName'])
#
# @itchat.msg_register(TEXT,isGroupChat=True)
# def text_reply(msg):
#     if msg['isAt']:
#         itchat.send(u'@%s\u2005I received: %s '%(msg['ActualNickName'],msg['Content']),msg['FromUserName'])


@itchat.msg_register(SHARING, isFriendChat=True, isGroupChat=True,isMpChat=True)
def share_repaly(msg):
    print msg['Content']

    root = ET.fromstring(msg['Content'])
    itchat.send(msg['Content'], toUserName='filehelper')

    app = root.find('appinfo')
    url = ''
    for child in app.getchildren():
        if child.text == '饿了么' or child.text == '美团':

            #
            appmsg = root.find('appmsg')
            for c in appmsg.getchildren():
                if c.tag == 'url':
                    url = c.text
            break

    # get
    print url
    ret = requests.get(url)
    print ret.json



itchat.auto_login(hotReload=True)
itchat.run()