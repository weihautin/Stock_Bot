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

#stock_name_list = TWSENo().all_stock_name

OTC_no_list = OTCNo().all_stock_no # 所有上櫃股票代碼

#OTC_name_list = OTCNo().all_stock_name


content = "贏要衝,輸要縮.  生死有命,富貴在天."   #沒有辦法換行

time_now = datetime.now().strftime("%Y-%m%d") #今天的日期 ex:2015-0411
title = str(time_now+"-小小兵機器人") #Email郵件的標題 ex:2015-0411-選股機器人

attachment = str(time_now)+'.txt' #附件名稱使用當日時間 ex:2015-0411.txt

fileopen = open(attachment, 'w') #開啟檔案,w沒有該檔案就新增

f = open('/home/tim/GMAIL.txt','r') #於前一個相對目錄中放置登入GMAIL帳號密碼,目的為了不再GitHub顯示出來.
ID = f.readline().strip('\n') #不包含換行符號\n
PW = f.readline().strip('\n')



fileopen.write('上市公司股票篩選\n\n\n')


j = 1
for i in stock_no_list:
    print i, '上市', Stock_no_name[i]
    try:
        best_point, info = BestFourPoint(Stock(i)).best_four_point()
       
        if best_point:           # 買點
            fileopen.write(str(j)+' '+'Buy'+' '+i+' ('+Stock_no_name[i].encode("UTF-8")+')'+'\n')
            fileopen.write(info.encode("UTF-8"))
            fileopen.write('\n\n')
            fileopen.write('----------------------------------\n')
           
            j+=1
    except:     # 不作為或資料不足
        pass
    
fileopen.write('\n\n\n上櫃公司股票篩選\n\n\n')

j = 1
for i in OTC_no_list:
    print i,'上櫃', OTC_no_name[i]
    try:
        best_point, info = BestFourPoint(Stock(i)).best_four_point()

        if best_point:           # 買點
            fileopen.write(str(j)+' '+'Buy'+' '+i+' ('+OTC_no_name[i].encode("UTF-8")+')'+'\n')
            fileopen.write(info.encode("UTF-8"))
            fileopen.write('\n\n')
            fileopen.write('----------------------------------\n')
            j+=1
    except:     # 不作為或資料不足
        pass

    

fileopen.close()                #關閉檔案


# 透過sendEmail附加檔案寄送Email
"""
ID = ID.decode("utf-8")
ID = ID.encode("ascii","ignore")
ll

PW = PW.decode("utf-8")
PW = PW.encode("ascii","ignore")

title = title.decode("utf-8")
title = title.encode("ascii","ignore")
"""

os.system('sendEmail -o \
 -f u160895@taipower.com.tw \
 -t "WEI <weihautin@gmail.com>" u160895@taipower.com.tw hautinboy@yahoo.com.tw\
 -s smtp.gmail.com:587 \
 -xu %s \
 -xp %s \
 -u %s \
 -m %s \
 -a %s \
 '%(ID, PW, title, content, attachment))
 
 
 
 

 
