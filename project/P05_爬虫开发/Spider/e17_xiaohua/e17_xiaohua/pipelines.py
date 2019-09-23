# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class E17XiaohuaPipeline(object):
    def process_item(self, item, spider):
        return item


class XiaohuaPipeline(object):

    def __init__(self):
        self.file = open('xiaohua.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        str = json.dumps(dict(item), ensure_ascii=False)

        str = str + '\n'
        self.file.write(str)


    def close_spider(self, spider):
        self.file.close()