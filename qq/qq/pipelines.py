# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class QqPipeline(object):
    def process_item(self, item, spider):
        return item


class QQPipeline(object):


    def __init__(self):
        self.file = open('qq.json', 'wb')


    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(content)

    def close_spider(self, spider):
        self.file.close()
