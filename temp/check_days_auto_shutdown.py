# -*- coding: utf-8 -*-
"""
判斷今天日否有開市
更改/grs/opendate.csv檔案,檔案內的日期為非開市日
週末為非開市日
依據 http://www.twse.com.tw/ch/trading/trading_days.php
"""
import os



from grs.twseopen import TWSEOpen
from datetime import datetime

open_or_not = TWSEOpen()

if open_or_not.d_day(datetime.today()) == True:
    print '今天有開市'
    
if open_or_not.d_day(datetime.today()) == False: #非開市日直接關機
    os.system('dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 "org.freedesktop.login1.Manager.PowerOff" boolean:true')



#open_or_not.d_day(datetime.today())        # 判斷今天是否開市
                                           # 回傳 True or False
#open_or_not.d_day(datetime(2012, 12, 22))  # 判斷 2012/12/22 是否開市



    
