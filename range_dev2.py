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
from grs import TWSENo
from grs import OTCNo

start = time.time() #記錄程式執行後的開始時間

stock_no_list = TWSENo().all_stock_no # 所有上市股票代碼

OTC_no_list = OTCNo().all_stock_no # 所有上櫃股票代碼

Stock_no_name = TWSENo().all_stock # 所有上市股票名稱與代碼字典 type: dict


f = open(u"range.txt",'w') #欲儲存資料的文字檔檔名
f.write("人數	股數	佔集保庫存數比例 (%)\n") #文字檔標頭

#stock_No_total = [1101,1102,2330,2412]
fetch_month = [20150302,20150430,20150522]

print u"正在連結期交所網站抓取資料，請稍等。抓取一個月的資料約10秒，需等待多久取決於抓取多少月份的資料"

tmp = []
owner = {} #儲存歷史資料

for k in TWSENo().all_stock_no:
	owner[k]=[]

# 年月日迴圈
for stock_No in TWSENo().all_stock_no:
    stock_No = str(stock_No)
    for stock_date in fetch_month:
	stock_date = str(stock_date)
	         
        print  # 每連結一天,於螢幕列印該天日期.
	print stock_No, stock_date


        optionUrl = "http://www.tdcc.com.tw/smWeb/QryStock.jsp?SCA_DATE="+stock_date+"&SqlMethod=StockNo&StockNo="+stock_No+"&sub=%ACd%B8%DF" #連結集保戶股權分散表該天網頁

        html = urllib.urlopen(optionUrl)  #open file-like object

        #regexp = re.compile(r"<TD align=right class=\"12bk\">(?P<file>.*)</TD>") #Compile a regular expression pattern, returning a pattern object., 成交價格

	regexp = re.compile(r"<td align=\"right\">(?P<file>.*)</td>")

        # 正規表示式 (?P<file>.*)  一個括號裡面的東西為一個group
                     
        i = 0 #只抓前六筆符合的資料(開盤價 最高價 最低價  最後成交價 成交量  未沖銷契約量)
	tmp = [] #清空
        for line in html.readlines():
                result = regexp.search(line)

                #search(string[, pos[, endpos]]) --> match object or None.
                #Scan through string looking for a match, and return a corresponding
                #MatchObject instance. Return None if no position in the string matches.
                                                          
                if result != None:   #列假日與國定假日都抓不到資料為None
                    fileName = result.group('file')  #參數可以打 'file'  或只打數字 1  變數regexp一個括號裡面的東西為一個group
                    # MatchObject instances support the following methods and attributes:
                    # http://docs.python.org/release/2.5.2/lib/match-objects.html
                    i+=1

                    f.write('%-15s'%(fileName)) #儲存價格資料
                    tmp.append(fileName)
                           

                if i == 48:
                    owner[stock_No].append(tmp)
		    break 
	

        html.close()
        
f.close()



  

more_tmp=[]


for m in owner.keys():
    try:
        if float(owner[m][-1][-3].replace(',', '')) > float(owner[m][-2][-3].replace(',', '')) > float(owner[m][-3][-3].replace(',', '')):
            tmp = (float(owner[m][-1][-3].replace(',', ''))-float(owner[m][-3][-3].replace(',', '')))/float(owner[m][-3][-3].replace(',', ''))*100
            print  Stock_no_name[m],"(",m,")",'股東多了',float(owner[m][-1][-3].replace(',', ''))-float(owner[m][-3][-3].replace(',', '')),"人","目前總股東",float(owner[m][-1][-3].replace(',', '')),"人,約多了","%.1f"%tmp,"%人數"
            more_tmp.append(m)
    except:
        pass
        

less_more=[]        
for m in owner.keys():
    try:
        if float(owner[m][-1][-3].replace(',', '')) < float(owner[m][-2][-3].replace(',', '')) < float(owner[m][-3][-3].replace(',', '')):
            tmp = (float(owner[m][-3][-3].replace(',', ''))-float(owner[m][-1][-3].replace(',', '')))/float(owner[m][-3][-3].replace(',', ''))*100
            print  Stock_no_name[m],"(",m,")",'股東少了',float(owner[m][-3][-3].replace(',', ''))-float(owner[m][-1][-3].replace(',', '')),"人","目前總股東",float(owner[m][-1][-3].replace(',', '')),"人,約少了","%.1f"%tmp,"%人數"
            less_more.append(m)
    except:
        pass
        

big_tmp = []

for n in owner.keys():
    if owner[n][-1][-4] > owner[n][-2][-4] > owner[n][-3][-4]:
        tmp = (float(owner[n][-1][-4])-float(owner[n][-3][-4]))*float(owner[n][-1][-2].replace(',', ''))/100/1000
        print Stock_no_name[n],"(",n,")",'大股東持股增加',float(owner[n][-1][-4])-float(owner[n][-3][-4]),"%","目前總股數",owner[n][-1][-2],"約增加","%.0f"%tmp,"張"
        big_tmp.append(n)
        
        


        
big_tmp_less = []

for n in owner.keys():
    try:
        if owner[n][-1][-4] < owner[n][-2][-4] < owner[n][-3][-4]:
            tmp = (float(owner[n][-3][-4])-float(owner[n][-1][-4]))*float(owner[n][-1][-2].replace(',', ''))/100/1000
            print  Stock_no_name[n],"(",n,")",'大股東持股減少',float(owner[n][-3][-4])-float(owner[n][-1][-4]),"%","目前總股數",owner[n][-1][-2],"約減少","%.0f"%tmp,"張"
            big_tmp_less.append(n)
    except:
        pass


"""
s1 = set(big_tmp_less)
s2 = set(more_tmp)
print s1.intersection(s2)
print list(s1.intersection(s2))
"""
        
        

# owner['1102'][-1][-4] 
#              [最近月份][內容]
# 內容 -1 100.0
# -2 股數
# -3 總人數
# -4 買1000張以上股東%數






