import requests
from bs4 import BeautifulSoup
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError
import pymysql
import os

def findkey(key, soup):
    all_sections=soup.find_all('section')
    for section in all_sections:
        if section.get('class')==[key]:
            target_section=section
            break
    return target_section

def webcheck(web):
    output=open('temp.html','w',encoding='utf-8')
    html=requests.get(web)
    soup=BeautifulSoup(html.text,'html.parser')

    output.write(soup.prettify())
    output.close()
    target_section=None
    target_section=findkey('layout__grid-news', soup)
    news=target_section.find('ul')
    item=news.find('a')
    return item.get('href')

CHANNEL_ACCESS_TOKEN = "UYBnsEo8qLdA4aQAdbX/NUxy9L86NT5epTsoy8d3h2xRItfJyecH49jRkUP26eHbHqN6FCUyboStjuk7TMg/a1u+c+z9mS/CvKJ2/g3my9olG4CQy2yLfHO3ceORUy5CxufKXbUl1xyG7nGHSsM7IwdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

connect_db = pymysql.connect(host='us-cdbr-east-05.cleardb.net', user='bb92b47b5b40af', passwd='ad501df8', charset='utf8', db='heroku_c420746d6bd4d14')

with connect_db.cursor() as cursor:

    personal="""
    SELECT * from user
    """

    website="""
    SELECT * FROM website
    """

    webchange="""
    UPDATE website SET `最新新聞` = %s WHERE `網站` = %s
    """

    target="""
    SELECT 帳號 FROM web_trace WHERE `網站` = %s
    """

    changes=[]

    cursor.execute(personal)
    pers=cursor.fetchall()

    cursor.execute(website)
    webs=cursor.fetchall()
    
    for web in webs:
        new=webcheck(web[1])
        if new!=web[2]:
            cursor.execute(webchange,[new,web[0]])
            changes.append([web[0],web[1]])

    for chan in changes:
        cursor.execute(target,[chan[0]])
        sends=cursor.fetchall()
        for send in sends:
            try:
                line_bot_api.push_message(send[0], TextSendMessage(text='「'+str(chan[0])+'」網站已更新\n'+str(chan[1])))
            except LineBotApiError as e:
                raise e

    connect_db.commit()
    
connect_db.close()
