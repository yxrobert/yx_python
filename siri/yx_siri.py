#! /usr/bin/env pythontools
#coding=utf-8


# import speech
import win32api
import os
import sys
import time
import win32con
import requests
import base64

 
cmd = {
    u'关机' : 'shutdown -s -t 1',
    u'重启' : 'shutdown -r',
    u'关闭浏览器' : 'taskkill /F /IM chrome.exe',
    u'关闭QQ' : 'taskkill /F /IM QQ.exe',
}


def func_quit():
    speech.say(u'已退出程序，感谢使用！')
    sys.exit()

def get_authorization():
    return base64.b64encode(bytes("wm:4qW6kbgK6F", encoding="ascii")).decode('ascii')

def func_download(): 
    session = requests.Session()

    headers = {
        'Authorization': 'Basic {}'.format(get_authorization()),
        'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.2.102 Yowser/2.5 Safari/537.36'
    }

    i1 = session.get(url="http://192.168.33.121/wm/", headers=headers)
    print(i1.text)



    # i2 = session.post(
    #     url="http://192.168.33.121/wm",
    #     data={'Credentials':'wm:4qW6kbgK6F'}
    # )
    # print(i2.text)

    # i3 = session.post(
    #     url="http://192.168.0.247/buyTicket",
    #     data={'email': 'lanhezhong@163.com'}
    # )
    # print(i3.text)


def go_loop():
    speech.say('语音识别已开启 ')
    while True:
        phrase = speech.input()
        if phrase in cmd_func.keys():
            speech.say('即将为您%s' % phrase)
            cmd_func[phrase]()
        elif phrase in cmd.keys():
            speech.say('即将为您%s' % phrase)
            os.system(cmd[phrase])
            speech.say('任务已完成！')
            if phrase == '放首歌':
                pass
        else:
            speech.say('I do not know what you say')
            pass

cmd_func = {
    u'下载' : func_download,
    u'退出程序' : func_quit,
}

def main():
    # go_loop()
    func_download()

if __name__ == '__main__':
    main()
