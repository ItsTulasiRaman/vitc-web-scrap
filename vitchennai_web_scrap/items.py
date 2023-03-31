# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VitchennaiWebScrapItem(scrapy.Item):
    # define the fields for your item here like:
    faculty_name = scrapy.Field()
    position = scrapy.Field()
    email = scrapy.Field()
