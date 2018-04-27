#coding : utf-8

import re
import urllib
url="https://www.qiushibaike.com/hot/"
user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3408.400 QQBrowser/9.6.12028.400"
headers={'user-Agent':user_agent}
request=urllib.request(url,headers=headers)
response=urllib.request(request)
content=response.read().decode('utf-8')
parrtern=re.compile('content">(.*?)<!--(.*?)-->.*?</div>',re.S)
items = re.findall(parrtern,content)
for item in items:
    print(item[0])