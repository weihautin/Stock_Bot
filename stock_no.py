# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 00:43:39 2015

@author: tim
"""

from grs import TWSENo


twse_no = TWSENo()
twse_no.all_stock       # 所有股票名稱、代碼 type: dict
twse_no.all_stock_no    # 所有股票代碼 type: list
twse_no.all_stock_name  # 所有股票名稱 type: list
twse_no.industry_code   # 回傳類別代碼 type: dict
twse_no.industry_comps  # 回傳類別所屬股票代碼 type: dict
twse_no.search(u'中')   # 搜尋股票名稱，回傳 type: dict
twse_no.searchbyno(23)  # 搜尋股票代碼，回傳 type: dict
twse_no.last_update     # 回傳列表最後更新時間（非同步）type: str
