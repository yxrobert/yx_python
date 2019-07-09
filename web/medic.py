#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import json

reload(sys)
sys.setdefaultencoding('UTF-8')

url = [
'''
curl 'http://12333.qingdao.gov.cn/grcx2/public/f10030110/queryYlbxMlcx.action' -H $'Cookie: WMONID=Q0lPClufwuj; cookie=36925438; _gscu_1494205420=62309306bb7sxa91; _gscbrs_1494205420=1; JSESSIONID=v-rBRhQ9MWzOr5u2AkyUSMHTHe75q-EBVoJg-IJP9SZyKvm1glXT\u21782152053' -H 'Origin: http://12333.qingdao.gov.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/plain, */*; q=0.01' -H 'Referer: http://12333.qingdao.gov.cn/grcx2/public/f10030110/index.action?resourceId=10030110&_t=873404&_winid=w7561' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'cxtj1=1&cxtj2=&cxtj3=1&pageIndex=%d&pageSize=100&sortField=&sortOrder=' --compressed --insecure
''',

'''
curl 'http://12333.qingdao.gov.cn/grcx2/public/f10030111/queryDdyyyfcx.action' -H $'Cookie: WMONID=Q0lPClufwuj; cookie=36925438; _gscu_1494205420=62309306bb7sxa91; _gscbrs_1494205420=1; JSESSIONID=LJnVuSIDFFNrgMnTHQrKm_O3v9HlQ2qWzh5_VjX5pHw0rA09yKJ7\u21782152053; _gscs_1494205420=t62658556o3dhle91|pv:1' -H 'Origin: http://12333.qingdao.gov.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/plain, */*; q=0.01' -H 'Referer: http://12333.qingdao.gov.cn/grcx2/public/f10030111/index.action?resourceId=10030111&_t=620136&_winid=w9656' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'pageIndex=%d&pageSize=100&sortField=&sortOrder=' --compressed --insecure
''',

'''
curl 'http://12333.qingdao.gov.cn/grcx2/public/f10030112/queryZlxmfwsscx.action' -H $'Cookie: WMONID=Q0lPClufwuj; cookie=36925438; _gscu_1494205420=62309306bb7sxa91; _gscbrs_1494205420=1; JSESSIONID=LJnVuSIDFFNrgMnTHQrKm_O3v9HlQ2qWzh5_VjX5pHw0rA09yKJ7\u21782152053; _gscs_1494205420=t62658556o3dhle91|pv:1' -H 'Origin: http://12333.qingdao.gov.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/plain, */*; q=0.01' -H 'Referer: http://12333.qingdao.gov.cn/grcx2/public/f10030112/index.action?resourceId=10030112&_t=944017&_winid=w9656' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'cxtj1=&cxtj2=1&pageIndex=%d&pageSize=100&sortField=&sortOrder=' --compressed --insecure
''',

'''
curl "http://12333.qingdao.gov.cn/grcx2/public/f10030113/queryBzmlcx.action" -H "Cookie: WMONID=Q0lPClufwuj; cookie=36925438; _gscu_1494205420=62309306bb7sxa91; _gscbrs_1494205420=1; JSESSIONID=VlbQZ1afC9bll9JeLOhxcrIFBt-4sXawEqgQrQlOFQCNewncpjZp^!782152053; _gscs_1494205420=t62572183zirpgj91^|pv:2" -H "Origin: http://12333.qingdao.gov.cn" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: zh-CN,zh;q=0.9,en;q=0.8" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: text/plain, */*; q=0.01" -H "Referer: http://12333.qingdao.gov.cn/grcx2/public/f10030113/index.action?resourceId=10030113^&_t=127935^&_winid=w4911" -H "X-Requested-With: XMLHttpRequest" -H "Connection: keep-alive" --data "cxtj1=^&cxtj2=1^&pageIndex=%d^&pageSize=100^&sortField=^&sortOrder=" --compressed --insecure
''',

'''
curl "http://12333.qingdao.gov.cn/grcx2/public/f10030116/queryYbhccx.action" -H "Cookie: WMONID=Q0lPClufwuj; cookie=36925438; _gscu_1494205420=62309306bb7sxa91; _gscbrs_1494205420=1; JSESSIONID=VlbQZ1afC9bll9JeLOhxcrIFBt-4sXawEqgQrQlOFQCNewncpjZp^!782152053; _gscs_1494205420=t62572183zirpgj91^|pv:2" -H "Origin: http://12333.qingdao.gov.cn" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: zh-CN,zh;q=0.9,en;q=0.8" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: text/plain, */*; q=0.01" -H "Referer: http://12333.qingdao.gov.cn/grcx2/public/f10030116/index.action?resourceId=10030116^&_t=350568^&_winid=w4911" -H "X-Requested-With: XMLHttpRequest" -H "Connection: keep-alive" --data "cxtj1=^&cxtj2=^&pageIndex=%d^&pageSize=100^&sortField=^&sortOrder=" --compressed --insecure
''',

'''
curl "http://12333.qingdao.gov.cn/grcx2/public/f10030120/queryCareList.action" -H "Cookie: WMONID=Q0lPClufwuj; cookie=36925438; _gscu_1494205420=62309306bb7sxa91; _gscbrs_1494205420=1; JSESSIONID=VlbQZ1afC9bll9JeLOhxcrIFBt-4sXawEqgQrQlOFQCNewncpjZp^!782152053; _gscs_1494205420=t62572183zirpgj91^|pv:2" -H "Origin: http://12333.qingdao.gov.cn" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: zh-CN,zh;q=0.9,en;q=0.8" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: text/plain, */*; q=0.01" -H "Referer: http://12333.qingdao.gov.cn/grcx2/public/f10030120/index.action?resourceId=10030120^&_t=633249^&_winid=w4911" -H "X-Requested-With: XMLHttpRequest" -H "Connection: keep-alive" --data "cxtj1=^&cxtj2=^&pageIndex=%d^&pageSize=100^&sortField=^&sortOrder=" --compressed --insecure
''',
]

save_name = [
"medic",
"hospital",
"service",
"ill",
"meterial",
"notice",
]
count = [375, 222, 203, 391, 3, 9]

#
# def unicode_convert(input):
# 	if isinstance(input, dict):
# 		return {unicode_convert(key): unicode_convert(value) for key, value in input.iteritems()}
# 	elif isinstance(input, list):
# 		return [unicode_convert(element) for element in input]
# 	elif isinstance(input, unicode):
# 		return input.encode('utf-8')
# 	else:
# 		return input


def down_data(f, url, page):
	cmd = url % page
	output = os.popen(cmd)
	ret = output.read()

	data = json.loads(ret)
	for i in data['data']:
		if isinstance(i, dict):
			for k, v in i.items():
				# print v
				f.write(v)
				f.write('\t')
		else:
			print(v)
		f.write('\n')

def main():

	if len(sys.argv) > 1:
		idx = int(sys.argv[1])
		with open(save_name[idx] + ".tsv", 'w') as f:	
				for i in range(0, count[idx]):
					down_data(f, url[idx], i)
	else:
		for idx in range(len(url)):
			with open(save_name[idx] + ".tsv", 'w') as f:	
				for i in range(0, count[idx]):
					down_data(f, url[idx], i)

if __name__ == "__main__":
	main()
