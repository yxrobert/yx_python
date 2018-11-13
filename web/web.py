#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from lxml import etree
import requests

ht = 'http://www.ygdy8.net/'
# 请求第一页数据
#url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'Referer': 'http://www.ygdy8.net/html/gndy/dyzz/list_23_2.html'
}
move = []
# 得到前七页链接q
base_html = "http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html"
for x in range(1, 2):
    url = base_html.format(x)
    # 得到电影页代码
    resopen = requests.get(url, headers=headers)
    html = resopen.text
    # html = resopen.content.decode('gbk')
    # 得到电影链接
    htmls = etree.HTML(html)  # 导入
    D_url = htmls.xpath("//table[@class='tbspan']//a/@href")
    for D in D_url:
        DY_url = ht + D
        movies = {}
        # 以获取前几页所有下载页面链接
        resopens = requests.get(DY_url, headers=headers)
        html_DY = resopens.content.decode('gbk')
        html_DY_get = etree.HTML(html_DY)
        title = html_DY_get.xpath(
            "//div[@class='title_all']//font[@color='#07519a']/text()")
        movies['title'] = title
        img = html_DY_get.xpath("//div[@id='Zoom']//img/@src")
        img_hb = img[0]
        # img_jq = img[1]
        movies['海报'] = img_hb
        # movies['剧情图'] = img_jq
        get_texts = html_DY_get.xpath("//div[@id='Zoom']//text()")
        for get_text in get_texts:
            print get_text
            if get_text.startswith(u'◎年　　代'):
                get_text = get_text.replace(u'◎年　　代', '')
                movies['年代'] = get_text
            elif get_text.startswith(u'◎类　　别'):
                get_text = get_text.replace(u'◎类　　别', '')
                movies['类别'] = get_text
            elif get_text.startswith(u'◎主　　演'):
                get_text = get_text.replace(u'◎主　　演', '')
                movies['主演'] = get_text
            elif get_text.startswith(u'◎简　　介'):
                get_text = get_text.replace(u'◎简　　介', '')
                movies['简介'] = get_text
        # print(movies)
        move.append(movies)
        # print(move)
        movie = str(move)
        break
with open('电影天堂.txt', 'w')as fp:
    fp.write(movie)
