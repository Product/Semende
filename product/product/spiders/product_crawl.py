# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ProductCrawlSpider(CrawlSpider):
    name = 'product_crawl'
    allowed_domains = ['http://kor.lottedfs.com/']
    start_urls = ['http://kor.lottedfs.com/kr/product/productDetail?prdNo=10001860657&dispShopNo1=1100001&dispShopNo2=1100002&dispShopNo3=1100003']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        i['prdname'] = response.xpath('//*[@id="prdDetailTopArea"]/div[1]/em').extract()
        i['prdprice'] = response.xpath('//*[@id="prdPriceBenefit"]/div[2]/dl[1]/dd/div/strong').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
