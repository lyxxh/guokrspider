# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuokrspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    grouprange = scrapy.Field()
    groupname = scrapy.Field()
    issuper = scrapy.Field()
    members = scrapy.Field()
    link = scrapy.Field()
    status = scrapy.Field()
    update_time = scrapy.Field()
    pass
