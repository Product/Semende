#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 23:16:44 2018

@author: ikhwan
"""


from selenium import webdriver
from bs4 import BeautifulSoup
import re

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('\n', data)




driver = webdriver.Chrome('/Users/ikhwan/capstone/chromedriver')


driver.get('https://www.shilladfs.com/estore/kr/ko/login')
driver.find_element_by_xpath('//*[@id="container"]/div[1]/div/div/div[2]/div/a').click()
driver.implicitly_wait(2)
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]

driver.switch_to_window(window_after)

driver.find_element_by_name('j_username').send_keys('john6939')
driver.find_element_by_name('j_password').send_keys('whdlrghks1!')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div/div/div[2]/div[1]/a').click()
driver.implicitly_wait(2)
driver.switch_to_window(window_before)
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div[1]/ul/li[3]/a').click()
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

reserved = str(soup.find("dl",{"class":"save"}).find("dd").find("div").find("span").find("em"))
price = remove_html_tags(reserved)
price = "".join(price.split());
print(price)

from selenium import webdriver
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import threading
from time import time

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('\n', data)

def lotte(user_id,user_pw):
    driver = webdriver.Chrome('/Users/ikhwan/capstone/chromedriver')
    
    driver.get("https://kor.lps.lottedfs.com/kr/mypage/svmnHstrList")
    driver.find_element_by_name('loginLpId').send_keys(user_id)
    driver.find_element_by_name('password').send_keys(user_pw)
    driver.find_element_by_xpath('/html/body/div/div/section/div/div/div[1]/form/div[2]/div/div[1]/p[2]/a').click()
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.ID, 'mylotteMemberInfoArea'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ('lotte fail')
        #WebDriverWait wait = new WebDriverWait(WebDriverRefrence,5);
        #wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("mylotteMemberInfoArea")));
    
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    
    #일반 적립금
    req1 = soup.find("a",{"id" : "selectSvmn_01"}).find("strong")
    price1 = remove_html_tags(str(req1))
    print(price1)

#플러스 적립금
#req2 = soup.find("a",{"id" : "selectSvmn_02"}).find("strong")
#price2 = remove_html_tags(str(req2))
#print(price2)

#PC전용 적립금
#req3 = soup.find("a",{"id" : "selectSvmn_03"}).find("strong")
#price3 = remove_html_tags(str(req3))
#print(price3)

#모바일 전용 적립금
#req4 = soup.find("a",{"id" : "selectSvmn_04"}).find("strong")
#price4 = remove_html_tags(str(req4))
#print(price4)




def shinla(user_id,user_pw):

    driver = webdriver.Chrome('/Users/ikhwan/capstone/chromedriver')
    
    
    driver.get('https://www.shilladfs.com/estore/kr/ko/login')
    driver.find_element_by_xpath('//*[@id="container"]/div[1]/div/div/div[2]/div/a').click()
    driver.implicitly_wait(2)
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    
    driver.switch_to_window(window_after)
    
    driver.find_element_by_name('j_username').send_keys(user_id)
    driver.find_element_by_name('j_password').send_keys(user_pw)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div/div/div[2]/div[1]/a').click()

        #WebDriverWait wait = new WebDriverWait(WebDriverRefrence,5);
        #wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("mylotteMemberInfoArea")));
    driver.switch_to_window(window_before)
    #timeout = 5
    #try:
    #    element_present = EC.presence_of_element_located((By.Xpath, '//*[@id="header"]/div[2]/div/div[1]/ul/li[3]/a'))
    #    WebDriverWait(driver, timeout).until(element_present)
    #except TimeoutException:
    #    print ('shinla fail')
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div[1]/ul/li[3]/a').click()
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    
    reserved = soup.find("dl",{"class":"save"}).find("dd").find("div").find("span").find("em")
    price = remove_html_tags(str(reserved))
    print(price)



def ssg(user_id,user_pw):
    driver = webdriver.Chrome('/Users/ikhwan/capstone/chromedriver')
    driver.get('https://www.ssgdfm.com/shop/main')
    driver.find_element_by_xpath('//*[@id="nSTopNav"]/div/div/ul/li[3]/a').click()
    driver.implicitly_wait(2)
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]

    driver.switch_to_window(window_after)
    driver.find_element_by_name('userId').send_keys(user_id)
    driver.find_element_by_name('password').send_keys(user_pw)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/input').click()
    driver.implicitly_wait(1)
    try:
        result = driver.current_url
    except :
        driver.switch_to_window(window_before)
        result = driver.current_url
    driver.find_element_by_xpath('//*[@id="nSTopNav"]/div/div/ul/li[3]/a').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="/shop/mypage/save/"]').click()
    driver.implicitly_wait(1)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    #총 적립금만 가져오기
    req1 = soup.find("p",{"class" : "dataTxt"}).find("span")
    price1 = remove_html_tags(str(req1))
    print(price1)

begin = time()
user_id = 'john6939'
user_pw = 'whdlrghks1!'
    
th_a = threading.Thread(target = lotte, args=(user_id, user_pw))
th_b = threading.Thread(target = shinla, args=(user_id, user_pw))
th_c = threading.Thread(target = ssg, args=(user_id, user_pw))
th_a.start()
th_b.start()
th_c.start()
 
th_a.join()
th_b.join()
th_c.join()
end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))









