#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:27:38 2018

@author: ikhwan
"""

import requests
from bs4 import BeautifulSoup
import re
from time import sleep

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('\n', data)

productInfo_Shilla=[]

def shilla():
    for i in range(0, len(URL_shilla)):
        productURL = 'http://www.shilladfs.com'
        productNum = URL_shilla[i]
        product = productURL+productNum
        product = 'http://www.shilladfs.com/estore/kr/ko/Skin-Care/Basic-Skin-Care/Lotion/p/3396788'
        req = requests.get(product)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        sl_title = soup.find("meta",{"property" : "og:description"})    #상품이름 가져오기
        sl_product_title = sl_title.get('content')
        sl_URL = soup.find("meta",{"property" : "og:url"})              #상품URL 가져오기
        sl_product = sl_URL.get('content')
        sl_image = soup.find("meta",{"property" : "og:image"})          #상품이미지URL 가져오기
        sl_image_URL = sl_image.get('content')
        if 'desc pd-name' in html:      #대부분의 페이지에서 가격과 브랜드, 레퍼런스 넘버 가져오기
            sl_product_category_list = soup.find_all("a",{"class" : "selectbtn"})
            sl_product_category1 = sl_product_category_list[0].text       
            sl_product_category2 = sl_product_category_list[1].text
            sl_product_category3 = sl_product_category_list[2].text
            sl_product_normal_price = soup.find("em",{"class" : "pd-discount"}).text
            sl_product_brand = soup.find("strong",{"class" : "point"}).text
            sl_product_number = soup.find("p",{"class" : "number pd-no"}).text
            productInfo_Shilla.append([sl_product_title,sl_product_normal_price, sl_product_category1, sl_product_category2,sl_product_category3,sl_product_brand,sl_product_number,sl_image_URL, sl_product])
        elif 'prd_info' in html:        #예외적인 페이지가 있음 ex) http://www.shilladfs.com/estore/kr/ko/p/72534
            sl_product_category_list = soup.find("div",{"class" : "sub_nav"}).find("ul").find_all("li")
            sl_product_category1 = sl_product_category_list[1].text       
            sl_product_category2 = sl_product_category_list[2].text
            sl_product_category3 = sl_product_category_list[3].text
            sl_price = soup.find("div",{"class" : "prd_price"}).find("dl",{"class" : "prd_info_guide normal"}).find("dd").find("strong")
            sl_product_normal_price = remove_html_tags(str(sl_price)) 
            sl_product_brandname = soup.find("input",{"id" : "brandId"})
            sl_product_brand = sl_product_brandname.get("value")
            productInfo_Shilla.append([sl_product_title,sl_product_normal_price, sl_product_category1, sl_product_category2,sl_product_category3,sl_product_brand,sl_product_number,sl_image_URL, sl_product])
        #elif '' in html: #http://www.shilladfs.com/estore/kr/ko/Skin-Care/Basic-Skin-Care/Lotion/p/2038721
            
        else:
            print(i)
            
        
        i=i+1
        sleep(3)
        if i==10:
            break;
shilla()





def test(num):
    for i in range(0, len(URL_ssg)):
        productnum = URL_ssg[i]
        if num in URL_ssg[i]:
            print(i)
            break;
        
test('20199000006')



    
    
    
    
    
    
    

