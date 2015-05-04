# -*- coding: utf-8 -*-
"""
傳統黃金交叉5日均線大於20日均線即可
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



fileopen.write("\n"+"傳統黃金交叉定義:昨天短均線低於長均線,今天短均線高於長均線"+"\n\n")


#傳統黃金交叉(5日均線向上穿越10日均線)
index = 1 
for i in stock_no_list:
    try: 
        if BestFourPoint(Stock(i)).golden_cross_no_back_test(m=5,n=10):
           fileopen.write(str(index)+" "+"傳統黃金交叉(5日均線向上穿越10日均線)"+"-"+Stock_no_name[i].encode("UTF-8")+"-"+i+"-"+"成交張數"+"-"+str(int(Stock(i).raw[-1][1]/1000))+"\n")
           index = index + 1 
    except:     # 回傳為None 或 資料不足導致ValueError
        pass
fileopen.write("\n\n")



#傳統黃金交叉(5日均線向上穿越20日均線)
index = 1
for i in stock_no_list:
    try: 
        if BestFourPoint(Stock(i)).golden_cross_no_back_test(m=5,n=20):
           fileopen.write(str(index)+" "+"傳統黃金交叉(5日均線向上穿越20日均線)"+"-"+Stock_no_name[i].encode("UTF-8")+"-"+i+"-"+"成交張數"+"-"+str(int(Stock(i).raw[-1][1]/1000))+"\n")
           index = index + 1
    except:     # 回傳為None 或 資料不足導致ValueError
        pass
fileopen.write("\n\n")






 
fileopen.write('\n\n\n上櫃公司股票篩選\n\n\n')


#傳統黃金交叉(5日均線向上穿越10日均線)
index = 1
for i in OTC_no_list:
    try:
        if BestFourPoint(Stock(i)).golden_cross_no_back_test(m=5,n=20):
           fileopen.write(str(index)+" "+"傳統黃金交叉(5日均線向上穿越20日均線)"+"-"+OTC_no_name[i].encode("UTF-8")+"-"+i+"-"+"成交張數"+"-"+str(int(Stock(i).raw[-1][1]))+"\n")
           index = index + 1
    except:     # 回傳為None 或 資料不足導致ValueError
        pass
fileopen.write("\n\n")




fileopen.close()                #關閉檔案


"""
os.system('sendEmail -o \
 -f u160895@taipower.com.tw \
 -t "WEI <weihautin@gmail.com>" u160895@taipower.com.tw \
 -s smtp.gmail.com:587 \
 -xu %s \
 -xp %s \
 -u %s \
 -m %s \
 -a %s \
 '%(ID, PW, title, content, attachment))
"""

 
 
 

 
