# -*- coding: utf-8 -*-
"""
功能:抓取個股殖利率程式
網址: http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU_d.php
前置作業:需要把csv檔中頭尾相關中文標題先刪除
"""


import csv

def stock_buy_sell_oneday():
    '''
    回傳dict:[股票名稱, 本益比, 殖利率(%), 股價淨值比]
    回傳dict:[台泥utf8, '14.93', '5.69', '1.37']
    EX: a['1101'] = [u'\u53f0\u6ce5', '14.93', '5.69', '1.37']
    '''
    buy_sell_oneday_dict = {}
    f = open('TWTB4U_20150424.csv','r')
    for row in csv.reader(f):
        try:
            buy_sell_oneday_dict[row[0].strip()]=[row[1].decode('UTF-8').strip(),row[2].strip()]
        except:
            pass
    f.close()
    return buy_sell_oneday_dict 
    

if __name__ == "__main__":

    a = stock_buy_sell_oneday()
    print a['9921'][0]
    print a['9921'][1]  #回傳Y表示暫停現股賣出後現款買進當沖註記

    



"""
twse_yields = {}
f = open('TWTB4U_20150424.csv','r')
for row in csv.reader(f):
    print row
    try:
        twse_yields[row[0].strip()]=[row[1].decode('Big5').strip(),row[2].strip()]
	print type(row[0])
	print '123'
    except:
        pass
f.close()

"""







