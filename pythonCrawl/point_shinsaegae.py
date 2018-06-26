#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 16:50:05 2018

@author: ikhwan
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import re

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('\n', data)

def checkID():
    driver = webdriver.Chrome('/Users/ikhwan/capstone/chromedriver')
    driver.get('https://www.ssgdfm.com/shop/main')
    driver.find_element_by_xpath('//*[@id="nSTopNav"]/div/div/ul/li[3]/a').click()
    driver.implicitly_wait(3)
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]

    driver.switch_to_window(window_after)
    driver.find_element_by_name('userId').send_keys('john6939')
    driver.find_element_by_name('password').send_keys('whdlrghks1!')
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/input').click()
    driver.implicitly_wait(3)
    try:
        result = driver.current_url
    except :
        driver.switch_to_window(window_before)
        result = driver.current_url
    driver.find_element_by_xpath('//*[@id="nSTopNav"]/div/div/ul/li[3]/a').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="/shop/mypage/save/"]').click()
    driver.implicitly_wait(3)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    #총 적립금만 가져오기
    req1 = soup.find("p",{"class" : "dataTxt"}).find("span")
    price1 = remove_html_tags(str(req1))
    print(price1)

checkID()







driver = webdriver.Chrome('/Users/ikhwan/capstone/chromedriver')

driver.get('https://www.ssgdfm.com/shop/login/loginPopupForm?redirectUrl=https:://www.ssgdfm.com/shop/main&nonUserType=myPage')
driver.find_element_by_name('userId').send_keys('john6939')
driver.find_element_by_name('password').send_keys('whdlrghks1!')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/input').click()
driver.implicitly_wait(3)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')









driver = webdriver.Chrome('/Users/ikhwan/capstone/chromedriver')


driver.get('https://www.ssgdfm.com/shop/main')
driver.find_element_by_xpath('//*[@id="nSTopNav"]/div/div/ul/li[3]/a').click()
driver.implicitly_wait(3)
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]

driver.switch_to_window(window_after)

driver.find_element_by_name('userId').send_keys('john6939')
driver.find_element_by_name('password').send_keys('whdlrghks1!')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/input').click()
driver.implicitly_wait(3)


try:
    print(driver.current_url)
except :
    driver.switch_to_window(window_before)
    print(driver.current_url)

