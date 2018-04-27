#coding:utf-8
from urllib import parse
from urllib import request
import webbrowser
values={"username":"18217485621","password":"LXwojj2014"}
# data=parse.urlencode(values).encode('utf-8')
url="http://kaoshi.edu.sina.com.cn/college/scorelist?/tab=batch&wl=1&local=2&batch=&syear=2013"
req=request.Request(url)
response=request.urlopen(req)
print(response.read().decode())
# file=open('https://mail.163.com/','w')
# file.write(content).
# webbrowser.open(url)
print('hehe')
# import urllib
# import urllib2
#
# values = {"username":"1016903103@qq.com","password":"XXXX"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url,data)
# response = urllib2.urlopen(request)
# print response.read()