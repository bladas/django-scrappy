from time import sleep

import scrapy

from scrap.items import CarItem

from utils import time_of_function


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://auto.ria.com/uk/legkovie-catalog/']

    @time_of_function
    def parse(self, response):
        all_brands = response.css('a.item-brands')
        for brand in all_brands:
            brand_url = brand.css('::attr(href)').extract()[0]
            yield scrapy.Request(brand_url, callback=self.parse_models)

    def parse_models(self, response):
        cars = response.css('a.address::attr(href)').extract()
        for car_url in cars:
            yield scrapy.Request(car_url,callback=self.parse_car)
        next_page = response.css('a.page-link.js-next::attr(href)').extract_first()
        if 'https' in next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse_models)

    def parse_car(self,response):
        car_info = response.xpath('//span[@itemprop = "title"]/text()').getall()
        car_name = response.css('h1::attr(title)').extract_first()
        price = response.xpath('//div[@class = "price_value"]//strong/text()').get()
        if len(car_info) != 0:
            car = CarItem()
            car['brand'] = car_info[3]
            car['car_model'] = car_info[4]
            car['car_url'] = response.url
            car['car'] = car_name
            car['price'] = price
            yield car