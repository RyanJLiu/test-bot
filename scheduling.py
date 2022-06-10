from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError
import pymysql
import os
import time

CHANNEL_ACCESS_TOKEN = "UYBnsEo8qLdA4aQAdbX/NUxy9L86NT5epTsoy8d3h2xRItfJyecH49jRkUP26eHbHqN6FCUyboStjuk7TMg/a1u+c+z9mS/CvKJ2/g3my9olG4CQy2yLfHO3ceORUy5CxufKXbUl1xyG7nGHSsM7IwdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

tn=time.localtime();
tnow=time.strftime("%H:%M:00", tn)

connect_db = pymysql.connect(host='us-cdbr-east-05.cleardb.net', user='bb92b47b5b40af', passwd='ad501df8', charset='utf8', db='heroku_c420746d6bd4d14')

with connect_db.cursor() as cursor:

    tim="""
    SELECT 帳號, 早餐, 午餐, 晚餐, 睡眠 from user WHERE 姓名 ='UserA'
    """
    
    med = """
    SELECT 藥品, 備註, 早餐, 午餐, 晚餐, 睡前 from offer WHERE 病歷號碼 ='10000001'
    """

    name="""
    SELECT 姓名 from clients WHERE 病歷號碼 ='10000001'
    """    

    cursor.execute(tim)
    stim=cursor.fetchall()
    
    cursor.execute(med)
    data = cursor.fetchall()

    cursor.execute(name)
    reply=cursor.fetchone()
    
connect_db.close()

to=stim[0][0]
if data[0][2]:
    tbre=stim[0][1]
else:
    tbre='false'
if data[0][3]:
    tlun=stim[0][2]
else:
    tlun='false'
if data[0][4]:
    tdin=stim[0][3]
else:
    tdin='false'
if data[0][5]:
    tnig=stim[0][4]
else:
    tnig='false'
if tnow==str(tbre):
    flag=1
elif tnow==str(tlun):
    flag=1
elif tnow==str(tdin):
    flag=1
elif tnow==str(tnig):
    flag=1
else:
    flag=0
if flag==1:
    try:
        line_bot_api.push_message(to, TextSendMessage(text='dear '+str(reply[0])+' 請記得用藥\n'+str(data[0][0])+'，'+str(data[0][1])))
    except LineBotApiError as e:
        raise e
