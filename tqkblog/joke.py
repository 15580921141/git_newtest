#coding:utf-8
import re
from bs4 import BeautifulSoup

import  requests

import sys
sys.getfilesystemencoding()
booler = True
while booler:
	try:
		kwywords=input("please input keywords:\n")
		content= requests.get("http://dict.baidu.com/s",params={'wd':kwywords}).content
		soup = BeautifulSoup(content,"lxml")
		content1=str(soup.findAll(class_="tab-content")[-1].find('p')).split("<")[1].replace("p>","").strip()
		print(content1)
	except Exception:
		print("未查询到相关数据")
	# k=0
	# strk=content1
	# print(strk)
	while True:
		question = input("'yes'or'no':")
		if question == "yes":
			break
		elif question == "no":
			booler = False
			break
		else:
			print("输入错误，请重新输入!")
			continue
# s=[]
# for item in strk :
# 	k=k+1
# 	print(item),
# 	s.append(item)
#
# 	if k==50 :
# 		print('')
# 		k=0




# print content1