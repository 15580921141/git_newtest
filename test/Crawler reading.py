#coding:utf-8

import requests
from urllib.request import urlopen
import json
url='http://kaoshi.edu.sina.com.cn/college/scorelist?/tab=batch&wl=1&local=2&batch=&syear=2013'
#-------方案一：
# re=urlopen(url)
# print(re.read().decode())
# ------方案二：
requ_a=requests.get(url)
# requ_a.encoding='utf-8'
# print(requ_a.text)
stry=json.dumps(requ_a.text)+"\n"
print(type(stry))
print(stry.encode('utf-8').decode(''))

# 方案三:
# f=urllib.request.Request(url)
# response=urllib.request.urlopen(f)
# data=response.read()
#
# print(data.decode('utf-8'))
# file=open('file_scholl.html','wb')
# file.write(data)
# file.close()


# import urllib.request
#
# file=urllib.request.urlopen('http://kaoshi.edu.sina.com.cn/?p=college&s=api2015&a=getAllCollege')
#
# data=file.read()    #读取全部
#
# dataline=file.readline()    #读取一行内容
#
# fhandle=open("./1.html","wb")    #将爬取的网页保存在本地
# fhandle.write(data)
# fhandle.close()
