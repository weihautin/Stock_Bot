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
    f = open('./update_csv/BWIBBU_d20151026.csv','r')
    for row in csv.reader(f):
        try:
            twse_yields[row[0]]=[row[1].decode('Big5'),row[2],row[3],row[4]]
        except:
            pass
    f.close()
    return twse_yields
    
def yields_otc():
    """
    https://www.tpex.org.tw/web/stock/aftertrading/peratio_analysis/pera.php?l=zh-tw
    回傳dict:[股票名稱, 本益比, 殖利率(%), 股價淨值比]
    回傳dict:[台泥utf8, '14.93', '5.69', '1.37']
    EX: a['1101'] = [u'\u53f0\u6ce5', '14.93', '5.69', '1.37']
    """
    twse_yields = {}
    f = open('./update_csv/pera_1041026.csv','r')
    for row in csv.reader(f):
        try:
            twse_yields[row[0]]=[row[1].decode('Big5'),row[2],row[3],row[4]]
        except:
            pass
    f.close()
    return twse_yields

def vip_other():
    """ 
    回傳dict:[持股資料年度	政府機構()	僑外投資()	本國金融機構()	本國法人()	本國個人()]
    """
    vip_other_return = {}
    f = open('./update_csv/Vip_others.csv','r')
    for row in csv.reader(f):
        try:
            vip_other_return[row[1]]=[row[3],row[4],row[5],row[6],row[7],row[8]]
        except:
            pass
    f.close()
    return vip_other_return 

def vip_main():
    """ 
    回傳dict:[名稱	持股資料月份	全體董監持股(%)	全體董監質押(%) ]
    """
    vip_main_return = {}
    f = open('./update_csv/Vip_main.csv','r')
    for row in csv.reader(f):
        try:
            vip_main_return[row[0]]=[row[1],row[2],row[3],row[4]]
        except:
            pass
    f.close()
    return vip_main_return


if __name__ == "__main__":

    a = vip_main()
    print a['1101']
    
