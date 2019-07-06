# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class E15MeijuPipeline(object):
    def process_item(self, item, spider):
        return item


class MeijuPipeline(object):

    # def __init__(self):
    #     self.file = open('meiju.json', 'wb')

    def process_item(self, item, spider):
        print(item['name'])
        print(item['href'])
        # print(item['tv'])
        # with open('meiju.json', 'a') as f:
        #     json.dump(dict(item), f)
        return item
