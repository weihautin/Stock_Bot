# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:22:25 2015

@author: tim
"""

from grs import Stock

stock = Stock('1307', twse=True)                         # 擷取台化股價1101'

"""
print stock.moving_average(5)                 # 計算五日均價與持續天數
print stock.moving_average_value(5)           # 計算五日均量與持續天數
print stock.moving_average_bias_ratio(5, 10)  # 計算五日、十日乖離值與持續天數

from grs import TWSENo


twse_no = TWSENo()
a = twse_no.all_stock       # 所有股票名稱、代碼 type: dict
twse_no.all_stock_no    # 所有股票代碼 type: list
twse_no.all_stock_name  # 所有股票名稱 type: list
twse_no.industry_code   # 回傳類別代碼 type: dict
twse_no.industry_comps  # 回傳類別所屬股票代碼 type: dict
twse_no.search(u'中')   # 搜尋股票名稱，回傳 type: dict
twse_no.searchbyno(23)  # 搜尋股票代碼，回傳 type: dict
twse_no.last_update     # 回傳列表最後更新時間（非同步）type: str
"""
