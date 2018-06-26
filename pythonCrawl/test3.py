#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:45:34 2018

@author: ikhwan
"""

import urllib
from bs4 import BeautifulSoup
request = urllib.request.Request('https://www.shilladfs.com/estore/kr/ko/myshilla/benefit/mileage') 
response = urllib.request.urlopen(request)
test = response.read()
soup = BeautifulSoup(test, 'html5lib')

print(soup)