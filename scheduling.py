from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError
import pymysql

CHANNEL_ACCESS_TOKEN = "UYBnsEo8qLdA4aQAdbX/NUxy9L86NT5epTsoy8d3h2xRItfJyecH49jRkUP26eHbHqN6FCUyboStjuk7TMg/a1u+c+z9mS/CvKJ2/g3my9olG4CQy2yLfHO3ceORUy5CxufKXbUl1xyG7nGHSsM7IwdB04t89/1O/w1cDnyilFU="
to = "Ud0b3296f8e4a70520b4ed2f2d1b3bdd8"

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

connect_db = pymysql.connect(host='localhost', port=3306, user='the_bot', passwd='TestBot001', charset='utf8', db='bot_test')

with connect_db.cursor() as cursor:

    name="""
    SELECT 姓名 from medicine WHERE 編號='0013456'
    """
    
    sql = """
    SELECT 藥名, 備註 from medicine WHERE 編號='0013456'
    """
    
    cursor.execute(name)
    reply=cursor.fetchone()
    
    # 執行 SQL 指令
    cursor.execute(sql)
    
    # 取出全部資料
    data = cursor.fetchall()

# 關閉 SQL 連線
connect_db.close()

try:
    line_bot_api.push_message(to, TextSendMessage(text='dear '+str(reply[0])+' 請記得用藥\n'+str(data[0])+'\n'+str(data[1])))
except LineBotApiError as e:
    raise e
