#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 01:31:21 2018

@author: ikhwan
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen("http://kor.lottedfs.com/kr/product/productDetail?prdNo=10001860657&dispShopNo1=1100001&dispShopNo2=1100002&dispShopNo3=1100003")
document = page.read()
soup = BeautifulSoup(document, 'html5lib')
price = soup.find(id="prdPriceBenefit")
print(price)

def get_html(url):
	response = None
	with ClientSession() as session:
		with aiohttp.Timeout(60):
			try:
				response = await session.get(url)
				
				if response.status == 200:
					return (yield from response.text('utf8'))
			except Exception as e:
				if response is not None:
					response.close()
				raise e
			finally:
				if response is not None:
					await response.release()
