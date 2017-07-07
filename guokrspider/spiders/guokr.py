# -*- coding: utf-8 -*-
import scrapy
from guokrspider.items import GuokrspiderItem


class GuokrSpider(scrapy.Spider):
    name = 'guokr'
    allowed_domains = ['guokr.com']
    start_urls = ['http://guokr.com/']

    def parse(self, response):
        item = GuokrspiderItem()
        item['title'] = response.xpath('/html/head/title/text()').extract()
        yield item
