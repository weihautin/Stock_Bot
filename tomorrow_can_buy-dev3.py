# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:22:32 2015

@author: tim
"""
# 請先安裝 sudo apt-get install sendemail

import os
import sys
sys.path.append('/home/tim/Stock_Bot')
sys.path.append('/home/tim/Stock_Bot/')
sys.path.append('/home/tim/Stock_Bot/update_csv')
from datetime import datetime
from grs import BestFourPoint
from grs import Stock
from grs import TWSENo
from grs import OTCNo
from csvv import yields as fields #殖利率
from csvv import yields_otc as fields_otc #殖利率
from csvv import vip_other
from csvv import vip_main 
from rand_market_value import market_value as rank_market_value #股本排名
#from sell_buy_immediately import stock_buy_sell_oneday as oneday #是否為現股當充


OTC_no_name = OTCNo().all_stock     # 所有上櫃股票名稱與代碼字典 type: dict

OTC_no_list = OTCNo().all_stock_no # 所有上櫃股票代碼


content = "贏要衝,輸要縮."   #沒有辦法換行

time_now = datetime.now().strftime("%Y%m%d_%H%M%S") #今天的日期 ex:2015-0411
title = str(time_now+"-明天標的股") #Email郵件的標題 ex:2015-0411-選股機器人

attachment = str(time_now)+'.txt' #附件名稱使用當日時間 ex:2015-0411.txt

fileopen = open("detail.txt", 'w') #開啟檔案,w沒有該檔案就新增

f = open('/home/tim/GMAIL.txt','r') #於前一個相對目錄中放置登入GMAIL帳號密碼,目的為了不再GitHub顯示出來.
ID = f.readline().strip('\n') #不包含換行符號\n
PW = f.readline().strip('\n')



fileopen.write('\n\n\n上櫃公司股票篩選===>'+"昨天成交量比前天多,昨天收盤價又比昨天開盤價（暴量長紅),今天收盤又上漲1~10%,且今天成交張數要大於50張"+"\n")

"""
 result = self.data.value[-2] > self.data.value[-3] and self.data.price[-2] > self.data.openprice[-2] and \
                 self.data.price[-1]/self.data.price[-2] >= 1.01  and self.data.price[-1]/self.data.price[-2] <= 1.11 and self.data.value[-1]*1000 > 500

"""

index = 1 
for i in OTC_no_list:
    try:
        if BestFourPoint(Stock(i,mons=2)).otc_y_v_t_r():
           print i,'otc'         #暴量長紅2天

           close_price = Stock(i).raw[-1][6]
           MA5 = Stock(i,mons=2).moving_average(5)[0][-1]
           MA10 = Stock(i,mons=2).moving_average(10)[0][-1]
           MA20 = Stock(i,mons=2).moving_average(20)[0][-1]

           Bias5 = (close_price-MA5)/MA5*100
           Bias10 = (close_price-MA10)/MA10*100
           Bias20 = (close_price-MA20)/MA20*100
           turnover_ration = float(Stock(i).raw[-1][1])/(float(rank_market_value()[i][3])*10000)*100

           try:
 		fileopen.write(OTC_no_name[i].encode("UTF-8")+"`("+i+")"+"OTC"+","+"成交張數"+str(int(Stock(i).raw[-1][1]))+","+ \
                "收盤價"+str(close_price)+","+"去年殖利率"+str(fields_otc()[i][2])+","+"目前價格相當於週均價成長"+"%.1f"%Bias5+"%"+","+"雙週均價"+"%.1f"%Bias10+"%"+ \
                ","+"月均價"+"%.1f"%Bias20+"%"+","+"發行"+rank_market_value()[i][3]+"萬張"+","+"市值"+rank_market_value()[i][4]+"億"+","+"上市"+ \
                rank_market_value()[i][5]+"年"+","+ \
                "當日成交張數/總發行張數="+"%.3f"%turnover_ration+"%"+ "\n")

	   except:
                print i+"資料抓取有問題"
                fileopen.write(OTC_no_name[i].encode("UTF-8")+"`("+i+")"+"OTC"+","+"成交張數"+str(int(Stock(i).raw[-1][1]))+","+"資料抓取有問題"+"\n")
		pass

           
           index = index + 1 
    except:     # 回傳為None 或 資料不足導致ValueError
        print i+"i in OTC_no_list:回傳為None 或 資料不足導致ValueError 或60天內其中有一天沒成交"
        pass



fileopen.close()                #關閉檔案

 
 
os.system('sendEmail -o \
-f weihautin@gmail.com  \
-t "WEI <weihautin@gmail.com>" \
-s smtp.gmail.com:587 \
-xu %s \
-xp %s \
-u %s \
-o message-file=/home/tim/detail.txt \
'%(ID, PW, title))
 

 
