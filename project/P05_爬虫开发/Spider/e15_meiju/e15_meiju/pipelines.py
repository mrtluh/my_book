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

    '''
    此方法必须被实现
    用来具体处理item内容
    且必须返回一个item
    '''

    def __init__(self):
        print("init ... meiju.json")
        self.file = open('meiju.json', 'wb')

    def process_item(self, item, spider):
        '''
        此案例只是把item值打印出来
        :param item:
        :param spider:
        :return:
        '''
        print(item['name'])
        with open('meiju.json', 'a') as f:
            json.dump(dict(item), f)

        return item
