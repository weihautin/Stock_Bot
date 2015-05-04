# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:22:59 2015

@author: tim
"""

import os
from grs import RealtimeTWSE
from datetime import datetime
from grs import Stock
from grs import TWSENo
from csvv import yields as fields #殖益率
from sell_buy_immediately import stock_buy_sell_oneday as oneday #是否為現股當充


Stock_no_name = TWSENo().all_stock  # 所有上市股票名稱與代碼字典 type: dict

stock_no_list = TWSENo().all_stock_no # 所有上市股票代碼


content = "贏要衝,輸要縮."   #沒有辦法換行
time_now = datetime.now().strftime("%Y%m%d-%H%M") #今天的日期 ex:2015-0411
title = str(time_now+"-盤中即時成交量機器人") #Email郵件的標題 ex:2015-0411-選股機器人

attachment = str(time_now)+'.csv' #附件名稱使用當日時間 ex:2015-0411.txt

fileopen = open(attachment, 'w') #開啟檔案,w沒有該檔案就新增

f = open('/home/tim/GMAIL.txt','r') #於前一個相對目錄中放置登入GMAIL帳號密碼,目的為了不再GitHub顯示出來.
ID = f.readline().strip('\n') #不包含換行符號\n:q

PW = f.readline().strip('\n')


fileopen.write('上市公司股票篩選\n\n\n')

#fileopen.write("股票",",","100",",","倍週均量",",","成交張數",",","殖利率","100",",","倍月均量")


#=====================
index = 1
for i in stock_no_list:
    #print i
    realtime_data = RealtimeTWSE(i)
    try:
        if realtime_data.data[i]['volume_acc'] > Stock(i,mons=3).moving_average_value(5)[0][-2] or realtime_data.data[i]['volume_acc'] > Stock(i,mons=3).moving_average_value(20)[0][-2]: #今天的量大於5日週均量
        #if realtime_data.data[i]['volume_acc'] > Stock(i,mons=1).raw[-2][1]/1000: #今天的量大於昨天的量 
           print i,'Yes123'         #暴量長紅2天
           try:
               if oneday()[i][1] == '':
                  one_day = "買賣現沖 "
               elif oneday()[i][1] =='Y':
                  one_day = "先買現沖"
               else:
                  one_day = ""
           except:
               one_day = "" #csv找不到該股票代碼,即不開放買賣現沖

#           fileopen.write(str(index)+" "+time_now+"-----目前該股累積成交量>週均量"+"-"+Stock_no_name[i].encode("UTF-8")+"-"+i+"-"+"成交張數"+"-"+str(int(Stock(i,mons=1).raw[-1][1]/1000))+"-"+"殖益率"+str(fields()[i][2])+"-"+one_day+"\n")

           fileopen.write('321')
           fileopen.write(i+"-"+Stock_no_name[i].encode("UTF-8")+"-"+"目前累積成交量"+","+        \
           str(float(realtime_data.data[i]['volume_acc'])/float(Stock(i,mons=3).moving_average_value(5)[0][-2]))+","+"倍週均量"+  \
        ","+ "成交張數"+"-"+str(realtime_data.data[i]['volume_acc'])+","+"殖益率"+str(fields()[i][2])+"-"+one_day+ \
        ","+str(float(realtime_data.data[i]['volume_acc'])/float(Stock(i,mons=3).moving_average_value(20)[0][-2]))+","+"倍月均量"+ \
                                                                                            "\n")
# str(int(Stock(i,mons=1).raw[-1][1]/1000))

           index = index + 1
    except:     # 回傳為None 或 資料不足導致ValueError
        pass


fileopen.close()                #關閉檔案

#realtime_data = RealtimeTWSE(1101)



#print realtime_data.data['1101']['volume_acc'] #今天的量
#print Stock('1101').raw[-2][1]/1000 #昨天的量


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




