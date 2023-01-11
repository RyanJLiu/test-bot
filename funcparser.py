from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError
import time
import datetime
import pymysql

def chq(instr):
    if (instr=="輕微頭痛" or instr=="胸悶" or instr=="喉嚨痛" or instr=="肚子痛" or instr=="心情不好"):
        return 1
    else:
        return 0
def que(instr):
    if (instr=="輕微頭痛"):
        return "多休息一下吧"
    elif (instr=="胸悶"):
        return "深呼吸一下"
    elif (instr=="喉嚨痛"):
        return "多喝點水"
    elif (instr=="肚子痛"):
        return "按摩一下肚子附近"
    elif (instr=="心情不好"):
        return "找點開心的事做吧"
    else :
        return "我不太確定該說什麼"

def getstat(userid):
    connect_db = pymysql.connect(host='us-cdbr-east-05.cleardb.net', user='bb92b47b5b40af', passwd='ad501df8', charset='utf8', db='heroku_c420746d6bd4d14')

    with connect_db.cursor() as cursor:

        stat="""
        SELECT * from stat where 帳號 = %s
        """

        cursor.execute(stat,[userid])
        st=cursor.fetchone()
        
    connect_db.close()
    return st[1]
def s0(userid):
    connect_db = pymysql.connect(host='us-cdbr-east-05.cleardb.net', user='bb92b47b5b40af', passwd='ad501df8', charset='utf8', db='heroku_c420746d6bd4d14')

    with connect_db.cursor() as cursor:

        stat="""
        UPDATE `stat` SET `狀態` = '0' WHERE `帳號` = %s
        """

        cursor.execute(stat,[userid])
        connect_db.commit()
    connect_db.close()
def setMan(userid, tname):
    connect_db = pymysql.connect(host='us-cdbr-east-05.cleardb.net', user='bb92b47b5b40af', passwd='ad501df8', charset='utf8', db='heroku_c420746d6bd4d14')

    with connect_db.cursor() as cursor:

        searchman="""
        SELECT * from clients where 姓名 = %s
        """

        setman="""
        UPDATE `user` SET `護理師` = %s WHERE `帳號` = %s
        """

        cursor.execute(searchman,[tname])
        manid=cursor.fetchone()

        if (manid):
            cursor.execute(setman,[manid[2],userid])
            connect_db.commit()
            repman="已更改護理師為"+tname
        else:
            repman="此人並非用戶"
    connect_db.close()
    return repman
def callMan(userid, msg):
    CHANNEL_ACCESS_TOKEN = "UYBnsEo8qLdA4aQAdbX/NUxy9L86NT5epTsoy8d3h2xRItfJyecH49jRkUP26eHbHqN6FCUyboStjuk7TMg/a1u+c+z9mS/CvKJ2/g3my9olG4CQy2yLfHO3ceORUy5CxufKXbUl1xyG7nGHSsM7IwdB04t89/1O/w1cDnyilFU="

    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
    connect_db = pymysql.connect(host='us-cdbr-east-05.cleardb.net', user='bb92b47b5b40af', passwd='ad501df8', charset='utf8', db='heroku_c420746d6bd4d14')

    with connect_db.cursor() as cursor:

        man="""
        SELECT * from user WHERE `帳號` = %s
        """

        user="""
        SELECT * from clients WHERE `帳號` = %s
        """
        
        cursor.execute(man,[userid])
        data=cursor.fetchone()
        cursor.execute(user,[userid])
        userdata=cursor.fetchone()

        if (data[1]):
            cursor.execute(user,[data[1]])
            mandata=cursor.fetchone()
            try:
                line_bot_api.push_message(data[1], TextSendMessage(text="from "+userdata[0]+":\n"+msg))
            except LineBotApiError as e:
                raise e
            repcall="已為您通知"+mandata[0]
        else:
            repcall="您並未設定護理師"
            
    connect_db.close()
    return repcall
def getset(userid):
    connect_db = pymysql.connect(host='us-cdbr-east-05.cleardb.net', user='bb92b47b5b40af', passwd='ad501df8', charset='utf8', db='heroku_c420746d6bd4d14')

    with connect_db.cursor() as cursor:

        user="""
        SELECT * from clients WHERE `帳號` = %s
        """

        timeset="""
        SELECT * from user WHERE `帳號` = %s
        """

        cursor.execute(user,[userid])
        userdata=cursor.fetchone()
        cursor.execute(timeset,[userid])
        timedata=cursor.fetchone()
        if (timedata[1]):
            cursor.execute(user,[timedata[1]])
            mandata=cursor.fetchone()
            repset="姓名: "+userdata[0]+"\n生日: "+str(userdata[1])+"\n性別: "+userdata[3]+"\n護理師: "+mandata[0]+"\n早餐時間"+str(timedata[2])+"\n午餐時間"+str(timedata[3])+"\n晚餐時間"+str(timedata[4])+"\n睡眠時間"+str(timedata[5])
        else:
            repset="姓名: "+userdata[0]+"\n生日: "+str(userdata[1])+"\n性別: "+userdata[3]+"\n早餐時間"+str(timedata[2])+"\n午餐時間"+str(timedata[3])+"\n晚餐時間"+str(timedata[4])+"\n睡眠時間"+str(timedata[5])
        
    connect_db.close()
    return repset
def getsch(userid):
    connect_db = pymysql.connect(host='us-cdbr-east-05.cleardb.net', user='bb92b47b5b40af', passwd='ad501df8', charset='utf8', db='heroku_c420746d6bd4d14')

    with connect_db.cursor() as cursor:

        repsch=''

        schedule="""
        SELECT * from schedule WHERE `帳號` = %s
        """

        cursor.execute(schedule,[userid])
        data=cursor.fetchall()
        for row in data:
            if time.strptime(str(row[1]), "%Y-%m-%d")>time.strptime((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d"),"%Y-%m-%d"):
                if row[2]:
                    repsch=repsch+row[3]+"  日期: "+str(row[1])+"  時間: "+str(row[2])+"\n"
                else:
                    repsch=repsch+row[3]+"  日期: "+str(row[1])+"\n"
        
    connect_db.close()
    return repsch
def getmed(userid):
    connect_db = pymysql.connect(host='us-cdbr-east-05.cleardb.net', user='bb92b47b5b40af', passwd='ad501df8', charset='utf8', db='heroku_c420746d6bd4d14')

    with connect_db.cursor() as cursor:

        repmed=''

        med="""
        SELECT * from offer WHERE `帳號` = %s
        """

        cursor.execute(med,[userid])
        data=cursor.fetchall()
        for row in data:
            if (time.strptime(str(row[3]), "%Y-%m-%d")>time.strptime((datetime.datetime.now()+datetime.timedelta(days=-row[1])).strftime("%Y-%m-%d"),"%Y-%m-%d")) and (time.strptime(str(row[3]), "%Y-%m-%d")<time.strptime((datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d"),"%Y-%m-%d")):
                repmed=repmed+"藥品名稱: "+str(row[0])+"  服用時間: "
                if row[4]:
                    repmed=repmed+"早餐 "
                if row[5]:
                    repmed=repmed+"午餐 "
                if row[6]:
                    repmed=repmed+"晚餐 "
                if row[7]:
                    repmed=repmed+"睡眠 "
                repmed=repmed+"\n"
       
    connect_db.close()
    return repmed
