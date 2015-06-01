# -*- coding: utf-8 -*-
"""
上市上櫃即時成交量計算

"""

import os
from grs import RealtimeTWSE
from grs import RealtimeOTC
from datetime import datetime
from grs import Stock
from grs import TWSENo
from grs import OTCNo
#from csvv import yields as fields #TWSE殖益率
#from csvv import yields_otc as fields_otc #OTC殖益率
#from sell_buy_immediately import stock_buy_sell_oneday as oneday #是否為現股當充
from csvv import yields as fields #殖利率
from csvv import yields_otc as fields_otc #殖利率
from csvv import vip_other
from csvv import vip_main 
from rand_market_value import market_value as rank_market_value #股本排名
from sell_buy_immediately import stock_buy_sell_oneday as oneday #是否為現股當充




Stock_no_name = TWSENo().all_stock  # 所有上市股票名稱與代碼字典 type: dict

stock_no_list = TWSENo().all_stock_no # 所有上市股票代碼

OTC_no_name = OTCNo().all_stock     # 所有上櫃股票名稱與代碼字典 type: dict

OTC_no_list = OTCNo().all_stock_no # 所有上櫃股票代碼


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
for i in stock_no_list:
    #print i
    realtime_data = RealtimeTWSE(i)
    try:
        if (realtime_data.data[i]['volume_acc'] > Stock(i,mons=3).moving_average_value(5)[0][-2] or realtime_data.data[i]['volume_acc'] > Stock(i,mons=3).moving_average_value(20)[0][-2]) and float(realtime_data.data[i]['diff'][1]) > 0: #今天的量大於5日週或月均量, 目前要漲
           print i,'TWSE123'        #暴量長紅2天

           close_price = Stock(i).raw[-1][6]
           MA5 = Stock(i,mons=2).moving_average(5)[0][-1]
           MA10 = Stock(i,mons=2).moving_average(10)[0][-1]
           MA20 = Stock(i,mons=2).moving_average(20)[0][-1]
           Bias5 = (close_price-MA5)/MA5*100
           Bias10 = (close_price-MA10)/MA10*100
           Bias20 = (close_price-MA20)/MA20*100
           turnover_ration = float(Stock(i).raw[-1][1]/1000)/(float(rank_market_value()[i][3])*10000)*100
	   try:
		vip_main_str = vip_main()[i][2]
	   except:
                vip_main_str = "無資料"

           time_week = float(realtime_data.data[i]['volume_acc'])/float(Stock(i,mons=3).moving_average_value(5)[0][-2])		
           time_month = float(realtime_data.data[i]['volume_acc'])/float(Stock(i,mons=3).moving_average_value(20)[0][-2])

           try:
                fileopen.write(Stock_no_name[i].encode("UTF-8")+"("+i+")"+"TWSE"+","+"漲幅"+str(float(realtime_data.data[i]['diff'][1]))+"%"+","+"%.1f"%time_week+"倍週量"+","+ \
"%.1f"%time_month+"倍月量"+","+"成交張數"+str(realtime_data.data[i]['volume_acc'])+","+"殖利率" \
           +str(fields()[i][2])+","+"收盤價"+str(close_price)+","+"週均線"+"%.1f"%Bias5+"%"+","+"雙週均價"+"%.1f"%Bias10+"%"\
+","+"月均價"+"%.1f"%Bias20+"%"+","+"發行"+rank_market_value()[i][3]+"萬張"+","+"市值"+rank_market_value()[i][4]+"億"+","+"上市"    \
+rank_market_value()[i][5]+"年"+","+rank_market_value()[i][6].encode("UTF-8")+","+"市值排名:"+rank_market_value()[i][0]+"/1548"+"," \
+"週轉率"+"%.3f"%turnover_ration+"%"+","+"政府機構"+vip_other()[i][1]+"%"+"橋外投資"+vip_other()[i][2]+"%"+"本國金融"+vip_other()[i][3]+"%" \
+"本國法人"+vip_other()[i][4]+"%"+"本國個人含董監"+vip_other()[i][5]+"%"+"董監持股"+vip_main_str+"\n")
           	   
           except:
                pass

    except: # 回傳為None 或 資料不足導致ValueError
        pass



fileopen.write('\n\n\n\n')
fileopen.write('上櫃公司股票篩選\n\n\n\n')

for i in OTC_no_list:  
    #print i
    realtime_data = RealtimeOTC(i)  
    try:
        if (realtime_data.data[i]['volume_acc'] > Stock(i,mons=3).moving_average_value(5)[0][-2]*1000 or realtime_data.data[i]['volume_acc'] > Stock(i,mons=3).moving_average_value(20)[0][-2]*1000) and float(realtime_data.data[i]['diff'][1]) > 0: #今天的量大於5日週或月均量, 目前要漲
           print i,'TWSE123'        #暴量長紅2天

           close_price = Stock(i).raw[-1][6]
           MA5 = Stock(i,mons=2).moving_average(5)[0][-1]
           MA10 = Stock(i,mons=2).moving_average(10)[0][-1]
           MA20 = Stock(i,mons=2).moving_average(20)[0][-1]
           Bias5 = (close_price-MA5)/MA5*100
           Bias10 = (close_price-MA10)/MA10*100
           Bias20 = (close_price-MA20)/MA20*100
           turnover_ration = float(Stock(i).raw[-1][1])/(float(rank_market_value()[i][3])*10000)*100
           try:
                vip_main_str = vip_main()[i][2]
           except:
                vip_main_str = "無資料"

           time_week = float(realtime_data.data[i]['volume_acc'])/float(Stock(i,mons=3).moving_average_value(5)[0][-2]*1000)         
           time_month = float(realtime_data.data[i]['volume_acc'])/float(Stock(i,mons=3).moving_average_value(20)[0][-2]*1000)

           try:
                fileopen.write(OTC_no_name[i].encode("UTF-8")+"("+i+")"+"TWSE"+","+"漲幅"+str(float(realtime_data.data[i]['diff'][1]))+"%"+","+"%.1f"%time_week+"倍週量"+","+ \
"%.1f"%time_month+"倍月量"+","+"成交張數"+str(realtime_data.data[i]['volume_acc'])+","+"殖利率" \
           +str(fields_otc()[i][2])+","+"收盤價"+str(close_price)+","+"週均線"+"%.1f"%Bias5+"%"+","+"雙週均價"+"%.1f"%Bias10+"%"\
+","+"月均價"+"%.1f"%Bias20+"%"+","+"發行"+rank_market_value()[i][3]+"萬張"+","+"市值"+rank_market_value()[i][4]+"億"+","+"上市"    \
+rank_market_value()[i][5]+"年"+","+rank_market_value()[i][6].encode("UTF-8")+","+"市值排名:"+rank_market_value()[i][0]+"/1548"+"," \
+"週轉率"+"%.3f"%turnover_ration+"%"+","+"政府機構"+vip_other()[i][1]+"%"+"橋外投資"+vip_other()[i][2]+"%"+"本國金融"+vip_other()[i][3]+"%" \
+"本國法人"+vip_other()[i][4]+"%"+"本國個人含董監"+vip_other()[i][5]+"%"+"董監持股"+vip_main_str+"\n")
                   
           except:
                pass

    except: # 回傳為None 或 資料不足導致ValueError
        pass





fileopen.close()                #關閉檔案


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




