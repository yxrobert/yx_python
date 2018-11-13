#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from lxml import etree
import requests
import sys

reload(sys)
sys.setdefaultencoding('gb2312')


def gbk_2_utf(_str):
    return _str.decode('gb2312').encode('UTF-8')


main_web = 'https://www.dytt8.net/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'Referer': 'http://www.ygdy8.net/html/gndy/dyzz/list_23_2.html'
}

new_movie_web = 'https://www.dytt8.net/html/gndy/dyzz/index.html'
movie_list = []
save_file = u'最新高分电影.txt'


def main():
    url = new_movie_web
    # 得到电影页代码
    reopens = requests.get(url, headers=headers)
    reopens.encoding = "gb2312"  # 手动指定字符编码为utf-8
    root = etree.HTML(reopens.text)  # 导入
    # root = etree.tostring(root, encoding="utf-8", xml_declaration=False)

    # res = root.xpath('//a/@class')    #取某节点所有某属性
    # res = root.xpath('//*[@class="ulink"]')   #取匹配的所有节点
    # res = root.xpath('//*[@class="ulink"]/@href')     #取匹配的所有节点的某属性
    res = root.xpath('//*[@class="ulink"]')
    # res = root.xpath('//*[@class="ulink"]/@*') #匹配所有属性
    # res = root.xpath('//*//[@class="ulink"]')
    # print type(res)

    #
    movie_name = ''
    movie_adress = ''

    str_grade = u'豆瓣评分　'
    demand = float('7.5')
    for i in res:
        movie_url = main_web + i.attrib['href']
        print movie_url
        movie_name = i.text
        req = requests.get(movie_url, headers=headers)
        req.encoding = "gb2312"
        s = req.text.find(str_grade)
        if s != -1:
            s += len(str_grade)
            e = req.text[s:].find('/')
            # print req.text[s: s + e]
            val = float(req.text[s: s + e])
            # print req.text
            print val

            if val > demand:
                # print req.text[s+e:]
                rt = etree.HTML(req.text)
                # result = rt.xpath('//td[1]/a[1]/@href')
                # 查找第一个td包含的a， 并且a的属性href中包含‘ftp’
                result = rt.xpath('//td[1]/a[contains(@href, "ftp")]')
                print type(result), result
                for j in result:
                    # print j.attrib['href']
                    movie_adress = j.attrib['href']
                    movie_list.append([movie_name, movie_adress])
                # break

        # print i.attrib['href'], i.text

    with open(save_file, 'w') as f:
        for i in movie_list:
            f.write(i[0] + '\n')
            f.write(i[1] + '\n\n')
        f.close()


if __name__ == "__main__":
    main()
