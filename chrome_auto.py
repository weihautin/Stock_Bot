# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:56:59 2015

@author: tim
"""

"""
import time
from selenium import webdriver

link_base = 'http://www.twse.com.tw/ch/trading/indices/MI_5MINS_HIST/MI_5MINS_HIST.php'
#http://www.twse.com.tw/ch/trading/indices/MI_5MINS_HIST/MI_5MINS_HIST.php?myear=100&mmon=01

driver = webdriver.Chrome()


for y in range(2015, 2014, -1):
    for m in range (12, 00, -1):
        link = link_base + '?myear={:d}&mmon={:02d}'.format(y-1911, m)
        driver.get(link)
        if driver.find_elements_by_class_name('gray12'):
            driver.find_elements_by_xpath('//img[contains(@src, "save_csv")]')[0].click()
            time.sleep(5)

driver.close()

"""



"""
import time
from selenium import webdriver

link_base = 'http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU_d.php'
# http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU_d.php?input_date=102%2F10%2F09&select2=ALL&order=STKNO&login_btn=%ACd%B8%DF
# 那天沒有開市沒網頁Download圖示的話會顯示IndexError: list index out of range

driver = webdriver.Chrome()


#?input_date=102%2F10%2F09&select2=ALL

for y in range(2014, 2013, -1):
    for m in range (5, 4, -1):
        for n in range(12, 00, -1):
            link = link_base + '?input_date={:d}%2F{:02d}%2F{:02d}&select2=ALL'.format(y-1911, m, n)
            driver.get(link)
            if driver.find_elements_by_class_name('basic2'):
                try:
                    driver.find_elements_by_xpath('//img[contains(@src, "save_csv")]')[0].click()
                except IndexError:
                    pass
                time.sleep(5)

driver.close()
"""


import time
from selenium import webdriver

link_base = 'http://www.twse.com.tw/ch/trading/exchange/TWT93U/TWT93U.php'
# http://www.twse.com.tw/ch/trading/exchange/TWT93U/TWT93U.php?input_date=101/03/02
# 那天沒有開市沒網頁Download圖示的話會顯示IndexError: list index out of range
# 預設目錄下載至此

driver = webdriver.Chrome()


#'?input_date={:d}/{:02d}/{:02d}'..format(y-1911, m, n)
for y in range(2014, 2013, -1):
    for m in range (5, 4, -1):
        for n in range(12, 00, -1):
            link = link_base + '?input_date={:d}/{:02d}/{:02d}'.format(y-1911, m, n)
            driver.get(link)
            if driver.find_elements_by_class_name('basic2'):
                try:
                    driver.find_elements_by_xpath('//img[contains(@src, "save_csv")]')[0].click()
                except IndexError:
                    pass
                time.sleep(5)

driver.close()



        


        