# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PubchemicDownloadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 获取下载链接地址
    mol_url = scrapy.Field()
    png_url = scrapy.Field()
    # 传递当前游标
    current_num=scrapy.Field()
    # 传递需要后面去命名
    cas=scrapy.Field()
