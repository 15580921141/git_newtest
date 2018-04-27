# class tes(object):
# 	def __init__(self):
# 		pass
import urllib.request
import urllib.response

req=urllib.request.Request('https://movie.douban.com/subject/26384741/?tag=热门&from=gaia')
res=urllib.request.urlopen(req)
print(res)