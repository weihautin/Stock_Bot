import urllib, re, os

#要自己手動建立目錄path

path = "C:\\test\\"  #儲存檔案的路徑
optionUrl = "http://www.taifex.com.tw/chinese/3/3_2_4.asp"  #開啟期貨網頁
downloadUrl = "http://www.taifex.com.tw/OptionsDailyDownload/" #下載檔案的網址

html = urllib.urlopen(optionUrl)  #open file-like object

regexp = re.compile(r"/OptionsDailyDownload/(?P<file>.*)\"><img") #Compile a regular expression pattern, returning a pattern object.
# 正規表示式 (?P<file>.*)  一個括號裡面的東西為一個group


print "Download to " + path #顯示下載到哪邊


for line in html.readlines():
  result = regexp.search(line)
    #search(string[, pos[, endpos]]) --> match object or None.
    #Scan through string looking for a match, and return a corresponding
    #MatchObject instance. Return None if no position in the string matches.
  if result != None:
    fileName = result.group('file')  #參數可以打 'file'  或只打數字 1  變數regexp一個括號裡面的東西為一個group
    # MatchObject instances support the following methods and attributes:
    # http://docs.python.org/release/2.5.2/lib/match-objects.html
    #

    if os.path.exists(path + fileName):
        continue  #如果已經有這個檔案則跳過
    print fileName
    try:
      urllib.urlretrieve(downloadUrl + fileName, path+fileName)
      #參數1來源檔案  ;參數2要儲存的路徑
    except IOError:
       #無法下載發生錯誤之類的
      print "fault"

html.close()

os.system("pause")

print "Done."