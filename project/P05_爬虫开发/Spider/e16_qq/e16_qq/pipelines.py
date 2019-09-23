# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class E16QqPipeline(object):
    def process_item(self, item, spider):
        return item


class QQPipeline(object):
    '''
    假设数据需要写入文件
    那么在什么时候关闭，打开文件
    '''

    def __init__(self):
        self.file = open('qq.json', 'wb')

    def process_item(self, item, spider):
        # item可以直接转换成字典
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(conent)

        return item


    def close_spider(self, spider):
        self.file.close()