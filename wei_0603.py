# -*- coding: utf-8 -*-
"""
抓取http://mops.twse.com.tw/mops/web/t05st10_ifrs公開資訊觀測站
各股累積營運情況
2013.01後採用IFRSs後之月營業收入資訊

@author: tim
"""


import urllib, re
import requests


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
        for line in html.readlines():
		result = regexp.search(line)
		if result != None:
			money = result.group('file')
			i+=1
		if i==4:
			return money.split()


if __name__ == "__main__":
	a = cumulative_revenues('2412','10212','102','12')
	print a

	


