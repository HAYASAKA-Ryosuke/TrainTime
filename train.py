#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import mechanize
import urllib2
import sys
import datetime
import locale
import time

def Terminal_judge(morningtime=datetime.time(15,0,0),deepnighttime=datetime.time(4,0,0)):
         now=datetime.datetime.now()
         #0時から15時間での間は琴似を表示
         if((morningtime.hour>now.hour)and(deepnighttime.hour<now.hour)):
           return {"start":"kotoni","end":"teine"}
         else:
           return {"start":"teine","end":"kotoni"}

br=mechanize.Browser()
URL="http://www3.jrhokkaido.co.jp/time/01ekiinput.asp"
URL2="http://www3.jrhokkaido.co.jp/time/03disp.asp"
br.open(URL)
enc=br.encoding()

br.select_form(nr=0)
#print br.form
br["S_EKI_IN"]="kotoni"
#br.select_form(name="E_EKI_IN")
br["E_EKI_IN"]="teine"
resp=br.submit()
#br.select_form(name="keiro")
#br.select_form(nr=0)
#resp=br.form.click(name='keiro',nr=0)
br.form_click(name='keiro')
#resp=br.form.action='keiro_search();'
#resp=br.form.submit(name="keiro_search();",nr=0)
#resp=br.submit()
#br.open(req)
#resp=br.open(URL2)
br.select_form(nr=0)
print br.form
#print Terminal_judge(datetime.time(15,0,0),datetime.time(4,0,0))

#soup.findAll('td',)
