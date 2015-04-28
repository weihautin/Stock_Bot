# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:22:32 2015

@author: tim
"""
# 請先安裝 sudo apt-get install sendemail

from grs import Stock
from grs import TWSENo
from weighted_index import Twse_Weighted_Index
import csv




Stock_no_name = TWSENo().all_stock  # 所有上市股票名稱與代碼字典 type: dict

stock_no_list = TWSENo().all_stock_no # 所有上市股票代碼

def twse_weight_percent():
    """
    回傳大盤加權指數佔比
    """
    stock_weight_percent = []
    f = open('stock_weighted1.csv','r')
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

    fileopen = open("cal_twse_weight.txt", 'w')
    
    a = twse_weight_percent()
    print a
    #print a['1101'][1], '殖益率'
    b = Twse_Weighted_Index() #大盤加權指數
    print int(b.Weighted_Index_average(1,b.serial_fetch(month=1))[-1])

    today_weight = b.Weighted_Index_average(1,b.serial_fetch(month=1))[-1]    
    
    # Stock('1101').raw[-1][-2] 漲跌點數
    # Stock('1101').raw[-1][4] 昨天收盤價
    # float(Stock('1101').raw[-1][-2]) / float(Stock('1101').raw[-1][4]) * today_weight * float(i[2]) / 100
    
    
    #for i in a:
    #    print i[0],i[1],i[2]
    
    total = 0    
    for i in a:
        contribution = 0
        contribution = float(Stock(i[0]).raw[-1][-2]) / float(Stock(i[0]).raw[-1][4]) * today_weight * float(i[2]) / 100
        total = total + contribution
        print i[0], contribution, total
        
    
    
    fileopen.write('\n\n\n上櫃公司股票篩選\n\n\n')
    
    fileopen.close()    #關閉檔案
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



