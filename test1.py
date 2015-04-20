# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:10:14 2015

@author: tim
"""

import csv
from cStringIO import StringIO

f = open('twse.csv')

try:
    reader = csv.reader(f)
    for row in reader:
        print row
finally:
    f.close()

