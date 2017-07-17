# -*- coding: utf-8 -*-
import scrapy
import re
from guokrspider.items import GuokrspiderItem


class GuokrSpider(scrapy.Spider):
    name = 'guokr'
    allowed_domains = ['guokr.com']
    start_urls = ['http://www.guokr.com/group/rank/popular/']

    def parse(self, response):
        # rangeall = soap.find_all('span', class_=['rank-num-top', 'rank-num'])
        # for id in rangeall:
        # item['grouprange'] = id.string
        # yield item
        # cs = soap.find('ul', class_="ranks")
        item = GuokrspiderItem()
        group_all = response.xpath('//ul[@class="ranks"]')
        group_list = group_all.xpath('./li')
        for group in group_list:
            item['grouprange'] = group.xpath('//span[starts-with(@class, "rank-num")]').extract()
            yield item
