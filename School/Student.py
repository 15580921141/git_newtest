# -*- coding:utf-8 -*-
# import time
#
# o = open('C:\Users\Administrator\PycharmProjects\untitled\School\joke.txt', 'r')
#
# s = o.read().decode('gbk')
#
# o.close()
#
#
# def setname(wname):
# 	if type(wname) != str:
# 		wname = 'untitled_' + time.strftime('%H%M%S') + '.txt'
# 		o = open(wname, 'w')
# 		o.write(s.encode('gbk'))
# 		print wname
# 	else:
# 		print 'ww'
#
# wname = input()
# setname(wname)
# o.close()


def long(tp_str):
	count = 0
	for i in tp_str:
		count = count + 1
		print i,
	print count

def indexses(index):
	count = 0
	for i in index:
		if index[count] is None:

			break
		count = count + 1
	print count-1,


# tp_str = raw_input()
# long(tp_str)
index=raw_input()
indexses(index)
