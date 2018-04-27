#coding:utf-8
import re
from bs4 import BeautifulSoup

import  requests

import sys
type = sys.getfilesystemencoding()

kwywords=input("please input keywords:\n")

content= requests.get("http://dict.baidu.com/s",params={'wd':kwywords}).content
soup = BeautifulSoup(content,"lxml")


content1=str(soup.findAll(class_="tab-content")[0].find("p")).split("<")[1].replace("p>","").strip()

k=0

strk=content1

print(strk)
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