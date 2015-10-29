# -*- coding: utf-8 -*-
"""
產生每日漲跌％統計資料

@author: tim
"""
import os
from datetime import datetime
from grs import BestFourPoint
from grs import Stock
from grs import TWSENo
from grs import OTCNo
import time, itertools


# 記錄開始時間 Record start time
tStart = time.time()



Stock_no_name = TWSENo().all_stock  # 所有上市股票名稱與代碼字典 type: dict

OTC_no_name = OTCNo().all_stock     # 所有上櫃股票名稱與代碼字典 type: dict

stock_no_list = TWSENo().all_stock_no # 所有上市股票代碼

OTC_no_list = OTCNo().all_stock_no # 所有上櫃股票代碼


content = "贏要衝,輸要縮."   #沒有辦法換行

time_now = datetime.now().strftime("%Y-%m%d") #今天的日期 ex:2015-0411
title = str(time_now+"-今日各股漲跌幅度統計") #Email郵件的標題 ex:2015-0411-選股機器人

attachment = str(time_now)+'percent.txt' #附件名稱使用當日時間 ex:2015-0411.txt

fileopen = open(attachment, 'w') #開啟檔案,w沒有該檔案就新增

f = open('/home/tim/GMAIL.txt','r') #於前一個相對目錄中放置登入GMAIL帳號密碼,目的為了不再GitHub顯示出來.
ID = f.readline().strip('\n') #不包含換行符號\n
PW = f.readline().strip('\n')


fileopen.write(time_now+'上市公司股票篩選\n\n\n')


#上市漲跌幅%
twse_pos0 = [] #平盤
twse_pos0_1 = []
twse_pos1_2 = []
twse_pos2_3 = []
twse_pos3_4 = []
twse_pos4_5 = []
twse_pos5_6 = []
twse_pos6_7 = []
twse_pos7_8 = []
twse_pos8_9 = []
twse_pos9_10 = []

twse_minus0_1 = []
twse_minus1_2 = []
twse_minus2_3 = []
twse_minus3_4 = []
twse_minus4_5 = []
twse_minus5_6 = []
twse_minus6_7 = []
twse_minus7_8 = []
twse_minus8_9 = []
twse_minus9_10 = []



#=====================
total_twse = 0 
for i in stock_no_list:
    try:
	percent = float(Stock(i,mons=2)._SimpleAnalytics__raw_data[-1][7]) / float(Stock(i,mons=2)._SimpleAnalytics__raw_data[-2][6])
        percent = percent * 100
	if percent > 0 and percent < 1:
           twse_pos0_1.append(i)		
	if percent >= 1 and percent < 2: 
           twse_pos1_2.append(i) 
        if percent >= 2 and percent < 3:
           twse_pos2_3.append(i)
        if percent >= 3 and percent < 4:
           twse_pos3_4.append(i)
        if percent >= 4 and percent < 5:
           twse_pos4_5.append(i)
        if percent >= 5 and percent < 6:
           twse_pos5_6.append(i)
        if percent >= 6 and percent < 7:
           twse_pos6_7.append(i)
	if percent >= 7 and percent < 8:
	   twse_pos7_8.append(i)
	if percent >= 8 and percent < 9:
           twse_pos8_9.append(i)
	if percent >= 9 and percent < 10.5:
           twse_pos9_10.append(i)




        if percent < 0 and percent > -1:
           twse_minus0_1.append(i)
        if percent <= -1 and percent > -2:
           twse_minus1_2.append(i)
        if percent <= -2 and percent > -3:
           twse_minus2_3.append(i)
        if percent <= -3 and percent > -4:
           twse_minus3_4.append(i)
        if percent <= -4 and percent > -5:
           twse_minus4_5.append(i)
        if percent <= -5 and percent > -6:
           twse_minus5_6.append(i)
        if percent <= -6 and percent > -7:
           twse_minus6_7.append(i)
	if percent <= -7 and percent > -8:
	   twse_minus7_8.append(i)
	if percent <= -8 and percent > -9:
	   twse_minus8_9.append(i)
	if percent <= -9 and percent > -10.5:
	   twse_minus9_10.append(i)






	if percent == 0:
	   twse_pos0.append(i)

	total_twse+=1
    except:     # 回傳為None 或 資料不足導致ValueError
        pass

print '擷取到的上市公司有%d家'%int(total_twse)
fileopen.write('擷取到的上市公司有%d家'%int(total_twse)+'\n\n')

print '上市公司中收平盤的有%d家,共佔了%.1f percent'%(len(twse_pos0), len(twse_pos0)/float(total_twse)*100)
fileopen.write('上市公司中收平盤的有%d家,共佔了%.1f percent'%(len(twse_pos0), len(twse_pos0)/float(total_twse)*100)+'\n')

print '上市公司中漲0~1 percent的有%d家,共佔了%.1f percent'%(len(twse_pos0_1), len(twse_pos0_1)/float(total_twse)*100)
fileopen.write('上市公司中漲0~1 percent的有%d家,共佔了%.1f percent'%(len(twse_pos0_1), len(twse_pos0_1)/float(total_twse)*100)+'\n')

print '上市公司中漲>=1~2 percent的有%d家,共佔了%.1f percent'%(len(twse_pos1_2), len(twse_pos1_2)/float(total_twse)*100)
fileopen.write('上市公司中漲>=1~2 percent的有%d家,共佔了%.1f percent'%(len(twse_pos1_2), len(twse_pos1_2)/float(total_twse)*100)+'\n')

print '上市公司中漲2~3 percent的有%d家,共佔了%.1f percent'%(len(twse_pos2_3), len(twse_pos2_3)/float(total_twse)*100)
fileopen.write('上市公司中漲2~3 percent的有%d家,共佔了%.1f percent'%(len(twse_pos2_3), len(twse_pos2_3)/float(total_twse)*100)+'\n')

print '上市公司中漲3~4 percent的有%d家,共佔了%.1f percent'%(len(twse_pos3_4), len(twse_pos3_4)/float(total_twse)*100)
fileopen.write('上市公司中漲3~4 percent的有%d家,共佔了%.1f percent'%(len(twse_pos3_4), len(twse_pos3_4)/float(total_twse)*100)+'\n')

print '上市公司中漲4~5 percent的有%d家,共佔了%.1f percent'%(len(twse_pos4_5), len(twse_pos4_5)/float(total_twse)*100)
fileopen.write('上市公司中漲4~5 percent的有%d家,共佔了%.1f percent'%(len(twse_pos4_5), len(twse_pos4_5)/float(total_twse)*100)+'\n')

print '上市公司中漲5~6 percent的有%d家,共佔了%.1f percent'%(len(twse_pos5_6), len(twse_pos5_6)/float(total_twse)*100)
fileopen.write('上市公司中漲5~6 percent的有%d家,共佔了%.1f percent'%(len(twse_pos5_6), len(twse_pos5_6)/float(total_twse)*100)+'\n')

print '上市公司中漲6~7 percent的有%d家,共佔了%.1f percent'%(len(twse_pos6_7), len(twse_pos6_7)/float(total_twse)*100)
fileopen.write('上市公司中漲6~7 percent的有%d家,共佔了%.1f percent'%(len(twse_pos6_7), len(twse_pos6_7)/float(total_twse)*100)+'\n')

print '上市公司中漲7~8 percent的有%d家,共佔了%.1f percent'%(len(twse_pos7_8), len(twse_pos7_8)/float(total_twse)*100)
fileopen.write('上市公司中漲7~8 percent的有%d家,共佔了%.1f percent'%(len(twse_pos7_8), len(twse_pos7_8)/float(total_twse)*100)+'\n')

print '上市公司中漲8~9 percent的有%d家,共佔了%.1f percent'%(len(twse_pos8_9), len(twse_pos8_9)/float(total_twse)*100)
fileopen.write('上市公司中漲7~8 percent的有%d家,共佔了%.1f percent'%(len(twse_pos8_9), len(twse_pos8_9)/float(total_twse)*100)+'\n')

print '上市公司中漲9~10 percent的有%d家,共佔了%.1f percent'%(len(twse_pos9_10), len(twse_pos9_10)/float(total_twse)*100)
fileopen.write('上市公司中漲9~10 percent的有%d家,共佔了%.1f percent'%(len(twse_pos9_10), len(twse_pos9_10)/float(total_twse)*100)+'\n')


print '***************************'
fileopen.write('***************************\n')

print '上市公司中跌0~1 percent的有%d家,共佔了%.1f percent'%(len(twse_minus0_1), len(twse_minus0_1)/float(total_twse)*100)
fileopen.write('上市公司中跌0~1 percent的有%d家,共佔了%.1f percent'%(len(twse_minus0_1), len(twse_minus0_1)/float(total_twse)*100)+'\n')

print '上市公司中跌>=1~2 percent的有%d家,共佔了%.1f percent'%(len(twse_minus1_2), len(twse_minus1_2)/float(total_twse)*100)
fileopen.write('上市公司中跌>=1~2 percent的有%d家,共佔了%.1f percent'%(len(twse_minus1_2), len(twse_minus1_2)/float(total_twse)*100)+'\n')

print '上市公司中跌2~3 percent的有%d家,共佔了%.1f percent'%(len(twse_minus2_3), len(twse_minus2_3)/float(total_twse)*100)
fileopen.write('上市公司中跌2~3 percent的有%d家,共佔了%.1f percent'%(len(twse_minus2_3), len(twse_minus2_3)/float(total_twse)*100)+'\n')

print '上市公司中跌3~4 percent的有%d家,共佔了%.1f percent'%(len(twse_minus3_4), len(twse_minus3_4)/float(total_twse)*100)
fileopen.write('上市公司中跌3~4 percent的有%d家,共佔了%.1f percent'%(len(twse_minus3_4), len(twse_minus3_4)/float(total_twse)*100)+'\n')

print '上市公司中跌4~5 percent的有%d家,共佔了%.1f percent'%(len(twse_minus4_5), len(twse_minus4_5)/float(total_twse)*100)
fileopen.write('上市公司中跌4~5 percent的有%d家,共佔了%.1f percent'%(len(twse_minus4_5), len(twse_minus4_5)/float(total_twse)*100)+'\n')

print '上市公司中跌5~6 percent的有%d家,共佔了%.1f percent'%(len(twse_minus5_6), len(twse_minus5_6)/float(total_twse)*100)
fileopen.write('上市公司中跌5~6 percent的有%d家,共佔了%.1f percent'%(len(twse_minus5_6), len(twse_minus5_6)/float(total_twse)*100)+'\n')

print '上市公司中跌6~7 percent的有%d家,共佔了%.1f percent'%(len(twse_minus6_7), len(twse_minus6_7)/float(total_twse)*100)
fileopen.write('上市公司中跌6~7 percent的有%d家,共佔了%.1f percent'%(len(twse_minus6_7), len(twse_minus6_7)/float(total_twse)*100)+'\n')

print '上市公司中跌7~8 percent的有%d家,共佔了%.1f percent'%(len(twse_minus7_8), len(twse_minus7_8)/float(total_twse)*100)
fileopen.write('上市公司中跌7~8 percent的有%d家,共佔了%.1f percent'%(len(twse_minus7_8), len(twse_minus7_8)/float(total_twse)*100)+'\n')

print '上市公司中跌8~9 percent的有%d家,共佔了%.1f percent'%(len(twse_minus8_9), len(twse_minus8_9)/float(total_twse)*100)
fileopen.write('上市公司中跌8~9 percent的有%d家,共佔了%.1f percent'%(len(twse_minus8_9), len(twse_minus8_9)/float(total_twse)*100)+'\n')

print '上市公司中跌9~10 percent的有%d家,共佔了%.1f percent'%(len(twse_minus9_10), len(twse_minus9_10)/float(total_twse)*100)
fileopen.write('上市公司中跌9~10 percent的有%d家,共佔了%.1f percent'%(len(twse_minus9_10), len(twse_minus9_10)/float(total_twse)*100)+'\n')




print '***************************'
fileopen.write('***************************\n')


print '買到上市平盤股票機率%.1f,上漲股票機率%.1f,下跌股票機率%.1f'%(len(twse_pos0)/float(total_twse)*100,(len(twse_pos0_1)+len(twse_pos1_2)+len(twse_pos2_3)+len(twse_pos3_4)+len(twse_pos4_5)+len(twse_pos5_6)+len(twse_pos6_7)+len(twse_pos7_8)+len(twse_pos8_9)+len(twse_pos9_10))/float(total_twse)*100, (len(twse_minus0_1)+len(twse_minus1_2)+len(twse_minus2_3)+len(twse_minus3_4)+len(twse_minus4_5)+len(twse_minus5_6)+len(twse_minus6_7)+len(twse_minus7_8)+len(twse_minus8_9)+len(twse_minus9_10))/float(total_twse)*100)


twse_zero = len(twse_pos0)/float(total_twse)*100
twse_up = (len(twse_pos0_1)+len(twse_pos1_2)+len(twse_pos2_3)+len(twse_pos3_4)+len(twse_pos4_5)+len(twse_pos5_6)+len(twse_pos6_7)+len(twse_pos7_8)+len(twse_pos8_9)+len(twse_pos9_10))/float(total_twse)*100
tswe_down = (len(twse_minus0_1)+len(twse_minus1_2)+len(twse_minus2_3)+len(twse_minus3_4)+len(twse_minus4_5)+len(twse_minus5_6)+len(twse_minus6_7)+len(twse_minus7_8)+len(twse_minus8_9)+len(twse_minus9_10))/float(total_twse)*100
fileopen.write('買到上市平盤股票機率%.1f,上漲股票機率%.1f,下跌股票機率%.1f'%(twse_zero,twse_up,tswe_down)+'\n')


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
otc_pos7_8 = []
otc_pos8_9 = []
otc_pos9_10 = []

otc_minus0_1 = []
otc_minus1_2 = []
otc_minus2_3 = []
otc_minus3_4 = []
otc_minus4_5 = []
otc_minus5_6 = []
otc_minus6_7 = []
otc_minus7_8 = []
otc_minus8_9 = []
otc_minus9_10 = []



total_otc = 0
for i in OTC_no_list:
    try:
        percent = float(Stock(i,mons=2)._SimpleAnalytics__raw_data[-1][7]) / float(Stock(i,mons=2)._SimpleAnalytics__raw_data[-2][6])
        percent = percent * 100 
        if percent > 0 and percent < 1:
           otc_pos0_1.append(i)    
        if percent >= 1 and percent < 2:  
           otc_pos1_2.append(i) 
        if percent >= 2 and percent < 3:
           otc_pos2_3.append(i)
        if percent >= 3 and percent < 4:
           otc_pos3_4.append(i)
        if percent >= 4 and percent < 5:
           otc_pos4_5.append(i)
        if percent >= 5 and percent < 6:
           otc_pos5_6.append(i)
        if percent >= 6 and percent < 7:
           otc_pos6_7.append(i)
	if percent >= 7 and percent < 8:
           otc_pos7_8.append(i)
	if percent >= 8 and percent < 9:
           otc_pos8_9.append(i)
	if percent >= 9 and percent < 10.5:
           otc_pos9_10.append(i)

        if percent < 0 and percent > -1: 
           otc_minus0_1.append(i)
        if percent <= -1 and percent > -2: 
           otc_minus1_2.append(i)
        if percent <= -2 and percent > -3: 
           otc_minus2_3.append(i)
        if percent <= -3 and percent > -4: 
           otc_minus3_4.append(i)
        if percent <= -4 and percent > -5: 
           otc_minus4_5.append(i)
        if percent <= -5 and percent > -6: 
           otc_minus5_6.append(i)
        if percent <= -6 and percent > -7: 
           otc_minus6_7.append(i)
	if percent <= -7 and percent > -8:  
           otc_minus7_8.append(i)
	if percent <= -8 and percent > -9:  
           otc_minus8_9.append(i)	
	if percent <= -9 and percent > -10.5:  
           otc_minus9_10.append(i)

        if percent == 0 :
	   otc_pos0.append(i)

        total_otc+=1
    except:     # 回傳為None 或 資料不足導致ValueError
        pass

print '***************************'
fileopen.write('***************************\n\n\n\n\n')

print '擷取到的上櫃公司有%d家'%int(total_otc)
fileopen.write('擷取到的上櫃公司有%d家'%int(total_otc)+'\n')

print '上櫃公司中收平盤的有%d家,共佔了%.1f percent'%(len(otc_pos0), len(otc_pos0)/float(total_otc)*100)
fileopen.write('上櫃公司中收平盤的有%d家,共佔了%.1f percent'%(len(otc_pos0), len(otc_pos0)/float(total_otc)*100)+'\n')

print '上櫃公司中漲0~1 percent的有%d家,共佔了%.1f percent'%(len(otc_pos0_1), len(otc_pos0_1)/float(total_otc)*100)
fileopen.write('上櫃公司中漲0~1 percent的有%d家,共佔了%.1f percent'%(len(otc_pos0_1), len(otc_pos0_1)/float(total_otc)*100)+'\n')

print '上櫃公司中漲>=1~2 percent的有%d家,共佔了%.1f percent'%(len(otc_pos1_2), len(otc_pos1_2)/float(total_otc)*100)
fileopen.write('上櫃公司中漲>=1~2 percent的有%d家,共佔了%.1f percent'%(len(otc_pos1_2), len(otc_pos1_2)/float(total_otc)*100)+'\n')

print '上櫃公司中漲2~3 percent的有%d家,共佔了%.1f percent'%(len(otc_pos2_3), len(otc_pos2_3)/float(total_otc)*100)
fileopen.write('上櫃公司中漲2~3 percent的有%d家,共佔了%.1f percent'%(len(otc_pos2_3), len(otc_pos2_3)/float(total_otc)*100)+'\n')

print '上櫃公司中漲3~4 percent的有%d家,共佔了%.1f percent'%(len(otc_pos3_4), len(otc_pos3_4)/float(total_otc)*100)
fileopen.write('上櫃公司中漲3~4 percent的有%d家,共佔了%.1f percent'%(len(otc_pos3_4), len(otc_pos3_4)/float(total_otc)*100)+'\n')

print '上櫃公司中漲4~5 percent的有%d家,共佔了%.1f percent'%(len(otc_pos4_5), len(otc_pos4_5)/float(total_otc)*100)
fileopen.write('上櫃公司中漲4~5 percent的有%d家,共佔了%.1f percent'%(len(otc_pos4_5), len(otc_pos4_5)/float(total_otc)*100)+'\n')

print '上櫃公司中漲5~6 percent的有%d家,共佔了%.1f percent'%(len(otc_pos5_6), len(otc_pos5_6)/float(total_otc)*100)
fileopen.write('上櫃公司中漲5~6 percent的有%d家,共佔了%.1f percent'%(len(otc_pos5_6), len(otc_pos5_6)/float(total_otc)*100)+'\n')

print '上櫃公司中漲6~7 percent的有%d家,共佔了%.1f percent'%(len(otc_pos6_7), len(otc_pos6_7)/float(total_otc)*100)
fileopen.write('上櫃公司中漲6~7 percent的有%d家,共佔了%.1f percent'%(len(otc_pos6_7), len(otc_pos6_7)/float(total_otc)*100)+'\n')

print '上櫃公司中漲7~8 percent的有%d家,共佔了%.1f percent'%(len(otc_pos7_8), len(otc_pos7_8)/float(total_otc)*100)
fileopen.write('上櫃公司中漲7~8 percent的有%d家,共佔了%.1f percent'%(len(otc_pos7_8), len(otc_pos7_8)/float(total_otc)*100)+'\n')

print '上櫃公司中漲8~9 percent的有%d家,共佔了%.1f percent'%(len(otc_pos8_9), len(otc_pos8_9)/float(total_otc)*100)
fileopen.write('上櫃公司中漲8~9 percent的有%d家,共佔了%.1f percent'%(len(otc_pos8_9), len(otc_pos8_9)/float(total_otc)*100)+'\n')

print '上櫃公司中漲9~10 percent的有%d家,共佔了%.1f percent'%(len(otc_pos9_10), len(otc_pos9_10)/float(total_otc)*100)
fileopen.write('上櫃公司中漲9~10 percent的有%d家,共佔了%.1f percent'%(len(otc_pos9_10), len(otc_pos9_10)/float(total_otc)*100)+'\n')




print '***************************'
fileopen.write('***************************'+'\n')

print '上櫃公司中跌0~1 percent的有%d家,共佔了%.1f percent'%(len(otc_minus0_1), len(otc_minus0_1)/float(total_otc)*100)
fileopen.write('上櫃公司中跌0~1 percent的有%d家,共佔了%.1f percent'%(len(otc_minus0_1), len(otc_minus0_1)/float(total_otc)*100)+'\n')

print '上櫃公司中跌>=1~2 percent的有%d家,共佔了%.1f percent'%(len(otc_minus1_2), len(otc_minus1_2)/float(total_otc)*100)
fileopen.write('上櫃公司中跌>=1~2 percent的有%d家,共佔了%.1f percent'%(len(otc_minus1_2), len(otc_minus1_2)/float(total_otc)*100)+'\n')

print '上櫃公司中跌2~3 percent的有%d家,共佔了%.1f percent'%(len(otc_minus2_3), len(otc_minus2_3)/float(total_otc)*100)
fileopen.write('上櫃公司中跌2~3 percent的有%d家,共佔了%.1f percent'%(len(otc_minus2_3), len(otc_minus2_3)/float(total_otc)*100)+'\n')

print '上櫃公司中跌3~4 percent的有%d家,共佔了%.1f percent'%(len(otc_minus3_4), len(otc_minus3_4)/float(total_otc)*100)
fileopen.write('上櫃公司中跌3~4 percent的有%d家,共佔了%.1f percent'%(len(otc_minus3_4), len(otc_minus3_4)/float(total_otc)*100)+'\n')

print '上櫃公司中跌4~5 percent的有%d家,共佔了%.1f percent'%(len(otc_minus4_5), len(otc_minus4_5)/float(total_otc)*100)
fileopen.write('上櫃公司中跌4~5 percent的有%d家,共佔了%.1f percent'%(len(otc_minus4_5), len(otc_minus4_5)/float(total_otc)*100)+'\n')

print '上櫃公司中跌5~6 percent的有%d家,共佔了%.1f percent'%(len(otc_minus5_6), len(otc_minus5_6)/float(total_otc)*100)
fileopen.write('上櫃公司中跌5~6 percent的有%d家,共佔了%.1f percent'%(len(otc_minus5_6), len(otc_minus5_6)/float(total_otc)*100)+'\n')

print '上櫃公司中跌6~7 percent的有%d家,共佔了%.1f percent'%(len(otc_minus6_7), len(otc_minus6_7)/float(total_otc)*100)
fileopen.write('上櫃公司中跌6~7 percent的有%d家,共佔了%.1f percent'%(len(otc_minus6_7), len(otc_minus6_7)/float(total_otc)*100)+'\n')

print '上櫃公司中跌7~8 percent的有%d家,共佔了%.1f percent'%(len(otc_minus7_8), len(otc_minus7_8)/float(total_otc)*100)
fileopen.write('上櫃公司中跌7~8 percent的有%d家,共佔了%.1f percent'%(len(otc_minus7_8), len(otc_minus7_8)/float(total_otc)*100)+'\n')

print '上櫃公司中跌8~9 percent的有%d家,共佔了%.1f percent'%(len(otc_minus8_9), len(otc_minus8_9)/float(total_otc)*100)
fileopen.write('上櫃公司中跌8~9 percent的有%d家,共佔了%.1f percent'%(len(otc_minus8_9), len(otc_minus8_9)/float(total_otc)*100)+'\n')

print '上櫃公司中跌9~10 percent的有%d家,共佔了%.1f percent'%(len(otc_minus9_10), len(otc_minus9_10)/float(total_otc)*100)
fileopen.write('上櫃公司中跌9~10 percent的有%d家,共佔了%.1f percent'%(len(otc_minus9_10), len(otc_minus9_10)/float(total_otc)*100)+'\n')


print '***************************'
fileopen.write('***************************'+'\n')

print '買到上櫃平盤股票機率%.1f,上漲股票機率%.1f,下跌股票機率%.1f'%(len(otc_pos0)/float(total_otc)*100,(len(otc_pos0_1)+len(otc_pos1_2)+len(otc_pos2_3)+len(otc_pos3_4)+len(otc_pos4_5)+len(otc_pos5_6)+len(otc_pos6_7)+len(otc_pos7_8)+len(otc_pos8_9)+len(otc_pos9_10))/float(total_otc)*100, (len(otc_minus0_1)+len(otc_minus1_2)+len(otc_minus2_3)+len(otc_minus3_4)+len(otc_minus4_5)+len(otc_minus5_6)+len(otc_minus6_7)+len(otc_minus7_8)+len(otc_minus8_9)+len(otc_minus9_10))/float(total_otc)*100)

otc_zero = len(otc_pos0)/float(total_otc)*100
otc_up = (len(otc_pos0_1)+len(otc_pos1_2)+len(otc_pos2_3)+len(otc_pos3_4)+len(otc_pos4_5)+len(otc_pos5_6)+len(otc_pos6_7)+len(otc_pos7_8)+len(otc_pos8_9)+len(otc_pos9_10))/float(total_otc)*100
otc_down = (len(otc_minus0_1)+len(otc_minus1_2)+len(otc_minus2_3)+len(otc_minus3_4)+len(otc_minus4_5)+len(otc_minus5_6)+len(otc_minus6_7)+len(otc_minus7_8)+len(otc_minus8_9)+len(otc_minus9_10))/float(total_otc)*100

fileopen.write('買到上櫃平盤股票機率%.1f,上漲股票機率%.1f,下跌股票機率%.1f'%(otc_zero,otc_up,otc_down)+'\n\n\n\n\n\n\n\n')



print '***************************'
fileopen.write('***************************'+'\n')

print '買到全上市與上櫃平盤股票機率%.1f,上漲股票機率%.1f,下跌股票機率%.1f'%(  (len(otc_pos0)+len(twse_pos0))/float(total_twse+total_otc)*100 ,\
     ( (len(otc_pos0_1)+len(otc_pos1_2)+len(otc_pos2_3)+len(otc_pos3_4)+len(otc_pos4_5)+len(otc_pos5_6)+len(otc_pos6_7)+len(otc_pos7_8) \
+len(otc_pos8_9)+len(otc_pos9_10))+(len(twse_pos0_1)+len(twse_pos1_2)+len(twse_pos2_3)+len(twse_pos3_4)+len(twse_pos4_5)+len(twse_pos5_6)+ \
len(twse_pos6_7)+len(twse_pos7_8)+len(twse_pos8_9)+len(twse_pos9_10)) ) / float(total_twse+total_otc )*100, \
((len(otc_minus0_1)+len(otc_minus1_2)+len(otc_minus2_3)+len(otc_minus3_4)+len(otc_minus4_5)+len(otc_minus5_6)+len(otc_minus6_7)+ \
len(otc_minus7_8)+len(otc_minus8_9)+len(otc_minus9_10))+(len(twse_minus0_1)+len(twse_minus1_2)+len(twse_minus2_3)+len(twse_minus3_4) \
+len(twse_minus4_5)+len(twse_minus5_6)+len(twse_minus6_7)+len(twse_minus7_8)+len(twse_minus8_9)+len(twse_minus9_10))) / float(total_twse+total_otc )*100 )


total_zero = (len(otc_pos0)+len(twse_pos0))/float(total_twse+total_otc)*100
total_up = ( (len(otc_pos0_1)+len(otc_pos1_2)+len(otc_pos2_3)+len(otc_pos3_4)+len(otc_pos4_5)+len(otc_pos5_6)+len(otc_pos6_7)+len(otc_pos7_8)+len(otc_pos8_9)+len(otc_pos9_10))+ \
(len(twse_pos0_1)+len(twse_pos1_2)+len(twse_pos2_3)+len(twse_pos3_4)+len(twse_pos4_5)+len(twse_pos5_6)+len(twse_pos6_7)+len(twse_pos7_8)+len(twse_pos8_9)+len(twse_pos9_10))) / float(total_twse+total_otc )*100
total_down = ((len(otc_minus0_1)+len(otc_minus1_2)+len(otc_minus2_3)+len(otc_minus3_4)+len(otc_minus4_5)+len(otc_minus5_6)+len(otc_minus6_7)++len(otc_minus7_8)+len(otc_minus8_9)+len(otc_minus9_10)) \
+(len(twse_minus0_1)+len(twse_minus1_2)+len(twse_minus2_3)+len(twse_minus3_4)+len(twse_minus4_5)+len(twse_minus5_6)+len(twse_minus6_7)+len(twse_minus7_8)+len(twse_minus8_9)+len(twse_minus9_10))) / float(total_twse+total_otc )*100

fileopen.write('買到全上市與上櫃平盤股票機率%.1f,上漲股票機率%.1f,下跌股票機率%.1f'%(total_zero,total_up,total_down))




# 記錄結束時間 Record stop time
tStop = time.time()

print "共花費了幾秒"
print(tStop - tStart)




fileopen.close()                #關閉檔案

# u027425@gmail.com

os.system('sendEmail -o \
 -f u160895@taipower.com.tw \
 -t "WEI <weihautin@gmail.com>" u027351@taipower.com.tw \
 -s smtp.gmail.com:587 \
 -xu %s \
 -xp %s \
 -u %s \
 -m %s \
 -a %s \
 '%(ID, PW, title, content, attachment))

 
 
# figoman1979@gmail.com 

 
