# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
import pymysql
from scrapy import log


# 保存到mongodb
class GuokrspiderPipeline(object):
    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MONGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄

    def process_item(self, item, spider):
        # print(item['grouprange'], end=' ')
        # print(item['groupname'], end=' ')
        # print(item['issuper'], end=' ')
        # print(item['members'], end=' ')
        # print(item['link'], end=' ')
        # print(item['status'])
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        return item


# 保存到mysql
class GuokrspiderMysqlPipeline(object):
    def __init__(self):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            port=settings['MYSQL_PORT'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8'
        )
        self.conn = pymysql.connect(**dbargs)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    """insert into guokr_group_range(group_range,group_name,is_super,members,link,status,update_time)
         values (%s,%s,%s,%s,%s,%s,%s)""",
                   (item['grouprange'],
                    item['groupname'],
                    item['issuper'],
                    item['members'],
                    item['link'],
                    item['status'],
                    item['update_time']))
                self.conn.commit()
        except:
            self.conn.rollback()
        return item
