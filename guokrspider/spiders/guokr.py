# -*- coding: utf-8 -*-
import scrapy
import re
import time
from guokrspider.items import GuokrspiderItem
from scrapy import Request


class GuokrSpider(scrapy.Spider):
    name = 'guokr'
    allowed_domains = ['guokr.com']
    start_urls = ['http://www.guokr.com/group/rank/popular/']
    host = 'http://www.guokr.com'
    time_now = time.strftime("%Y%m%d%H%M%S", time.localtime())

    def parse(self, response):
        item = GuokrspiderItem()
        group_all = response.xpath('//ul[@class="ranks"]')
        group_list = group_all.xpath('./li')
        for group in group_list:
            item['grouprange'] = group.xpath('.//span[starts-with(@class, "rank-num")]/text()').extract_first()
            item['groupname'] = group.xpath('./span/a[@target="_blank"]/text()').extract_first()
            super = group.xpath('./span/a[@class="gicon-super"]/@title').extract_first()
            if super:
                item['issuper'] = 1
            else:
                item['issuper'] = 0
            member = re.findall(r"[0-9]{1,7}", group.xpath('.//span[@class="group-members"]/text()').extract_first())
            item['members'] = member[0]
            item['link'] = group.xpath('./span/a[@target="_blank"]/@href').extract_first()
            status = re.findall(r"[\u4e00-\u9fa5]{1,3}",
                                group.xpath('./span[@class="rank-right"]/a/span/text()').extract_first())
            if status:
                item['status'] = status[0]
            else:
                item['status'] = group.xpath('./span[@class="rank-right"]/a/text()').extract_first()
            item['update_time'] = self.time_now
            yield item

        next_page = response.xpath('//li[a="下一页"]/a/@href').extract_first()
        if next_page:
            yield Request(self.host + next_page, callback=self.parse)
