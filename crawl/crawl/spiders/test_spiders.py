#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:57:47 2018

@author: ikhwan
"""
import scrapy
import sys
from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from crawl.items import CrawlItem
from scrapy.http import Request
from scrapy.selector import Selector
reload(sys)
sys.setdefaultencoding('utf-8')
 
class test_spiders(scrapy.Spider):
    name = "crawl"  #spider 이름
    allowed_domains = ["http://kor.lottedfs.com"]   #크롤링할 최상위 도메인
    start_urls = ["http://kor.lottedfs.com/kr/product/productDetail?prdNo=10001860657&dispShopNo1=1100001&dispShopNo2=1100002&dispShopNo3=1100003"]  #실제 크롤링할 주소
     
    def parse(self, response):
        hxs = Selector(response)    #지정된 주소에서 전체 소스코드를 가져옴
        selects =[] #전체 소스코드 중에서 필요한 영역만 잘라내서 담을 리스트
        selects = hxs.xpath('//tbody[@class="line"]/tr')    #필요한 영역을 잘라서 리스트에 저장
        items = [] #데이터를 Item별로 구별해서 담을 리스트
        for sel in selects:
            item = CrawlItem() #item 객체 선언 
            item['prdname'] = sel.xpath('em[@class="name"]/text()').extract() #상품이름 추출
            item['prdprice'] = sel.xpath('strong[@class="fc3"]/text()').extract() #상품가격 추출
           
            items.append(item) #Item 1개 세트를 리스트에 담음
        return items


#<em class="name">ULTRA FACIAL TONER 250ml</em>

#<div class="priceArea">
#<strong class="fc3">$19</strong>
#<span>(20,292원)</span>
#</div>
#//*[@id="prdPriceBenefit"]/div[2]/dl[1]/dd/div/strong