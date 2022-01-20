from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError
import pymysql

CHANNEL_ACCESS_TOKEN = "UYBnsEo8qLdA4aQAdbX/NUxy9L86NT5epTsoy8d3h2xRItfJyecH49jRkUP26eHbHqN6FCUyboStjuk7TMg/a1u+c+z9mS/CvKJ2/g3my9olG4CQy2yLfHO3ceORUy5CxufKXbUl1xyG7nGHSsM7IwdB04t89/1O/w1cDnyilFU="
to = "Ud0b3296f8e4a70520b4ed2f2d1b3bdd8"

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

connect_db = pymysql.connect(connection = pymysql.connect(host=os.environ.get('CLEARDB_DATABASE_HOST'),
                             user=os.environ.get('CLEARDB_DATABASE_USER'),
                             password=os.environ.get('CLEARDB_DATABASE_PASSWORD'),
                             db=os.environ.get('CLEARDB_DATABASE_DB'),
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connect_db.cursor() as cursor:

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

connect_db.close()

try:
    line_bot_api.push_message(to, TextSendMessage(text='dear '+str(name[0])+' 請記得用藥\n'+str(data[0])+'\n'+str(data[1])))
except LineBotApiError as e:
    raise e
