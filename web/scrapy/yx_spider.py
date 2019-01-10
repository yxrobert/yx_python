# -*- coding: utf-8 -*-
import scrapy


class YxSpiderSpider(scrapy.Spider):
    name = 'yx_spider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        yield url
