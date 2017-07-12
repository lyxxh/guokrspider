# -*- coding: utf-8 -*-
import scrapy
import guokrspider.items


class GuokrSpider(scrapy.Spider):
    name = 'guokr'
    allowed_domains = ['guokr.com']
    start_urls = ['http://guokr.com/']

    def parse(self, response):
        item = guokrspider.items.GuokrspiderItem()
        item['title'] = response.xpath('/html/head/title/text()').extract()
        item['description'] = response.xpath('/html/head/@content[@name="Description"]').extract()
        yield item
