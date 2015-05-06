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
from csvv import yields as fields #TWSE殖益率
from csvv import yields_otc as fields_otc #OTC殖益率
from sell_buy_immediately import stock_buy_sell_oneday as oneday #是否為現股當充
#from grs import yields as fields
#from grs import yields_otc as fields_otc
#from grs import stock_buy_sell_oneday as oneday


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


realtime_data = RealtimeTWSE('1101')

#fileopen.write("股票",",","100",",","倍週均量",",","成交張數",",","殖利率","100",",","倍月均量")





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




