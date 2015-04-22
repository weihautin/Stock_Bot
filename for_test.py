# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:22:32 2015

@author: tim
"""
# 請先安裝 sudo apt-get install sendemail

import os
from datetime import datetime
from grs import BestFourPoint
from grs import Stock
from grs import TWSENo
from grs import OTCNo


Stock_no_name = TWSENo().all_stock  # 所有上市股票名稱與代碼字典 type: dict

OTC_no_name = OTCNo().all_stock     # 所有上櫃股票名稱與代碼字典 type: dict

stock_no_list = TWSENo().all_stock_no # 所有上市股票代碼

OTC_no_list = OTCNo().all_stock_no # 所有上櫃股票代碼


content = "贏要衝,輸要縮."   #沒有辦法換行

time_now = datetime.now().strftime("%Y-%m%d") #今天的日期 ex:2015-0411
title = str(time_now+"-小小兵盤後機器人") #Email郵件的標題 ex:2015-0411-選股機器人

attachment = str(time_now)+'.txt' #附件名稱使用當日時間 ex:2015-0411.txt

fileopen = open(attachment, 'w') #開啟檔案,w沒有該檔案就新增

f = open('/home/tim/GMAIL.txt','r') #於前一個相對目錄中放置登入GMAIL帳號密碼,目的為了不再GitHub顯示出來.
ID = f.readline().strip('\n') #不包含換行符號\n
PW = f.readline().strip('\n')


fileopen.write('上市公司股票篩選\n\n\n')


fileopen.write("\n""+昨天暴量長紅,今天又上漲"+"\n\n")

#=====================
index = 1 
for i in stock_no_list:
    try:
        if BestFourPoint(Stock(i)).y_v_t_r():
           print i,'123'         #暴量長紅2天
           fileopen.write(str(index)+" "+"昨天暴量長紅(昨天量>前天量,昨天收盤價>昨天開盤價),今天又上漲3%以上又不可以漲停,今日成交張數要大於800張"+"-"+Stock_no_name[i].encode("UTF-8")+"-"+i+"-"+"成交張數"+"-"+str(int(Stock(i).raw[-1][1]/1000))+"\n")
           index = index + 1 
    except:     # 回傳為None 或 資料不足導致ValueError
        pass

#=====================
index = 1 
for i in OTC_no_list:
    #print i
    try:
        if BestFourPoint(Stock(i)).y_v_t_r():
           print i,'123'         #暴量長紅2天
           fileopen.write(str(index)+" "+"昨天暴量長紅(昨天量>前天量,昨天收盤價>昨天開盤價),今天又上漲3%以上又不可以漲停,今日成交張數要大於800張"+"-"+OTC_no_name[i].encode("UTF-8")+"-"+i+"-"+"成交張數"+"-"+str(int(Stock(i).raw[-1][1]))+"\n")
           index = index + 1 
    except:     # 回傳為None 或 資料不足導致ValueError
        pass


fileopen.close()                #關閉檔案

"""
os.system('sendEmail -o \
 -f u160895@taipower.com.tw \
 -t "WEI <weihautin@gmail.com>" u160895@taipower.com.tw u027425@gmail.com \
 -s smtp.gmail.com:587 \
 -xu %s \
 -xp %s \
 -u %s \
 -m %s \
 -a %s \
 '%(ID, PW, title, content, attachment))
"""

 
 
 

 
