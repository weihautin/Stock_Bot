# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:22:25 2015

@author: tim
"""
from grs import TWTime
#from datetime import datetime

time_now = datetime.now().strftime("%Y-%m%d")


what_time = TWTime()
what_time.now()        # 顯示台灣此刻時間
what_time.localtime()  # 顯示當地此刻時間