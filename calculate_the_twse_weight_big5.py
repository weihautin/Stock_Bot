# -*- coding: utf-8 -*-
"""
計算各股票加權貢獻
"""
# 請先安裝 sudo apt-get install sendemail

import os
from grs import Stock
from grs import TWSENo
from weighted_index import Twse_Weighted_Index
import csv
from datetime import datetime




Stock_no_name = TWSENo().all_stock  # 所有上市股票名稱與代碼字典 type: dict

stock_no_list = TWSENo().all_stock_no # 所有上市股票代碼

def twse_weight_percent():
    """
    回傳大盤加權指數佔比
    """
    stock_weight_percent = []
    f = open('/home/tim/Stock_Bot/stock_weighted_20150428.csv','r')
    for row in csv.reader(f):
        try:
            #stock_weight_percent.append([row[1],row[2].decode('UTF-8'), row[3]])
            stock_weight_percent.append([row[1], row[2], row[3]])
        except:
            pass
    f.close()
    return stock_weight_percent

if __name__ == "__main__":
    pass
    
    content = "贏要衝,輸要縮."   #沒有辦法換行

    time_now = datetime.now().strftime("%Y%m%d-%H%M") #今天的日期 ex:2015-0411

    title = str(time_now+"-盤後各股加權貢獻") #Email郵件的標題 ex:2015-0411-選股機器人

    attachment = str(time_now)+'.csv' #附件名稱使用當日時間 ex:2015-0411.txt

    fileopen = open(attachment, 'w') #開啟檔案,w沒有該檔案就新增

    f = open('/home/tim/GMAIL.txt','r') #於前一個相對目錄中放置登入GMAIL帳號密碼,目的為了不再GitHub顯示出來.
    ID = f.readline().strip('\n') #不包含換行符號\n:q

    PW = f.readline().strip('\n')

    a = twse_weight_percent()
    #print a
    
    
    
    
    #print a['1101'][1], '殖益率'
    b = Twse_Weighted_Index() #大盤加權指數
    #print int(b.Weighted_Index_average(1,b.serial_fetch(month=1))[-1])

    today_weight = b.Weighted_Index_average(1,b.serial_fetch(month=2))[-1]    # -1今天收盤 -2昨天收盤
    
    # Stock('1101').raw[-1][-2] 漲跌點數
    # Stock('1101').raw[-1][4] 昨天收盤價
    # float(Stock('1101').raw[-1][-2]) / float(Stock('1101').raw[-1][4]) * today_weight * float(i[2]) / 100
    
    
    #for i in a:
    #    print i[0],i[1],i[2]

    fileopen.write("各股加權貢獻依據2015年4月28日下的權重計算"+"\n")
    
    total = 0    
    for i in a:
       
        contribution = 0
        try:
            contribution = float(Stock(i[0]).raw[-1][-2]) / float(Stock(i[0]).raw[-2][-3]) * today_weight * float(i[2]) / 100
        except:
            pass #抓到非數字跳過
        total = total + contribution
        
        print i[0],i[1],contribution,total      
        
        
        fileopen.write(str(i[0])+','+str(i[1])+','+str(contribution)+','+ str(total)+"\n")
        
    fileopen.close()    #關閉檔案

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

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



