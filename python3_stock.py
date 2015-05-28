# -*- coding: utf-8 -*-
"""
Created on Sun May 24 02:27:02 2015

@author: tim
"""

"""
import csv
import string
import codecs
import urllib.parse
import urllib.request
import configparser
import os
import datetime
import shutil
url="http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php"
values = {'download' : 'csv',
          'qdate' : '103/12/26',
          'selectType' : 'ALLBUT0999' }

data = urllib.parse.urlencode(values)
req= urllib.request.Request(url, data.encode('utf-8'))
response = urllib.request.urlopen(req)

file1=open("qooooooooo.csv","w")
for line in response.read().decode('CP950'):
    if len(line)>0:
        file1.writelines(line)
file1.close()

"""

"""
# 外資買賣超
import csv
import string
import codecs
import urllib.parse
import urllib.request
import configparser
import os
import datetime
import shutil
url="http://www.twse.com.tw/ch/trading/fund/TWT38U/TWT38U.php"
values = {'download' : 'csv',
          'qdate' : '103/12/26'}

data = urllib.parse.urlencode(values)
req= urllib.request.Request(url, data.encode('utf-8'))
response = urllib.request.urlopen(req)

file1=open("qooooooooo.csv","w")
for line in response.read().decode('CP950'):
    if len(line)>0:
        file1.writelines(line)
file1.close()

"""

# 三大法人買賣超http://www.twse.com.tw/ch/trading/fund/T86/print.php?edition=ch&filename=genpage/201505/20150522_2by_issue.dat&type=csv&select2=ALLBUT0999&qdate=20150522

