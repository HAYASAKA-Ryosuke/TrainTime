#!/usr/bin/env python
#-*-coding:utf-8-*-

from selenium import webdriver
import datetime
import locale
import time
from BeautifulSoup import BeautifulSoup
import urllib2
import codecs
def Terminal_judge(morningtime=datetime.time(15,0,0),deepnighttime=datetime.time(4,0,0)):
          now=datetime.datetime.now()
          #0時から15時間での間は琴似を表示
          if((morningtime.hour>now.hour)and(deepnighttime.hour<now.hour)):
            return {"start":"kotoni","end":"teine"}
          else:
            return {"start":"teine","end":"kotoni"}

URL="http://www3.jrhokkaido.co.jp/time/01ekiinput.asp"
URL2="http://www3.jrhokkaido.co.jp/time/03disp.asp"
driver=webdriver.Firefox()
driver.get(URL)
driver.find_element_by_name('S_EKI_IN').send_keys("kotoni")
driver.find_element_by_name('E_EKI_IN').send_keys("teine")
driver.find_element_by_name('eki').click()
resp=driver.find_element_by_name('keiro').click()
opener=urllib2.build_opener()

#html=unicode(opener.open(URL2).read(),'shift-jis')
f=codecs.open('traininfo','w','MS932')
f.write(driver.page_source)
f.close()
driver.close()
soup=BeautifulSoup()
