# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:48:54 2015

@author: tim
"""
import os



from grs.twseopen import TWSEOpen
from datetime import datetime

open_or_not = TWSEOpen()

if open_or_not.d_day(datetime.today()) == True:
    print '123'
    
if open_or_not.d_day(datetime.today()) == False: #非開市日直接關機
    os.system('dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 "org.freedesktop.login1.Manager.PowerOff" boolean:true')



#open_or_not.d_day(datetime.today())        # 判斷今天是否開市
                                           # 回傳 True or False
#open_or_not.d_day(datetime(2012, 12, 22))  # 判斷 2012/12/22 是否開市



    
