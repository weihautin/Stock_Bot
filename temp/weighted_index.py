# -*- coding: utf-8 -*-
"""
計算盤後週月季年線
"""

import csv
import logging
import urllib3
from datetime import datetime
from cStringIO import StringIO
from dateutil.relativedelta import relativedelta
import os

try:
        os.remove("weighted_index.txt")
except OSError:
        pass

TWSE_HOST = 'http://www.twse.com.tw/'
TWSE_CONNECTIONS = urllib3.connection_from_url(TWSE_HOST)

#http://www.twse.com.tw/ch/trading/exchange/FMTQIK/FMTQIK2.php?STK_NO=&myear=2015&mmon=04&type=csv

#url = ('/ch/trading/exchange/STOCK_DAY/STOCK_DAY_print.php?genpage=genpage/Report201504/201504_F3_1_8_1101.php&type=csv')


class Twse_Weighted_Index(object):
    """大盤加權指數相關類別
    """
    def get_link(self, nowdatetime = datetime.today()):
        """設定證交所大盤加權指數盤後網址(抓取盤後csv檔案),網址如下
           http://www.twse.com.tw/ch/trading/exchange/FMTQIK/genpage/Report201504/201504_F3_1_2.php?STK_NO=&myear=2015&mmon=04
            :param datetime nowdatetime: 今天的日期
            :rtype: str (大盤盤後csv統計資料網址)
        """
        self.url = (
            '/ch/trading/exchange/' +
            'FMTQIK/FMTQIK2.php?STK_NO=&myear=' +
            '%(year)d&mmon=%(mon)02d' +
            '&type=csv') % {'year': nowdatetime.year,
                             'mon': nowdatetime.month }
        return self.url
                                    

    def serial_fetch(self,  month=15):
        """串連抓回來的各月大盤網頁資料
           :param int month: 欲取得的總月數
           :rtype: list 
           :returns: 各月大盤盤後資料
        """
        
        result = []
        for i in range(month):
            nowdatetime = datetime.today() - relativedelta(months=i) #產生不同月份的datetime資料
            tolist = self.to_list(nowdatetime)
            result = tolist + result
        return result
        
    def to_list(self, nowdatetime):
        """將抓到的csv大盤資料轉成list後回傳 
           :param int month: datetime nowdatetime: 今天的日期
           :returns: 該月大盤盤後資料(list)
        """
        
        self.url = self.get_link(nowdatetime) 
   
        logging.info(self.url)
        result = TWSE_CONNECTIONS.urlopen('GET', self.url)
        csv_files = csv.reader(StringIO(result.data))
        
        tolist = []

        for i in csv_files:
            i = [value.strip().replace(',', '') for value in i] #將逗點取消
            #[' 104/04/20', '4,912,281,564', '91,460,781,461', '835,649', '9,552.85', '-18.08']
            #['104/04/20', '4912281564', '91460781461', '835649', '9552.85', '-18.08']將逗點取代
        
            try:
                for value in (1, 2, 3, 4, 5, 6):
                    i[value] = float(i[value])
                    #['104/04/20', 4912281564.0, 91460781461.0, 835649.0, 9552.85, -18.08]                
            except (IndexError, ValueError):
                pass
            tolist.append(i)
        return tolist[2:-1] #將頭尾的標題文字去掉
        
    def Weighted_Index_average(self, nday, raw_data):
        """ 大盤加權指數的移動平均(均線)
            Input -->    nday : 要幾天平均線
                      raw_data: 原始分析資料
            Output--> 
        """
        Weighted_Index = []
        Weighted_Index_average = []

        for i in raw_data:
            Weighted_Index.append(i[4])
            
        for dummy in range(len(Weighted_Index) - int(nday) + 1): 
            Weighted_Index_average.append(round(sum(Weighted_Index[-nday:]) / nday, 3)) 
            Weighted_Index.pop()
        Weighted_Index_average.reverse()
        return Weighted_Index_average


if __name__ == "__main__":
#['104/04/20', 4912281564.0, 91460781461.0, 835649.0, 9552.85, -18.08]]
#    0日期         1成交股數       2成交金額    3成交筆數  4加權指數   5漲跌
    

    content = "贏要衝,輸要縮."   #沒有辦法換行
    time_now = datetime.now().strftime("%Y%m%d-%H%M") #今天的日期 ex:2015-0411
    title = str(time_now+"-盤後週月季年線") #Email郵件的標題 ex:2015-0411-選股機器人

    attachment = str(time_now)+'.txt' #附件名稱使用當日時間 ex:2015-0411.txt

    fileopen = open("weighted_index.txt", 'w') #開啟檔案,w沒有該檔案就新增

    f = open('/home/tim/GMAIL.txt','r') #於前一個相對目錄中放置登入GMAIL帳號密碼,目的為了不再GitHub顯示出來.
    ID = f.readline().strip('\n') #不包含換行符號\n:q

    PW = f.readline().strip('\n')

    a = Twse_Weighted_Index()
    #print a.serial_fetch(month=1)   

          
    
    print a.Weighted_Index_average(1,a.serial_fetch())# 印出每日收盤價格

    a8 = str(int(a.Weighted_Index_average(1,a.serial_fetch())[-1]))+'-'+'昨日收盤價***'
    
    print int(a.Weighted_Index_average(3,a.serial_fetch())[-1]),'三日均線'# 印出三日均線
    
    print int(a.Weighted_Index_average(5,a.serial_fetch())[-1]),'週線'# 印出週線
    
    print int(a.Weighted_Index_average(10,a.serial_fetch())[-1]),'雙週線'# 印出雙週線
    
    print int(a.Weighted_Index_average(20,a.serial_fetch())[-1]),'月線'# 印出月線
    
    print int(a.Weighted_Index_average(60,a.serial_fetch())[-1]),'季線'# 印出季線
    
    print int(a.Weighted_Index_average(120,a.serial_fetch())[-1]),'半年線'# 印出半年線
    
    print int(a.Weighted_Index_average(240,a.serial_fetch())[-1]),'年線'# 印出年線
  
    fileopen.write(str(int(a.Weighted_Index_average(3,a.serial_fetch())[-1]))+'-'+'三日均線'+'\n')
    a1 = str(int(a.Weighted_Index_average(3,a.serial_fetch())[-1]))+'-'+'三日均線***'

    fileopen.write(str(int(a.Weighted_Index_average(5,a.serial_fetch())[-1]))+'-'+'週線'+'\n')
    a2 = str(int(a.Weighted_Index_average(5,a.serial_fetch())[-1]))+'-'+'週線***'

    fileopen.write(str(int(a.Weighted_Index_average(10,a.serial_fetch())[-1]))+'-'+'雙週線'+'\n')
    a3 = str(int(a.Weighted_Index_average(10,a.serial_fetch())[-1]))+'-'+'雙週線***'

    fileopen.write(str(int(a.Weighted_Index_average(20,a.serial_fetch())[-1]))+'-'+'月線'+'\n')
    a4 = str(int(a.Weighted_Index_average(20,a.serial_fetch())[-1]))+'-'+'月線***'

    fileopen.write(str(int(a.Weighted_Index_average(60,a.serial_fetch())[-1]))+'-'+'季線'+'\n')
    a5 = str(int(a.Weighted_Index_average(60,a.serial_fetch())[-1]))+'-'+'季線***'

    fileopen.write(str(int(a.Weighted_Index_average(120,a.serial_fetch())[-1]))+'-'+'半年線'+'\n')
    a6 = str(int(a.Weighted_Index_average(120,a.serial_fetch())[-1]))+'-'+'半年線***'

    fileopen.write(str(int(a.Weighted_Index_average(240,a.serial_fetch())[-1]))+'-'+'年線'+'\n')
    a7 = str(int(a.Weighted_Index_average(240,a.serial_fetch())[-1]))+'-'+'年線***'


    content_1 = a8+a1+a2+a3+a4+a5+a6+a7

    fileopen.close() 
     

    os.system('sendEmail -o \
    -f u160895@taipower.com.tw \
    -t "WEI <weihautin@gmail.com>" u160895@taipower.com.tw \
    -s smtp.gmail.com:587 \
    -xu %s \
    -xp %s \
    -u %s \
    -o message-file=/home/tim/Stock_Bot/weighted_index.txt \
    '%(ID, PW, title))

    os.remove("weighted_index.txt")
   
"""
    os.system('sendEmail -o \
    -f u160895@taipower.com.tw \
    -t "WEI <weihautin@gmail.com>" u160895@taipower.com.tw \
    -s smtp.gmail.com:587 \
    -xu %s \
    -xp %s \
    -u %s \
    -m %s \
    -a %s \
    '%(ID, PW, title, content_1, attachment))
"""

    
    
    
    
    
  


    
