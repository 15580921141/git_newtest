#coding:utf-8

import  requests
import  time
import  chardet

s = requests.Session()
url1="http://test.admin.tianqi.eastday.com/index.php?m=index&c=login&a=login&r0.17155701600469597"

data1={"submit":"1",
		"user_name":"admin",
       "password":"123123"
}
s.post(url=url1,data=data1)

time.sleep(5)
print(s.get(url="http://test.admin.tianqi.eastday.com/index.php?m=index&c=index&a=index").content.decode("UTF-8-SIG"))
# print chardet.detect(s.get(url="http://test.admin.tianqi.eastday.com/index.php?m=index&c=index&a=index").content)

#
# data2={
# 	"submit":"1",
# 	"new_id":"",
# 	"name":"元旦",
# 	"time":"20180101",
# 	"image":"http://imgtianqi.eastday.com/res/upload/img/2016-12-30/5866349f9ccab.png",
# 	"url":"http://mtianqi.eastday.com/kuaibao/news/37395.html",
# 	"word":"元旦（12月30-1月1日）小长假即将到来，每逢佳节倍儿想嗨！",
#
# }
#
# urladd="http://test.admin.tianqi.eastday.com/index.php?m=index&c=festival&a=add&r0.4836729111108573"
# print(s.post(url=urladd,data=data2).content)