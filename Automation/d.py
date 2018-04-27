# coding:utf-8
import pymysql
conn = pymysql.connect(user='root', passwd='root',host='localhost', db='wamp_test',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()
# cur.execute("INSERT INTO wptest(title,url,rate) VALUES ('%s','%s','%s')"%('振兴','http://movie.douban.com','成龙'))

cur.execute('select * from wptest')
for r in cur:
    print("row_number:"+str(cur.rownumber))
    print(r)

cur.close()
conn.close()
