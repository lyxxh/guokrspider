# -*- coding: utf-8 -*-
import scrapy
from guokrspider.items import GuokrspiderItem


class GuokrSpider(scrapy.Spider):
    name = 'guokr'
    allowed_domains = ['guokr.com']
    start_urls = ['http://www.guokr.com/group/rank/popular/']

    def parse(self, response):
        item = GuokrspiderItem()
        group_all = response.xpath('//ul[@class="ranks"]')
        group_list = group_all.xpath('./li')
        for group in group_list:
            item['grouprange'] = group.xpath('.//span[starts-with(@class, "rank-num")]/text()').extract_first()
            item['groupname'] = group.xpath('./span/a[@target="_blank"]/text()').extract_first()
            item['link'] = group.xpath('./span/a[@target="_blank"]/@href').extract_first()
            yield item
