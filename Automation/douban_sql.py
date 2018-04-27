# coding:utf-8
import pymysql

db=pymysql.connect(host='localhost', user='root', passwd='root', db='wamp_test', charset='utf8')

db.autocommit(True)
cursor=db.cursor()
#  删除数据表内容
cursor.execute('delete from wptest')

f=open('D:/LX/new_test/douban_movie_clean.txt','r',encoding='utf-8')
count = 0
for fs in f:
	count += 1
	if count == 1:
		continue
	fs=fs.strip().split('^')
	print(count)
	cursor.execute("insert into wptest(title, url, rate) VALUES ('%s', '%s', '%s')"%(fs[1], fs[2], fs[4]))
	# cursor.execute('select * from wptest')

f.close()
cursor.close()
db.close()