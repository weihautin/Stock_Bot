# -*- coding: utf-8 -*-
"""
抓取http://mops.twse.com.tw/mops/web/t05st10_ifrs公開資訊觀測站
各股累積營運情況
2013.01後採用IFRSs後之月營業收入資訊

@author: tim
"""


import urllib, re
import requests
import csv
import time
import datetime
#from datetime import datetime
import os

start = time.time()

#title = str("TWSE_每月營收_100") #Email郵件的標題 ex:2015-0411-選股機器人

realtime_txt = open("earn_money_100.txt", 'w') #開啟檔案,w沒有該檔案就新增
realtime_txt.write("ID 值利率 與去年月營收比較  與去年累積營收比較 "+"\n")

f = open('/home/tim/GMAIL.txt','r') #於前一個相對目錄中放置登入GMAIL帳號密碼,目的為了不再GitHub顯示出來.
ID = f.readline().strip('\n') #不包含換行符號\n
PW = f.readline().strip('\n')



def cumulative_revenues(co_id, yearmonth, year, month):
	"""
	輸入:
	co_id = '8383' 股票代碼
	yearmonth = '10312'
	year = 103
	month = '01'
	http://mops.twse.com.tw/mops/web/t05st10_ifrs
	回傳list:['目前累積營收增減百分比']
	"""
	r = requests.post("http://mops.twse.com.tw/mops/web/t05st10_ifrs")



	#選歷史資料後按搜尋
	payload = {
	'encodeURIComponent':'1',
	'run':'	Y',
	'step':'0',
	'yearmonth':yearmonth,
	'TYPEK':'sii',
	'co_id':co_id,
	'off':'1',
	'year':year,
	'month':month,
	'firstin':'true'}

	r = requests.get("http://mops.twse.com.tw/mops/web/t05st10_ifrs", params=payload)
	optionUrl = r.url
	html = urllib.urlopen(optionUrl)  #open file-like object
        regexp = re.compile(r"<TD class='even' style='text-align:right !important;'>&nbsp;(?P<file>.*)</TD></TR>")

        i = 0 #只抓第四筆符合資料

        data =[]
        for line in html.readlines():
		result = regexp.search(line)
		if result != None:
			money = result.group('file')
			i+=1
                if i==2:
                        data.append(money.split())
                        
		if i==4:
			data.append(money.split())
                        return data 


if __name__ == "__main__":
        #a = cumulative_revenues('2412','10609','106','09')
        today = datetime.date.today()
        first = today.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        year=str(int(lastMonth.strftime("%Y"))-1911)
        month=lastMonth.strftime("%m")
        year_month=year+month


        title = str("TWSE_"+month+"月營收_100") #Email郵件的標題 ex:2015-0411-選股機器人

        s = open('TWSE.csv',"rb").read().decode("big5",'replace').encode("utf8") # Big5 to Utf-8
        open('TWSE_utf8.csv',"wb").write(s)  # 令存utf-8檔案 


        count = 0
        print "與去年月營收比較  與去年累積營收比較"
        with open('TWSE_utf8.csv') as csvfile:
            csvfile = csvfile.readlines()[1:102]
            readCSV = csv.reader(csvfile, delimiter=',') #以模組csv裡的函數reader來讀取csvfile變數，區隔符號為逗號(,)，讀>取後存到readCSV變數裡
            for row in readCSV: #就readCSV裡的所有資料(以列為單位)
                try:
                    time.sleep(8)
                    a = cumulative_revenues(row[0],year_month,year,month)
                    if float(a[5][0]) >= 0 and float(a[6][0]) >= 0 and float(row[2]) >= 0: #年累積營收要大於0  值利率要大於3%
	                    realtime_txt.write(str(row[0])+"  "+str(row[1]).strip()+"    "+str(row[2])+"  "+str(a[5])+"  "+str(a[6])+"  "+"\n")
        	            print  row[0],row[1],row[2],a[5],a[6]
                            count+=1
                except:
                    pass

            realtime_txt.write("月與年營收皆成長公司共有"+str(count)+"間"+"\n")

	

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
 -o message-file=/home/tim/earn_money_100.txt \
 '%(ID, PW, title))


os.remove('earn_money_100.txt')


