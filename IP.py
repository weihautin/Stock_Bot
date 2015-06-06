# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:22:32 2015

@author: tim
"""

import os
import socket
from datetime import datetime


if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip
    


if __name__ == "__main__":
    
    print get_lan_ip()
    
    content = "贏要衝,輸要縮."   #沒有辦法換行

    time_now = datetime.now().strftime("%Y%m%d_%H%M%S") #今天的日期 ex:2015-0411

    title = str(time_now+"-IP") #Email郵件的標題 ex:2015-0411-選股機器人


    attachment = str(time_now)+'-'+'IP.txt' #附件名稱使用當日時間 ex:2015-0411.txt

    fileopen = open(attachment, 'w') #開啟檔案,w沒有該檔案就新增

    f = open('/home/tim/GMAIL.txt','r') #於前一個相對目錄中放置登入GMAIL帳號密碼,目的為了不再GitHub顯示出來.
    ID = f.readline().strip('\n') #不包含換行符號\n
    PW = f.readline().strip('\n')
   
    ip = get_lan_ip()
   
    fileopen.write(str(ip))        
    fileopen.close()
   
    os.system('sendEmail -o \
    -f u160895@taipower.com.tw \
    -t "WEI <weihautin@gmail.com>" u160895@taipower.com.tw \
    -s smtp.gmail.com:587 \
    -xu %s \
    -xp %s \
    -u %s \
    -m %s \
    -a %s \
    '%(ID, PW, title, ip, attachment))
    
    
    