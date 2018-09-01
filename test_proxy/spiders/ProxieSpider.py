import scrapy
import os

class ProxieSpider(scrapy.Spider):

    name = "proxie"
    start_urls = ['http://www.baidu.com']

    def parse(self, response):
        print(response.body)
