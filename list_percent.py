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


#上市漲跌幅%
twse_pos0 = [] #平盤
twse_pos0_1 = []
twse_pos1_2 = []
twse_pos2_3 = []
twse_pos3_4 = []
twse_pos4_5 = []
twse_pos5_6 = []
twse_pos6_7 = []

twse_minus0_1 = []
twse_minus1_2 = []
twse_minus2_3 = []
twse_minus3_4 = []
twse_minus4_5 = []
twse_minus5_6 = []
twse_munus6_7 = []


#=====================
total_twse = 0 
for i in stock_no_list:
    try:
	percent = float(Stock(i)._SimpleAnalytics__raw_data[-1][7]) / float(Stock(i)._SimpleAnalytics__raw_data[-2][6])
        percent = percent * 100
	if percent > 0 and percent < 1:
           twse_pos0_1.append(i)		
	if percent > 1 and percent < 2: 
           twse_pos1_2.append(i) 
        if percent > 2 and percent < 3:
           twse_pos2_3.append(i)
        if percent > 3 and percent < 4:
           twse_pos3_4.append(i)
        if percent > 4 and percent < 5:
           twse_pos4_5.append(i)
        if percent > 5 and percent < 6:
           twse_pos5_6.append(i)
        if percent > 6 and percent < 7:
           twse_pos6_7.append(i)
        if percent < 0 and percent > -1:
           twse_minus0_1.append(i)
        if percent < -1 and percent > -2:
           twse_minus1_2.append(i)
        if percent < -2 and percent > -3:
           twse_minus2_3.append(i)
        if percent < -3 and percent > -4:
           twse_minus3_4.append(i)
        if percent < -4 and percent > -5:
           twse_minus4_5.append(i)
        if percent < -5 and percent > -6:
           twse_minus5_6.append(i)
        if percent < -6 and percent > -7:
           twse_minus6_7.append(i)
	if percent == 1:
	   twse_pos0.append(i)


	print percent
	total_twse+=1
    except:     # 回傳為None 或 資料不足導致ValueError
        pass

print '擷取到的上市公司有%d家'%int(total_twse)
print '上市公司中收平盤的有'+'%.2f'%(len(twse_pos0_1)/float(total_twse)*100)
print '上市公司漲0~1%的有'+'%.2f'%(len(twse_pos0_1)/float(total_twse)*100)


"""
#======================
# 上櫃股票漲跌%

otc_pos0 = [] #平盤
otc_pos0_1 = []
otc_pos1_2 = []
otc_pos2_3 = []
otc_pos3_4 = []
otc_pos4_5 = []
otc_pos5_6 = []
otc_pos6_7 = []

otc_minus0_1 = []
otc_minus1_2 = []
otc_minus2_3 = []
otc_minus3_4 = []
otc_minus4_5 = []
otc_minus5_6 = []
otc_minus6_7 = []



total_otc = 0
for i in OTC_no_list:
    print i
    try:
        percent = float(Stock(i)._SimpleAnalytics__raw_data[-1][7]) / float(Stock(i)._SimpleAnalytics__raw_data[-2][6])
        percent = percent * 100 
        if percent > 0 and percent < 1:
           otc_pos0_1.append(i)    
        if percent > 1 and percent < 2:  
           otc_pos1_2.append(i) 
        if percent > 2 and percent < 3:
           otc_pos2_3.append(i)
        if percent > 3 and percent < 4:
           otc_pos3_4.append(i)
        if percent > 4 and percent < 5:
           otc_pos4_5.append(i)
        if percent > 5 and percent < 6:
           otc_pos5_6.append(i)
        if percent > 6 and percent < 7:
           otc_pos6_7.append(i)
        if percent < 0 and percent > -1: 
           otc_minus0_1.append(i)
        if percent < -1 and percent > -2: 
           otc_minus1_2.append(i)
        if percent < -2 and percent > -3: 
           otc_minus2_3.append(i)
        if percent < -3 and percent > -4: 
           otc_minus3_4.append(i)
        if percent < -4 and percent > -5: 
           otc_minus4_5.append(i)
        if percent < -5 and percent > -6: 
           otc_minus5_6.append(i)
        if percent < -6 and percent > -7: 
           otc_minus6_7.append(i)
        if percent == 0 :
	   otc_pos0.append(i)

        print percent
        total_otc+=1
    except:     # 回傳為None 或 資料不足導致ValueError
        pass


"""



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

 
 
 

 
