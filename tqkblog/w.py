#coding:utf-8
import requests
import HTMLParser
import os.path
import re
def get_pic(path,num,proxies):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    url='http://www.budejie.com/pic/{}'
    for i in range(1,num):
        print u'正在爬取第%s页······'%i
        rq=requests.get(url.format(i),headers=headers,proxies=proxies)
     #   print rq.status_code
      #  et=etree.HTML(rq.text)
      #  xp=et.xpath('//a/img[@src]')
        pt = r'data-original="(\w.+?\.\w+)" title='
        url_list= re.findall(re.compile(pt),rq.text)
     #   print url_list
        for i in url_list:
            name=os.path.basename(i)
            with open(path+'\\'+name,'wb') as ps:
                ps.write(requests.get(i,headers=headers,proxies=proxies).content)
path='D:\\LX\\baisi'

proxies = {
    "http1": "http://115.29.2.139:80"
}
get_pic(path,100,proxies)
