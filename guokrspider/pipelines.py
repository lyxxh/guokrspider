# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GuokrspiderPipeline(object):
    def process_item(self, item, spider):
        print(item['title'])
        print(item['description'])
        return item
