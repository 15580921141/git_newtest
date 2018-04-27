from bs4 import BeautifulSoup
import requests
import json

# u = '中文' #指定字符串类型对象u
# str = u.encode('gb2312').decode('gb2312') #以gb2312编码对u进行编码，获得bytes类型对象str
# u1 = str
# print(str)

request=requests.get('https://movie.douban.com/j/search_tags?type=movie&source=index')
result=json.loads(request.text)
tags=result['tags']
# for tag,v in result.items():
# 	# print(tag)
# 	print(result[tag])
# movie={}
movie=[]
for tag in tags:
	limit=0
	while 1:
		url='https://movie.douban.com/j/search_subjects?type=movie&tag='+tag+'&page_limit=20&page_start='+str(limit)
		request=requests.get(url)
		# print(request.text)
		result=json.loads(request.text)
		# 爬取到信息列表
		value=result['subjects']
		# print(value)
		# print(type(value))
		for v in value:
			movie.append(v)
		# 可通过信息列表获取不同属性
		# print(movie[0]['url'])
		# print(len(movie))
		limit += 20
		if value == []:
			break
		break
	break
for x in range(0,len(movie)):
	itm=movie[x]
	request1=requests.get(itm['url'])
	html=BeautifulSoup(request1.text,'lxml')
	title=html.select('h1')[0]
	title = title.select('span')[0]
	title = title.get_text()
	t = title.split()
	t = t[0]
	content = html.select('#info')[0]
	content = content.get_text()

	print(content)
	# print(t+'\n'+itm['url']+content)
	break