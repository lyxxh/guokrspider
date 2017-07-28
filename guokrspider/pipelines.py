# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GuokrspiderPipeline(object):
    def process_item(self, item, spider):
        print(item['grouprange'], end=' ')
        print(item['groupname'], end=' ')
        print(item['issuper'], end=' ')
        print(item['members'], end=' ')
        print(item['link'], end=' ')
        print(item['status'])
        return item
