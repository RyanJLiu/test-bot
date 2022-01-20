from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError
import pymysql
import os

CHANNEL_ACCESS_TOKEN = "UYBnsEo8qLdA4aQAdbX/NUxy9L86NT5epTsoy8d3h2xRItfJyecH49jRkUP26eHbHqN6FCUyboStjuk7TMg/a1u+c+z9mS/CvKJ2/g3my9olG4CQy2yLfHO3ceORUy5CxufKXbUl1xyG7nGHSsM7IwdB04t89/1O/w1cDnyilFU="
to = "Ud0b3296f8e4a70520b4ed2f2d1b3bdd8"

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

connection = pymysql.connect(host='us-cdbr-east-05.cleardb.net', user='bb92b47b5b40af', passwd='ad501df8', charset='utf8', db='heroku_c420746d6bd4d14')


with connection.cursor() as cursor:

    getname="""
    SELECT 姓名 from medicine WHERE 編號='0013456'
    """
    
    sql = """
    SELECT 藥名, 備註 from medicine WHERE 編號='0013456'
    """
    
    cursor.execute(getname)
    name=cursor.fetchone()
    
    cursor.execute(sql)
    data = cursor.fetchall()

connection.close()

try:
    line_bot_api.push_message(to, TextSendMessage(text='dear '+str(name[0])+' 請記得用藥\n'+str(data[0])+'\n'+str(data[1])))
except LineBotApiError as e:
    raise e
