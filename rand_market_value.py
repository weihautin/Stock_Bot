# -*- coding: utf-8 -*-
"""
功能:抓取個股市值排名程式
網址:http://goodinfo.tw/StockInfo/StockList.asp?SHEET=%E5%85%AC%E5%8F%B8%E5%9F%BA%E6%9C%AC%E8%B3%87%E6%96%99&MARKET_CAT=%E7%86%B1%E9%96%80%E6%8E%92%E8%A1%8C&INDUSTRY_CAT=%E5%85%AC%E5%8F%B8%E7%B8%BD%E5%B8%82%E5%80%BC
GOOGLE : 上市市值排行
前置作業:需要把csv檔中頭尾相關中文標題先刪除
刪除：股價日,當日走勢,成交,漲跌,檔跌幅,成交張數,面值,成立年數,總經理
票面1股為10元，1000股的股票為一張，1億的股本代表1萬張的股票
"""


import csv

def market_value():
    """
    共有1548家上市櫃
    市值1000億排名前50名
    市值500億排前100
    市值100億排前300
    市值50億排前500
    市值20億排前1000
    市值10億排前1300
    市值5億排前1500
    回傳dict:[0排名,1名稱,2市場,3股本(億)(萬張),4市值(億),5上市年數,6產業別,7董事長]
    回傳dict:[40, 台泥utf8,上市, 369, 1541, 53.3, 水泥工業, 辜成允]
    EX: a['1101'] = ['40', u'\u53f0\u6ce5', u'\u4e0a\u5e02', '369', '1541', '53.3', u'\u6c34\u6ce5\u5de5\u696d', u'\u8f9c\u6210\u5141']
    """
    dic_market_value = {}
    f = open('/home/tim/Stock_Bot/update_csv/StockList_20150522.csv','r')
    for row in csv.reader(f):
        try:
            dic_market_value[row[1]]=[row[0],row[2].decode('UTF-8'),row[3].decode('UTF-8'),row[4],row[5],row[6],row[7].decode('UTF-8'),row[8].decode('UTF-8')]
        except:
            pass
    f.close()
    return dic_market_value 
    


if __name__ == "__main__":

    a = market_value()
    print a['1101']
    
