#!/usr/bin/python3
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from gi.repository import Notify
from time import sleep

while (1):

    my_url = "https://in.news.yahoo.com/world"
    uClient=uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    page_soup=soup(page_html,"html.parser")
    containers=page_soup.findAll("div",{"class":"Cf"})
    Notify.init("App Name")
 
    Notify.Notification.new("News : " + containers[0].h3.a.text).show()
    Notify.uninit()
    sleep(60)
#BeaytifulSoup #WebScrapping #Notify

