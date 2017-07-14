# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
from guokrspider.items import GuokrspiderItem


class GuokrSpider(scrapy.Spider):
    name = 'guokr'
    allowed_domains = ['guokr.com']
    start_urls = ['http://www.guokr.com/group/rank/popular/']

    def parse(self, response):
        soap = BeautifulSoup(response.text, 'lxml')
        item = GuokrspiderItem()
        rangeall = soap.find_all('span', class_=re.compile(r'rank-num*'))
        for id in rangeall:
            item['grouprange'] = id.string
            yield item
