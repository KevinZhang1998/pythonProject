# -*- coding: utf-8 -*-

# Scrapy settings for hotel project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'hotel'

SPIDER_MODULES = ['hotel.spiders']
NEWSPIDER_MODULE = 'hotel.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ' \
             '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

ITEM_PIPELINES = {
    'hotel.pipelines.HotelPipeline': 300,
}
MONGO_HOST = '127.0.0.1'
MONGO_PORT = '27017'
MONGO_DATABASE = 'QUOTES'
