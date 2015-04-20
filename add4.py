# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/tim/.spyder2/.temp.py
"""

import csv
import logging
import urllib3
from datetime import datetime
from cStringIO import StringIO
from dateutil.relativedelta import relativedelta

TWSE_HOST = 'http://www.twse.com.tw/'
TWSE_CONNECTIONS = urllib3.connection_from_url(TWSE_HOST)

#http://www.twse.com.tw/ch/trading/exchange/FMTQIK/FMTQIK2.php?STK_NO=&myear=2015&mmon=04&type=csv

#url = ('/ch/trading/exchange/STOCK_DAY/STOCK_DAY_print.php?genpage=genpage/Report201504/201504_F3_1_8_1101.php&type=csv')


class twse_history(object):
    def date(self, nowdatetime = datetime.today()):
        self.url = (
            '/ch/trading/exchange/' +
            'FMTQIK/FMTQIK2.php?STK_NO=&myear=' +
            '%(year)d&mmon=%(mon)02d' +
            '&type=csv') % {'year': nowdatetime.year,
                             'mon': nowdatetime.month }
        return self.url
                                    

    def serial_fetch(self,  month=3):
        
        result = []
        for i in range(month):
            nowdatetime = datetime.today() - relativedelta(months=i)
            tolist = self.to_list(nowdatetime)
            result = tolist + result
        return result
        
    def to_list(self, nowdatetime):
        self.url = self.date(nowdatetime)
        
        logging.info(self.url)
        result = TWSE_CONNECTIONS.urlopen('GET', self.url)
        csv_files = csv.reader(StringIO(result.data))
        logging.info(self.url)
        result = TWSE_CONNECTIONS.urlopen('GET', a.url)
        csv_files = csv.reader(StringIO(result.data))


        tolist = []

        for i in csv_files:
            i = [value.strip().replace(',', '') for value in i]
            #[' 104/04/20', '4,912,281,564', '91,460,781,461', '835,649', '9,552.85', '-18.08']
            #['104/04/20', '4912281564', '91460781461', '835649', '9552.85', '-18.08']將逗點取代
        
            try:
                for value in (1, 2, 3, 4, 5, 6):
                    i[value] = float(i[value])
                    #['104/04/20', 4912281564.0, 91460781461.0, 835649.0, 9552.85, -18.08]                
            except (IndexError, ValueError):
                pass
            tolist.append(i)
        return tolist[2:-1]
        

if __name__ == "__main__":
    
    a = twse_history()
    print a.serial_fetch(month=1)         
    print '123'
    
""" 
    logging.info(a.url)

    result = TWSE_CONNECTIONS.urlopen('GET', a.url)
    csv_files = csv.reader(StringIO(result.data))


    tolist = []

    for i in csv_files:
        i = [value.strip().replace(',', '') for value in i]
        #[' 104/04/20', '4,912,281,564', '91,460,781,461', '835,649', '9,552.85', '-18.08']
        #['104/04/20', '4912281564', '91460781461', '835649', '9552.85', '-18.08']將逗點取代
        
        try:
            for value in (1, 2, 3, 4, 5, 6):
                i[value] = float(i[value])
        #['104/04/20', 4912281564.0, 91460781461.0, 835649.0, 9552.85, -18.08]                
        except (IndexError, ValueError):
            pass
        tolist.append(i)
        #print tolist[2:-1] #把頭尾的標題文字去掉
        
"""
  

#result = []   
#for i in range(3):
#    result = tolist + result

#i = 4    
#nowdatetime = datetime.today() - relativedelta(months=i)


#month = 3
#for i in range(month):
#    print i
    

    