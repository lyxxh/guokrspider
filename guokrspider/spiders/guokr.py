# -*- coding: utf-8 -*-
import scrapy
import re
import time
from guokrspider.items import GuokrspiderItem
from scrapy import Request
from scrapy.conf import settings


class GuokrSpider(scrapy.Spider):
    name = 'guokr'
    allowed_domains = ['guokr.com']
    start_urls = ['http://www.guokr.com/group/rank/popular/']
    host = 'http://www.guokr.com'
    time_now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    cookie = settings['COOKIE']
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'www.guokr.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/60.0.3112.90 Safari/537.36 '
    }

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], headers=self.headers, cookies=self.cookie)  # 这里带着cookie发出请求

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
