# -*- coding: utf-8 -*-
import requests
import time
import datetime
import sys
import logging
import urllib
import json
reload(sys)
sys.setdefaultencoding('utf8')
 
def start():
    bomb_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'cookie': 'pt_key=******; pt_pin=********;',
        'User-Agent': 'jdapp;'
    }
    bomb_body = 'functionId=cakebaker_pk_getCakeBomb&body={}&client=wh5&clientVersion=1.0.0'
    bomb_state = requests.post('https://api.m.jd.com/client.action?functionId=cakebaker_pk_getCakeBomb', data=bomb_body, headers=bomb_headers).text
    logging.warning('炸弹状态:'+bomb_state)
    if 'timeStart' in bomb_state:
        bomb_state_json = json.loads(bomb_state)
        d_time = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d")+bomb_state_json["data"]["result"]["timeStart"], '%Y-%m-%d%H:%M')+datetime.timedelta(hours=-8)
        logging.warning('距离开始时间还有: '+str((d_time-datetime.datetime.now()).seconds)+'秒')
        if  (d_time-datetime.datetime.now()).seconds <= 60:
            while datetime.datetime.now() < d_time+datetime.timedelta(seconds=-2):
                logging.warning(datetime.datetime.now()+datetime.timedelta(hours=8))
                time.sleep(1)
            while datetime.datetime.now() > d_time+datetime.timedelta(seconds=-2) and datetime.datetime.now() < d_time+datetime.timedelta(seconds=2):
                bomb = requests.post('https://api.m.jd.com/client.action?functionId=cakebaker_pk_getCakeBomb', data=bomb_body, headers=bomb_headers).text
                logging.warning(datetime.datetime.now()+datetime.timedelta(hours=8))
                logging.warning('京东炸弹:'+bomb)
                if '成功' in bomb:
                    s = json.loads(bomb)
                    msg = urllib.quote(str(s["data"]["result"]["tip"]))
                    groupLevel = urllib.quote(str(s["data"]["result"]["groupLevel"]))
                    opponentLevel = urllib.quote(str(s["data"]["result"]["opponentLevel"]))
                    requests.get('https:# coding: utf-8
import requests
import time
import datetime
import sys
import logging
import urllib
import json
reload(sys)
sys.setdefaultencoding('utf8')
 
def start():
    bomb_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'cookie': 'pt_key=******; pt_pin=********;',
        'User-Agent': 'jdapp;'
    }
    bomb_body = 'functionId=cakebaker_pk_getCakeBomb&body={}&client=wh5&clientVersion=1.0.0'
    bomb_state = requests.post('https://api.m.jd.com/client.action?functionId=cakebaker_pk_getCakeBomb', data=bomb_body, headers=bomb_headers).text
    logging.warning('炸弹状态:'+bomb_state)
    if 'timeStart' in bomb_state:
        bomb_state_json = json.loads(bomb_state)
        d_time = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d")+bomb_state_json["data"]["result"]["timeStart"], '%Y-%m-%d%H:%M')+datetime.timedelta(hours=-8)
        logging.warning('距离开始时间还有: '+str((d_time-datetime.datetime.now()).seconds)+'秒')
        if  (d_time-datetime.datetime.now()).seconds <= 60:
            while datetime.datetime.now() < d_time+datetime.timedelta(seconds=-2):
                logging.warning(datetime.datetime.now()+datetime.timedelta(hours=8))
                time.sleep(1)
            while datetime.datetime.now() > d_time+datetime.timedelta(seconds=-2) and datetime.datetime.now() < d_time+datetime.timedelta(seconds=2):
                bomb = requests.post('https://api.m.jd.com/client.action?functionId=cakebaker_pk_getCakeBomb', data=bomb_body, headers=bomb_headers).text
                logging.warning(datetime.datetime.now()+datetime.timedelta(hours=8))
                logging.warning('京东炸弹:'+bomb)
                if '成功' in bomb:
                    s = json.loads(bomb)
                    msg = urllib.quote(str(s["data"]["result"]["tip"]))
                    groupLevel = urllib.quote(str(s["data"]["result"]["groupLevel"]))
                    opponentLevel = urllib.quote(str(s["data"]["result"]["opponentLevel"]))
                    requests.get('https://sc.ftqq.com/*********.send?text='+groupLevel+'+VS+'+opponentLevel)
                    logging.warning('成功')
                    break
        else:
            logging.warning(datetime.datetime.now()+datetime.timedelta(hours=8))
            logging.warning('非活动时间！')
    else:
        logging.warning(datetime.datetime.now()+datetime.timedelta(hours=8))
        logging.warning('非活动时间！')
 
def main_handler(event, context):
    return start()
 
 
if __name__ == '__main__':
    start()//sc.ftqq.com/*********.send?text='+groupLevel+'+VS+'+opponentLevel)
                    logging.warning('成功')
                    break
        else:
            logging.warning(datetime.datetime.now()+datetime.timedelta(hours=8))
            logging.warning('非活动时间！')
    else:
        logging.warning(datetime.datetime.now()+datetime.timedelta(hours=8))
        logging.warning('非活动时间！')
 
def main_handler(event, context):
    return start()
 
 
if __name__ == '__main__':
    start()