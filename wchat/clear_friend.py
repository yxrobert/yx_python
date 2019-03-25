#! /usr/bin/env python
# -*- coding: UTF-8 -*-


import itchat
import time
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

itchat.auto_login(hotReload=True) # 热加载

print(u'检测结果可能会引起不适。')
print(u'检测结果请在手机上查看，此处仅显示检测信息。')
print(u'消息被拒收为被拉黑， 需要发送验证信息为被删。')
print(u'没有结果就是好结果。')
print(u'检测1000位好友需要34分钟， 以此类推。')
print(u'为了你的账号安全着想，这个速度刚好。')
print(u'在程序运行期间请让程序保持运行，网络保持连接。')
print(u'请不要从手机端手动退出。')
input(u'按ENTER键继续...')


friends = itchat.get_friends(update=True)
lenght = len(friends)

for i in range(1, lenght):
	# 微信bug，用自己账户给所有好友发送"&#2403; &#2403; &#2403;"消息，当添加自己为好友时，只有自己能收到此信息，如果没添加自己为好友\
	# 没有人能收到此信息，笔者此刻日期为2019/1/6 8:30，到目前为止微信bug还没修复。
	# 所以迭代从除去自己后的第二位好友开始 range(1, lenght)。
	itchat.send("జ్ఞా", toUserName=friends[i]['UserName'])
	print(u'检测到第{i}位好友: {str(friends[i]["NickName"]).center(20, " ")}')
	# 发送信息速度过快会被微信检测到异常行为。
	time.sleep(2)

print(u'已检测完毕，请在手机端查看结果。')

itchat.run()