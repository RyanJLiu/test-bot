import funcparser
import pymysql

uid='Ud0b3296f8e4a70520b4ed2f2d1b3bdd8'
ret=funcparser.getsch(uid)
print(ret)
'''
connect_db = pymysql.connect(host='us-cdbr-east-05.cleardb.net', user='bb92b47b5b40af', passwd='ad501df8', charset='utf8', db='heroku_c420746d6bd4d14')

with connect_db.cursor() as cursor:

    sql="""
    INSERT INTO schedule (帳號, 日期, 時間, 行程, 備註) VALUES ('Ud0b3296f8e4a70520b4ed2f2d1b3bdd8', '2024-01-20', '', 'Tester', '')
    """
    
    cursor.execute(sql)
    connect_db.commit()
connect_db.close()

'''
