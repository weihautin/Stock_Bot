#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime #from datetime import datetime

import smtplib
import email.MIMEMultipart
import email.MIMEText
import email.MIMEBase
import os.path


time_now = datetime.now().strftime("%Y-%m%d")


From = "u160895@taipower.com.tw"
To = "weihautin@gmail.com"

 
server = smtplib.SMTP("smtp.taipower.com.tw")
server.login("ID","PASSWORD")      #仅smtp服务器需要验证时

# 開啟預定傳的內容
f = open('requirements.txt', 'r')
content = f.read()
f.close()


# 构造MIMEMultipart对象做为根容器
main_msg = email.MIMEMultipart.MIMEMultipart()
 
# 构造MIMEText对象做为邮件显示内容并附加到根容器
text_msg = email.MIMEText.MIMEText(content) #傳送預定的內容
main_msg.attach(text_msg)



"""
# 构造MIMEBase对象做为文件附件内容并附加到根容器
contype = 'application/octet-stream'
maintype, subtype = contype.split('/', 1)
"""

'''
## 读入文件内容并格式化
data = open("requirements.txt", 'rb')
file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
file_msg.set_payload(data.read( ))
data.close( )
email.Encoders.encode_base64(file_msg)
'''


"""
## 设置附件头
basename = os.path.basename(file_name)
file_msg.add_header('Content-Disposition',
 'attachment', filename = basename)
main_msg.attach(file_msg)
"""

# 设置根容器属性

from_name = time_now+u'股票篩選器'

main_msg['From'] = u"魏豪廷"
main_msg['To'] = "weihautin@gmail.com"
main_msg['Subject'] = "主旨股票"
#main_msg['Date'] = email.Utils.formatdate( )
 
# 得到格式化后的完整文本
fullText = main_msg.as_string( )

 
# 用smtp发送邮件
try:
    server.sendmail(From, To, fullText)
finally:
    server.quit()
    
    
