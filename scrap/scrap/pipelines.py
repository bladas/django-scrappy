import os
import re
import json
import logging
import psycopg2
import psycopg2.extras
import scrapy
import django

from utils import time_of_function

django.setup()
# from douban.definitions import CONFIG_DIR
# from scrapy.pipelines.images import ImagesPipeline
from connect.models import Car, CarModel, Brand


class ScrapySpiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "myspider":
            brand, _ = Brand.objects.get_or_create(name=item.get('brand'))
            car_model, _ = CarModel.objects.get_or_create(car_model_name=item.get('car_model'), brand=brand)
            CarModel.objects.get_or_create(car_model=car_model, car_url = item.get('car_url'),price = item.get('price'), car_name = item.get('car'))
            # self.list_of_cars.append(car)
            # if len(self.list_of_cars) == 200:
            #     Car.objects.bulk_create(self.list_of_cars)
            #     self.list_of_cars = []
            # if len(self.list_of_cars) != 0:
            #     Car.objects.bulk_create(self.list_of_cars)
            #     self.list_of_cars = []
        return item

