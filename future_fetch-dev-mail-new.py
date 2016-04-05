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
import datetime
#from datetime import datetime
from time import strftime


start = time.time() #記錄程式執行後的開始時間
today = strftime('%Y/%m/%d')
hour = strftime('%H%M')
year =  strftime('%Y')
month = strftime('%m')
day = strftime('%d')

# 1430下午兩點半以前抓昨天以前的資料,1430以後抓今天以前的資料
if int(hour) < 1430:

    day=int(day) #為何要抓昨天以前即前天資料? 不需要因為後段程式會抓今天的資料,尾部要抓今天資料是因為前半部遇到
    #抓不到日期會跳到今天資料, 所以有設定條件日今天日期則Break跳出迴圈
    if day < 9: #幫日期加一個零 => 01 02 ~ 09
        download_date = year+'/'+month+'/'+'0'+str(day)
    else:
	download_date = year+'/'+month+'/'+str(day)
else:
    
    day=int(day)
    if day < 9: #幫日期加一個零 => 01 02 ~ 09
        download_date = year+'/'+month+'/'+'0'+str(day)
    else:
        download_date = year+'/'+month+'/'+str(day)
    
    download_date = today


f = open(u"today_future.txt",'w') #欲儲存資料的文字檔檔名
f.write("開盤價         最高價         最低價         最後成交價     成交量         未沖銷契約量   日期\n") #文字檔標頭






#fetch_year = [int(year)] # 想要哪何年資料,用逗號分隔
#fetch_month = [int(month)-4,int(month)]   # 想要哪何月資料,用逗號分隔
fetch_year = [2016]
fetch_month = [2]




someday = datetime.date.today()


date_tmp = []

while (someday >= datetime.date.today()-datetime.timedelta(days = 120)) :
    # print out with date format : YYYYMMDD, example : 2014-09-20
    print str(someday.strftime("%Y-%m-%d"))
    
    date_tmp.append(someday.strftime("%Y-%m-%d"))
    
    # minus, timedelta(days = 1)
    someday -= datetime.timedelta(days = 1)






print u"正在連結期交所網站抓取資料，請稍等。抓取一個月的資料約10秒，需等待多久取決於抓取多少月份的資料"
tmp = []
future_list = [] #儲存歷史資料



for  ii in date_tmp:
       
            print ii.split('-')[0],ii.split('-')[1],ii.split('-')[2] # 每連結一天,於螢幕列印該天日期.
            optionUrl = "http://www.taifex.com.tw/chinese/3/3_1_1.asp?goday=&syear="+ii.split('-')[0]+"&smonth="+ii.split('-')[1]+"&sday="+ii.split('-')[2]+"&COMMODITY_ID=TX"  #連結期交所該天網頁

            html = urllib.urlopen(optionUrl)  #open file-like object

            regexp = re.compile(r"<TD align=right class=\"12bk\">(?P<file>.*)</TD>") #Compile a regular expression pattern, returning a pattern object., 成交價格
            check_date = re.compile(r"<h3 align=\'left\'>日期：(?P<file>.*)</h3>") # 該網頁的日期
           
            # 正規表示式 (?P<file>.*)  一個括號裡面的東西為一個group
                     
            i = 0 #只抓前六筆符合的資料(開盤價 最高價 最低價  最後成交價 成交量  未沖銷契約量)
            for line in html.readlines():
                result = regexp.search(line)
                date_ck = check_date.search(line)
                #search(string[, pos[, endpos]]) --> match object or None.
                #Scan through string looking for a match, and return a corresponding
                #MatchObject instance. Return None if no position in the string matches.
                if date_ck != None:  #輸入不正確日期,會連結到今天的網頁
                    tmp1 = date_ck.group('file')  #參數可以打 'file'  或只打數字 1  變數regexp一個括號裡面的東西為一個group
                    if tmp1 == download_date: # 假設網頁是今天跳出for迴圈,不儲存資料.期交所網站輸入不正確的日期會跳到今天日期的網頁
# http://www.taifex.com.tw/chinese/3/3_1_1.asp?goday=&syear=2015&smonth=5&sday=7&COMMODITY_ID=TX
                        break
                                                          
                if result != None:   #列假日與國定假日都抓不到資料為None
                    fileName = result.group('file')  #參數可以打 'file'  或只打數字 1  變數regexp一個括號裡面的東西為一個group
                    # MatchObject instances support the following methods and attributes:
                    # http://docs.python.org/release/2.5.2/lib/match-objects.html
                    i+=1
                                        
                    f.write('%-15s'%(fileName)) #儲存價格資料
                    tmp.append(fileName)
	            #future_list.append([fileName])
                           
                if i >= 6 :  #只抓前六筆符合的資料(開盤價 最高價 最低價  最後成交價 成交量  未沖銷契約量),超過前六筆資料後列印日期與跳出for迴圈
                    tmp.append('%s-%s-%s'%(ii.split('-')[0],ii.split('-')[1],ii.split('-')[2]))
                    future_list.append(tmp)
                    tmp = []
                    f.write('%s-%s-%s'%(ii.split('-')[0],ii.split('-')[1],ii.split('-')[2]))
                    f.write('\n')
                    break
           
          
            html.close()
        
#f.close()




# 今天的日期
iyear =  strftime('%Y')
imonth = strftime('%m')
date = strftime('%d')



tmp = []
optionUrl = "http://www.taifex.com.tw/chinese/3/3_1_1.asp?goday=&syear="+iyear+"&smonth="+imonth+"&sday="+date+"&COMMODITY_ID=TX"  #連結期交所該天網頁

html = urllib.urlopen(optionUrl)  #open file-like object

regexp = re.compile(r"<TD align=right class=\"12bk\">(?P<file>.*)</TD>") #Compile a regular expression pattern, returning a pattern object., 成交價格
check_date = re.compile(r"<h3 align=\'left\'>日期：(?P<file>.*)</h3>") # 該網頁的日期
     
# 正規表示式 (?P<file>.*)  一個括號裡面的東西為一個group
     
i = 0 #只抓前六筆符合的資料(開盤價 最高價 最低價  最後成交價 成交量  未沖銷契約量)
for line in html.readlines():
    result = regexp.search(line)
    date_ck = check_date.search(line)
    #search(string[, pos[, endpos]]) --> match object or None.
    #Scan through string looking for a match, and return a corresponding
    #MatchObject instance. Return None if no position in the string matches.


    if result != None:   #列假日與國定假日都抓不到資料為None
        fileName = result.group('file')  #參數可以打 'file'  或只打數字 1  變數regexp一個括號裡面的東西為一個group
        i+=1

        f.write('%-15s'%(fileName)) #儲存價格資料
        tmp.append(fileName)
        #future_list.append([fileName])

    if i >= 6 :  #只抓前六筆符合的資料(開盤價 最高價 最低價  最後成交價 成交量  未沖銷契約量),超過前六筆資料後列印日期與跳出for迴圈
        tmp.append('%s-%s-%s'%(iyear,imonth,date))
        future_list.append(tmp)
        f.write('%s-%s-%s'%(iyear,imonth,date))
        tmp = []
        break



#i+=1
html.close()
f.close()




future_file = open(u"calculate_future_average.txt",'w')

future_file.write("今天期貨收盤價==> %d"%(int(future_list[0][3]))+"\n")

########
total = 0  #三日均價
index = 0
average_count = 1
while average_count <= 3:
	total = total + float(future_list[index][3])
	index = index + 1
	average_count+=1
	
print "3日平均價==> %f"%(total/3)
	
future_file.write("期貨3日均價==> %d"%(total/3)+"\n")


########

high_price = []  #三日內最高價
index = 0
average_count = 1 
while average_count <= 3:
        high_price.append(float(future_list[index][1]))
        index = index + 1 
        average_count+=1
     
print "期貨3日內最高價==> %d"%(max(high_price))
            
future_file.write("期貨3日內最高價==> %d"%(max(high_price))+"\n")

########
total = 0  #三日內最高價均價
index = 0
average_count = 1
while average_count <= 3:
        total = total + float(future_list[index][1])
        index = index + 1
        average_count+=1

print "期貨3日內最高價均價==> %d"%(total/3)

future_file.write("期貨3日內最高價均價==> %d"%(total/3)+"\n")

########

low_price = []  #三日內最低價
index = 0
average_count = 1 
while average_count <= 3:
        low_price.append(float(future_list[index][2]))
        index = index + 1 
        average_count+=1
     
print "期貨3日內最低價==> %d"%(min(low_price))
     
future_file.write("期貨3日內最低價==> %d"%(min(low_price))+"\n")
########

total = 0  #三日內最低價均價
index = 0
average_count = 1
while average_count <= 3:
        total = total + float(future_list[index][2])
        index = index + 1
        average_count+=1

print "期貨3日內最低價均價==> %d"%(total/3)

future_file.write("期貨3日內最低價均價==> %d"%(total/3)+"\n")

########################################################################################

future_file.write("\n\n==============================================\n\n")


low_price = []  #5日內最低價
index = 0
average_count = 1 
while average_count <= 5: 
        low_price.append(float(future_list[index][2]))
        index = index + 1 
        average_count+=1

print "期貨5日內最低價==> %d"%(min(low_price))

future_file.write("期貨5日內最低價==> %d"%(min(low_price))+"\n")





high_price = []  #5日內最高價
index = 0
average_count = 1 
while average_count <= 5: 
        high_price.append(float(future_list[index][1]))
        index = index + 1 
        average_count+=1

print "期貨5日內高最價==> %d"%(max(high_price))

future_file.write("期貨5日內最高價==> %d"%(max(high_price))+"\n")


low_price = []  #10日內最低價
index = 0
average_count = 1
while average_count <= 10:  
        low_price.append(float(future_list[index][2]))
        index = index + 1
        average_count+=1

print "期貨10日內最低價==> %d"%(min(low_price))

future_file.write("期貨10日內最低價==> %d"%(min(low_price))+"\n")





high_price = []  #10日內最高價
index = 0
average_count = 1
while average_count <= 10: 
        high_price.append(float(future_list[index][1]))
        index = index + 1
        average_count+=1

print "期貨10日內高最價==> %d"%(max(high_price))

future_file.write("期貨10日內最高價==> %d"%(max(high_price))+"\n")



low_price = []  #20日內最低價
index = 0
average_count = 1
while average_count <= 20:
        low_price.append(float(future_list[index][2]))
        index = index + 1
        average_count+=1

print "期貨20日內最低價==> %d"%(min(low_price))

future_file.write("期貨20日內最低價==> %d"%(min(low_price))+"\n")





high_price = []  #20日內最高價
index = 0
average_count = 1
while average_count <= 20:
        high_price.append(float(future_list[index][1]))
        index = index + 1
        average_count+=1

print "期貨20日內高最價==> %d"%(max(high_price))

future_file.write("期貨20日內最高價==> %d"%(max(high_price))+"\n")



low_price = []  #40日內最低價
index = 0
average_count = 1
while average_count <= 40:
        low_price.append(float(future_list[index][2]))
        index = index + 1
        average_count+=1

print "期貨40日內最低價==> %d"%(min(low_price))

future_file.write("期貨40日內最低價==> %d"%(min(low_price))+"\n")





high_price = []  #40日內最高價
index = 0
average_count = 1
while average_count <= 40:
        high_price.append(float(future_list[index][1]))
        index = index + 1
        average_count+=1

print "期貨40日內高最價==> %d"%(max(high_price))

future_file.write("期貨40日內最高價==> %d"%(max(high_price))+"\n")


low_price = []  #60日內最低價
index = 0
average_count = 1
while average_count <= 60:
        low_price.append(float(future_list[index][2]))
        index = index + 1
        average_count+=1

print "期貨60日內最低價==> %d"%(min(low_price))

future_file.write("期貨60日內最低價==> %d"%(min(low_price))+"\n")





high_price = []  #60日內最高價
index = 0
average_count = 1 
while average_count <= 60: 
        high_price.append(float(future_list[index][1]))
        index = index + 1 
        average_count+=1

print "期貨60日內高最價==> %d"%(max(high_price))

future_file.write("期貨60日內最高價==> %d"%(max(high_price))+"\n")


print u"抓取資料完成"

end = time.time() # 紀錄程式執行完的結束時間
elapsed = end - start # 總程式執行時間

print u"總共花費", elapsed, u"秒."

# 輸入 future_list 這個變數可查到抓回來的資料

# if tmp1 == download_date: 假設網頁是今天跳出for迴圈,不儲存資料.期交所網站輸入不正確的日期會跳到今天日期的網頁

    

future_file.close()





content = "風險管控,操作紀律."   #沒有辦法換行
#time_now = datetime.now().strftime("%Y%m%d-%H%M") #今天的日期 ex:2015-0411
title = str("盤後期貨週月季最高最低價") #Email郵件的標題 ex:2015-0411-選股機器人

attachment = 'calculate_future_average.txt' #附件名稱使用當日時間 ex:2015-0411.txt

f = open('/home/tim/GMAIL.txt','r') #於前一個相對目錄中放置登入GMAIL帳號密碼,目的為了不再GitHub顯示出來.
ID = f.readline().strip('\n') #不包含換行符號\n:q

PW = f.readline().strip('\n')


os.system('sendEmail -o \
-f u160895@taipower.com.tw \
-t "WEI <weihautin@gmail.com>" u160895@taipower.com.tw \
-s smtp.gmail.com:587 \
-xu %s \
-xp %s \
-u %s \
-o message-file=/home/tim/Stock_Bot/calculate_future_average.txt \
'%(ID, PW, title))





