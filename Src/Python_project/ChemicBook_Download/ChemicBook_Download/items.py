# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChemicbookDownloadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mol_url_list = scrapy.Field()
    gif_url_list= scrapy.Field()
