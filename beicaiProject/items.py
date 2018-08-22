# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BeicaiprojectItem(scrapy.Item):
    姓名 = scrapy.Field()

    危险等级 = scrapy.Field()

    逾期金额 = scrapy.Field()

    出生地址 = scrapy.Field()

    同意 = scrapy.Field()

    不同意 = scrapy.Field()

