# -*- coding: utf-8 -*-
import scrapy
from HYX.items import HyxItem

class GzrSpider(scrapy.Spider):
    name = 'GZR1'
    allowed_domains = ['biqudao.com']
    start_urls = ['https://www.biqudao.com/bqge1618/']

    def parse(self, response):
        item = HyxItem()
        for box in response.xpath("//*[@id='list']"):
            item['title'] = box.xpath(".//a/text()").extract()[0].strip()
            item['url'] = 'http://www.biqudao.com' + box.xpath('.//@href').extract()[0]
            yield item

        url = response.xpath("//a/@href").extract()
        if url :
            page = 'http://www.biqudao.com' + url[0]
            yield scrapy.Request(page, callback=self.parse)