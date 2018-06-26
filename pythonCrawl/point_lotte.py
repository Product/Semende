
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 19:57:19 2018

@author: ikhwan
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('\n', data)

driver = webdriver.Chrome('/Users/ikhwan/capstone/chromedriver')

driver.get("https://kor.lps.lottedfs.com/kr/mypage/svmnHstrList")
driver.find_element_by_name('loginLpId').send_keys('john6939')
driver.find_element_by_name('password').send_keys('whdlrghks1!')
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
req2 = soup.find("a",{"id" : "selectSvmn_02"}).find("strong")
price2 = remove_html_tags(str(req2))
print(price2)

#PC전용 적립금
req3 = soup.find("a",{"id" : "selectSvmn_03"}).find("strong")
price3 = remove_html_tags(str(req3))
print(price3)

#모바일 전용 적립금
req4 = soup.find("a",{"id" : "selectSvmn_04"}).find("strong")
price4 = remove_html_tags(str(req4))
print(price4)





print(req1)
price = remove_html_tags(req1)

print(soup.find_all("td"))

p = soup.find_all('td')
paragraphs = []
for x in p:
    text = re.sub('<.+?>', '', str(x), 0, re.I|re.S)
    paragraphs.append(text)

content =''
for para in paragraphs:
    if para != '2018-03-19' and para != "" and para != "\n\n상세정보\n \n\n":
        #'\n\n\n':
        content = content+" " + para
    else :
        print(content)
        content = ''
    



