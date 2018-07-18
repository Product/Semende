#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:20:09 2018

@author: ikhwan
"""

# web_test.py
import requests
from bs4 import BeautifulSoup
import re
# remove html tags
def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('\n', data)

def shilla():
    # HTTP GET Request
    req = requests.get('http://www.shilladfs.com/estore/kr/ko/Skin-Care/Basic-Skin-Care/Skin-Toner/p/72534')
    # HTML 소스 가져오기
    html = req.text
    # BeautifulSoup으로 html소스를 python객체로 변환하기
    # 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
    # 이 글에서는 Python 내장 html.parser를 이용했다.
    soup = BeautifulSoup(html, 'html.parser')
    
    sl_product_title = soup.find("dl",{"class" : "prd_info"}).find("dt")
    sl_product_normal_price = soup.find("div",{"class" : "prd_price"}).find("dl",{"class" : "prd_info_guide normal"}).find("dd").find("strong")
    

    
    
    sl_title = remove_html_tags(str(sl_product_title))
    sl_price = remove_html_tags(str(sl_product_normal_price))
    
    
    print("Shilla's Product name is "+ sl_title)  
    print("Shilla's Product price is "+ sl_price)

    
def ssg():
     # HTTP GET Request
    req = requests.get('http://www.ssgdfm.com/shop/product/productDetail?prdtCode=05979000178')
    # HTML 소스 가져오기
    html = req.text
    # BeautifulSoup으로 html소스를 python객체로 변환하기
    # 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
    # 이 글에서는 Python 내장 html.parser를 이용했다.
    soup = BeautifulSoup(html, 'html.parser')
    
    ssg_product_title = soup.find("p",{"id" : "prdtNameTxt"})
    
    ssg_product_normal_price = soup.find("td",{"class" : "sell-price"}).find("strong")
  
    ssg_title = remove_html_tags(str(ssg_product_title))
    ssg_price = remove_html_tags(str(ssg_product_normal_price))
    
    
    print("Shinsegae's Product name is " + ssg_title)
    print("Shinsegae's Product price is " + ssg_price)
    
def lotte():
      # HTTP GET Request
      req = requests.get('http://kor.lottedfs.com/kr/product/productDetail?prdNo=10001860657&dispShopNo1=1100001&dispShopNo2=1100002&dispShopNo3=1100003')
    # HTML 소스 가져오기
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    # 모든 상품 정보는 var prd = 안에
    # 가격 - "saleUntPrc":"19.00"
    # 상품이름 - "prdNm":"ULTRA FACIAL TONER 250ml"
    # 재고 수량 = "stockQty":"74"
    # 가격가져오기
    pattern_price = re.compile(r'"saleUntPrc":"(.*?)"', re.MULTILINE | re.DOTALL)
    script_price = soup.find("script", text=pattern_price)
    pattern_name = re.compile(r'"prdNm":"(.*?)"', re.MULTILINE | re.DOTALL)
    script_title = soup.find("script", text=pattern_name)
    pattern_stk = re.compile(r'"stockQty":"(.*?)"', re.MULTILINE | re.DOTALL)
    script_stk = soup.find("script", text=pattern_stk)
    
    lotte_title = pattern_price.search(script_price.text).group(1)
    lotte_price = pattern_name.search(script_title.text).group(1)
    lotte_stk = pattern_stk.search(script_stk.text).group(1)
    
    # Meta데이터에서 가져오기
    #lotte_product_title = soup.find("meta",{"property" : "rb:itemName"})
    #lotte_product_normal_price = soup.find("meta",{"property" : "rb:originalPrice"})    
    #lotte_title = lotte_product_title.get('content')
    #lotte_price = lotte_product_normal_price.get('content')
   
        
    print("Lotte's Product name is " + lotte_title)
    print("Lotte's Product price is " + lotte_price)
    print("Lotte's Product stock is " + lotte_stk)

    
shilla()
ssg()
lotte()
