# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup
import os
from datetime import datetime
import time
import csv
from time import strftime


year =  strftime('%Y')


start = time.time()

content = "贏要衝,輸要縮."   #沒有辦法換行

time_now = datetime.now().strftime("%Y%m%d_%H%M%S") #今天的日期 ex:2015-0411

title = str(time_now+"__EPS") #Email郵件的標題 ex:2015-0411-選股機器人

realtime_txt = open("EPS.txt", 'w') #開啟檔案,w沒有該檔案就新增

year = str(int(year)-1911)

realtime_txt.write(year+"年第四季EPS"+"\n")
realtime_txt.write("代號  "+"   本季EPS 去年同期EPS 今年EPS累積 去年同期EPS累積"+"\n")


f = open('/home/tim/GMAIL.txt','r') #於前一個相對目錄中放置登入GMAIL帳號密碼,目的為了不再GitHub顯示出來.
ID = f.readline().strip('\n') #不包含換行符號\n
PW = f.readline().strip('\n')


with open('TWSE.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',') #以模組csv裡的函數reader來讀取csvfile變數，區隔符號為逗號(,)，讀取後存到readCSV變數裡
    for row in readCSV: #就readCSV裡的所有資料(以列為單位)
        print row[1]
        url = 'http://mops.twse.com.tw/mops/web/ajax_t164sb04?'\
        'encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&TYPEK=all&isnew=false&co_id='+row[0]+'&year='+'105'+'&season=04'

        try:
            time.sleep(10)
            response = urllib.urlopen(url)
            html = response.read()
            sp = BeautifulSoup(html.decode('utf-8'))  #cp950

            #print(sp)
            print url

            trs=sp.find_all('tr')
            for tr in trs:
                tds=tr.find_all('td')
                for td in tds:
                    if (td.get_text().strip()==u"基本每股盈餘") :
                        if (tds[1].get_text().strip()!=''):
                            print(row[0],year,'2',tds[1].get_text().strip())
                            print(row[0],year,'2',tds[3].get_text().strip())
            if response!= None:
                 realtime_txt.write(row[0]+" "+tds[1].get_text().strip()+" "+tds[3].get_text().strip()+"\n")

        except:
            pass

        

end = time.time()
elapsed = end - start
print( "Time taken: ", elapsed, "seconds.")
realtime_txt.write("Time taken: "+ str(elapsed) + " seconds.")

realtime_txt.close()


os.system('sendEmail -o \
 -f u160895@taipower.com.tw \
 -t "WEI <weihautin@gmail.com>" \
 -s smtp.gmail.com:587 \
 -xu %s \
 -xp %s \
 -u %s \
 -o message-file=/home/tim/EPS.txt \
 '%(ID, PW, title))

