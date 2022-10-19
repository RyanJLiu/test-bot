from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError
import pymysql
import os
import time

def med_mind():
    CHANNEL_ACCESS_TOKEN = "UYBnsEo8qLdA4aQAdbX/NUxy9L86NT5epTsoy8d3h2xRItfJyecH49jRkUP26eHbHqN6FCUyboStjuk7TMg/a1u+c+z9mS/CvKJ2/g3my9olG4CQy2yLfHO3ceORUy5CxufKXbUl1xyG7nGHSsM7IwdB04t89/1O/w1cDnyilFU="

    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

    tn=time.localtime();
    tnow=time.strftime("%#H:%M:00", tn)

    connect_db = pymysql.connect(host='us-cdbr-east-05.cleardb.net', user='bb92b47b5b40af', passwd='ad501df8', charset='utf8', db='heroku_c420746d6bd4d14')

    with connect_db.cursor() as cursor:

        personal="""
        SELECT * from user
        """
        
        offer = """
        SELECT * from offer WHERE `User id` = %s
        """

        name="""
        SELECT 姓名 from clients WHERE `User id` = %s
        """

        med="""
        SELECT 品名 from medicine WHERE `編號` = %s
        """

        cursor.execute(personal)
        pers=cursor.fetchall()

        for users in pers:
            to=users[0]
        
            cursor.execute(offer,[users[1]])
            data = cursor.fetchall()

            cursor.execute(name,[users[1]])
            reply=cursor.fetchone()

            for row in data:
                cursor.execute(med, [row[1]])
                med_name = cursor.fetchone()
            
                to=users[0]
                if row[5]:
                    tbre=users[3]
                else:
                    tbre='false'
                if row[6]:
                    tlun=users[4]
                else:
                    tlun='false'
                if row[7]:
                    tdin=users[5]
                else:
                    tdin='false'
                if row[8]:
                    tnig=users[6]
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
                        line_bot_api.push_message(to, TextSendMessage(text='dear '+str(reply[0])+' 請記得用藥\n'+str(med_name[0])+'，'+str(row[9])))
                    except LineBotApiError as e:
                        raise e
                
    connect_db.close()
