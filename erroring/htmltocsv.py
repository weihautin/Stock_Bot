# -*- coding: utf-8 -*-
"""
Created on Tue May 26 21:35:03 2015

@author: tim
"""

import contextlib
import datetime
import glob
import os
import re
import urllib

d1 = datetime.datetime(2000, 12, 7)
d2 = datetime.datetime(2000, 12, 12)
csvlinkbase = 'http://www.twse.com.tw/ch/trading/indices/MI_5MINS_HIST/MI_5MINS_HIST_print.php?language=ch&save=csv'

csvdata_re = re.compile(r'(<table border=1.*</table>)', re.DOTALL)

for d in (d1+datetime.timedelta(n) for n in range((d2-d1).days+1)):
    yyyymmdd = '{}{:02}{:02}'.format(d.year, d.month, d.day)
    filename = 'A441{}.csv'.format(yyyymmdd)
    link = 'http://www.twse.com.tw/ch/trading/fund/TWT44U/TWT44U_oldtsec.php?' \
    'Submit22222=%C2%ACd%C2%B8%C3%9F&qdate={}%2F{:02}%2F{:02}&'\
    'sorting=by_issue'.format(d.year-1911, d.month, d.day)
    with contextlib.closing(urllib.urlopen(link)) as page:
        content = page.read()
    csvsrc_match = csvdata_re.search(content)
    if csvsrc_match:
        csvsrc = csvsrc_match.groups()[0]
        csvsrc = re.sub(r'</td><tr>', '</td></tr><tr>', csvsrc)
        csvsrc = re.sub(r'</th>', '</td>', csvsrc)
        csvsrc = re.sub(r'<th>', '<td>', csvsrc)
        postdata = urllib.urlencode({'html': csvsrc})
        urllib.urlretrieve(csvlinkbase, filename, data=postdata)
        
result = [os.remove(fn) for fn in glob.iglob('*.csv') if os.path.getsize(fn) < 1992]
        