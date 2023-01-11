from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError
import pymysql
import os
import time
import datetime

def mind():
    CHANNEL_ACCESS_TOKEN = "UYBnsEo8qLdA4aQAdbX/NUxy9L86NT5epTsoy8d3h2xRItfJyecH49jRkUP26eHbHqN6FCUyboStjuk7TMg/a1u+c+z9mS/CvKJ2/g3my9olG4CQy2yLfHO3ceORUy5CxufKXbUl1xyG7nGHSsM7IwdB04t89/1O/w1cDnyilFU="

    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

    tn=time.localtime();
    tdate=time.strftime("%Y:%m:%d", tn)
    tnow=time.strftime("%#H:%M:00", tn)

    connect_db = pymysql.connect(host='us-cdbr-east-05.cleardb.net', user='bb92b47b5b40af', passwd='ad501df8', charset='utf8', db='heroku_c420746d6bd4d14')

    with connect_db.cursor() as cursor:

        personal="""
        SELECT * from user
        """
        
        offer = """
        SELECT * from offer WHERE `帳號` = %s
        """
        schedule="""
        SELECT * from schedule WHERE `帳號` = %s
        """

        cursor.execute(personal)
        pers=cursor.fetchall()

        for users in pers:
            to=users[0]
        
            cursor.execute(offer,[users[0]])
            data = cursor.fetchall()

            for row in data:
                if row[4]:
                    tbre=users[2]
                else:
                    tbre='false'
                if row[5]:
                    tlun=users[3]
                else:
                    tlun='false'
                if row[6]:
                    tdin=users[4]
                else:
                    tdin='false'
                if row[7]:
                    tnig=users[5]
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
                if time.strptime(str(row[3]), "%Y-%m-%d")<time.strptime((datetime.datetime.now()+datetime.timedelta(days=-row[1])).strftime("%Y-%m-%d"),"%Y-%m-%d"):
                    flag=0
                if time.strptime(str(row[3]), "%Y-%m-%d")>time.strptime(datetime.datetime.now().strftime("%Y-%m-%d"),"%Y-%m-%d"):
                    flag=0
                if flag==1:
                    try:
                        line_bot_api.push_message(to, TextSendMessage(text='請記得用藥\n'+str(row[0])+'，'+str(row[8])))
                    except LineBotApiError as e:
                        raise e

        for users in pers:
            to=users[0]
        
            cursor.execute(schedule,[users[0]])
            data = cursor.fetchall()

            for row in data:
                if (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")==str(row[1]):
                    if tnow=="18:00:00":
                        flag=1
                if flag==1:
                    try:
                        if(row[2]):
                            line_bot_api.push_message(to, TextSendMessage(text='提醒您，明日'+str(row[2])+'\n'+str(row[3])+'，'+str(row[4])))
                        else:
                            line_bot_api.push_message(to, TextSendMessage(text='提醒您，明日'+str(row[3])+'，'+str(row[4])))
                    except LineBotApiError as e:
                        raise e
        
    connect_db.close()
