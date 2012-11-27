#! /usr/bin/env python
# -*- coding:utf-8 -*-

from BeautifulSoup import BeautifulSoup
import mechanize
import datetime
import locale
import time
import codecs
import urllib2

on_st="%E7%90%B4%E4%BC%BC%28%E5%8C%97%E6%B5%B7%E9%81%93%29"#琴似
off_st="%E6%89%8B%E7%A8%B2"#手稲
Date_Year="2012"
Date_Month="11"
Date_Day="27"
Time_Hour="12"
URL=u"http://transit.goo.ne.jp/nconfirm.php?an=7&on_st="+on_st+u"&Jousha_select=&off_st="+off_st+u"&Gesha_select=&by_st=&sr=0&Date_Year="+Date_Year+u"&Date_Month="+Date_Month+u"&Date_Day="+Date_Day+u"&Time_Hour="+Time_Hour
html=urllib2.urlopen(URL).read()
soup=BeautifulSoup(html)

print soup('strong')[0].renderContents()
print soup('strong')[1].renderContents()
