# -*- coding: utf-8 -*-
"""
功能:抓取個股殖利率程式
網址: http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU_d.php
前置作業:需要把csv檔中頭尾相關中文標題先刪除
"""


import csv

def yields():
    """
    回傳dict:[股票名稱, 本益比, 殖利率(%), 股價淨值比]
    回傳dict:[台泥utf8, '14.93', '5.69', '1.37']
    EX: a['1101'] = [u'\u53f0\u6ce5', '14.93', '5.69', '1.37']
    """
    twse_yields = {}
    f = open('BWIBBU_d20150422.csv','r')
    for row in csv.reader(f):
        try:
            twse_yields[row[0]]=[row[1].decode('Big5'),row[2],row[3],row[4]]
        except:
            pass
    f.close()
    return twse_yields
    


if __name__ == "__main__":

    a = yields()
    print a['1101']
    
