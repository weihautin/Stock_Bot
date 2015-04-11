# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:24:50 2015

@author: tim
"""

from grs import BestFourPoint
from grs import Stock
from grs import TWSENo

stock_no_list = TWSENo().all_stock_no

"""原始程式
for i in stock_no_list:
    try:
        best_point, info = BestFourPoint(Stock(i)).best_four_point()
        if best_point:  # 買點
            print 'Buy: {0} {1}'.format(i, info)
        else:   # 賣點
            print 'Sell: {0} {1}'.format(i, info)
    except:     # 不作為或資料不足
        print 'X: {0}'.format(i)
"""

fileopen = open('whichone.txt','w') #開啟檔案,w沒有該檔案就新增

for i in stock_no_list:
    try:
        best_point, info = BestFourPoint(Stock(i)).best_four_point()
        if best_point:  # 買點
            print 'Buy: {0} {1}'.format(i, info)
            fileopen.write('Buy: {0} {1}\n'.format(i, info))               #寫入 p的內容
    except:     # 不作為或資料不足
        pass
    
fileopen.close()                #關閉檔案