"""
執行結果為於執行目錄下,將產生一個**期交所每日期貨收盤資料.txt**文字檔
期交所盤後約14:30分,網站才更新今日大盤資料
故14:30前需要去抓昨天以前的資料
期交所網站http://www.taifex.com.tw/chinese/3/3_1_1.asp
假設查詢不到該日期,將會將網頁跳至今天的日期
"""
import urllib, re
import time
import os
from datetime import datetime
from time import strftime


f = open(u"stock_contri.txt",'w') #欲儲存資料的文字檔檔名

print u"正在連結期交所網站抓取資料，請稍等。抓取一個月的資料約10秒，需等待多久取決於抓取多少月份的資料"


optionUrl = "https://www.taifex.com.tw/chinese/9/9_7_1.asp"


html = urllib.urlopen(optionUrl)  #open file-like object


for line in html.readlines():
    regexp = re.compile(r"<TD align=middle>(?P<file>.*)</td>") #Compile a regular expression pattern, returning a pattern object., 成交價格
    result = regexp.search(line)
    if result != None:
        fileName = result.group('file')
        f.write('%s'%(fileName))
    
    

          

html.close()
f.close()




