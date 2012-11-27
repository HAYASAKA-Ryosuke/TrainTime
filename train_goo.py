#! /usr/bin/env python
# -*- coding:utf-8 -*-

from BeautifulSoup import BeautifulSoup
import mechanize
import datetime
import locale
import time
import codecs
import urllib2
import datetime

#朝・昼なら琴似->手稲，夜なら手稲->琴似
def Station_judge(morningtime=datetime.time(15,0,0),deepnighttime=datetime.time(4,0,0)):
          now=datetime.datetime.now()                                            
          #0時から15時間での間は琴似を表示                                       
          if((morningtime.hour>now.hour)and(deepnighttime.hour<now.hour)):       
            return ["%E7%90%B4%E4%BC%BC%28%E5%8C%97%E6%B5%B7%E9%81%93%29","%E6%89%8B%E7%A8%B2"]                              
          else:                                                                  
            return ["%E6%89%8B%E7%A8%B2","%E7%90%B4%E4%BC%BC%28%E5%8C%97%E6%B5%B7%E9%81%93%29"]

#現在時刻および乗り降りの駅名からURLを生成する
def GenerateURL(Date_Year,Date_Month,Date_Day,Time_Hour,Time_Minute,on_st,off_st): 
   return u"http://transit.goo.ne.jp/nconfirm.php?an=7&on_st="+on_st+u"&Jousha_select=&off_st="+off_st+u"&Gesha_select=&by_st=&sr=0&Date_Year="+Date_Year+u"&Date_Month="+Date_Month+u"&Date_Day="+Date_Day+u"&Time_Hour="+Time_Hour+"&Time_Minute="+Time_Minute

def Next_train():
    now=datetime.datetime.now()
    date_year=str(now.year)
    date_month=str(now.month)
    date_day=str(now.day)
    time_hour=str(now.hour)
    time_minute=str(now.minute)
    station=Station_judge()
    URL=GenerateURL(date_year,date_month,date_day,time_hour,time_minute,station[0],station[1])
    html=urllib2.urlopen(URL).read()
    soup=BeautifulSoup(html)
    if(station[0]=="%E6%89%8B%E7%A8%B2"):
        return ["手->琴",soup('strong')[0].renderContents(),soup('strong')[1].renderContents()]
    else:
        return ["琴->手",soup('strong')[0].renderContents(),soup('strong')[1].renderContents()]
result= Next_train()
print result[0]+" "+result[1]+" "+result[2]
