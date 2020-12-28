# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CarItem(scrapy.Item):
    car = scrapy.Field()
    price = scrapy.Field()
    car_url = scrapy.Field()
    car_model = scrapy.Field()
    brand = scrapy.Field()
    brand_url = scrapy.Field()