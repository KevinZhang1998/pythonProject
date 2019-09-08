# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient


class HotelPipeline(object):
    collection_name = 'quote'

    def __init__(self, mongo_host, mongo_port, mongo_database):
        self.mongo_host = mongo_host
        self.mongo_port = mongo_port
        self.mongo_database = mongo_database

    def open_spider(self, spider):
        self.client = MongoClient(host=self.mongo_host, port=self.mongo_port)
        self.database = self.client[self.mongo_database]
        self.collection = self.database[self.collection_name]

    def close_spider(self, spider):
        self.client.close()

    @classmethod
    def from_settings(cls, settings):
        return cls(
            settings.get('MONGO_HOST'),
            int(settings.get('MONGO_PORT')),
            settings.get('MONGO_DATABASE')
        )

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
