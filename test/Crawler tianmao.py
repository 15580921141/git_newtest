#coding:utf-8

import urllib.request
# from pip import utils
from pip import utils

import requests
import http.cookiejar
import urllib.parse
#淘宝登录页面的url
import sys
import time

loginurl='https://login.taobao.com/member/login.jhtml'
#header信息
loginHeader={'Accept':'*/*','Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Content-Length':1218,
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie':'uid=29e5f8ed118aff5e; umdata_=70CF403AFFD707DFDCABE8D2B1D809F70AF48EDC01668AE63581855D0A27E29359D507882C4A35E9CD43AD3E795C914C354E14DEB038CEC4B9BC1528608790F6',
'Host':'ynuf.alipay.com',
'Origin':'https://login.taobao.com',
'Referer':'https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fbuyertrade.taobao.com%2Ftrade%2Fitemlist%2Flist_bought_items.htm',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}

# post='ENCODE~~V01~~eyJ4diI6IjMuMy43IiwieHQiOiJDMTUyMjA0NDU0MjE1ODgzOTkyOTAzOTk5MTUyMjEyMTM2MTc4NzA1OCIsImV0ZiI6InUiLCJ4YSI6InRhb2Jhb19sb2dpbiIsInNpdGVJZCI6IiIsInVpZCI6IlxcdTUzNTZcXHU3Q0JFXFx1NTRDMVxcdTc2ODQiLCJlbWwiOiJBQSIsImV0aWQiOiIiLCJlc2lkIjoiIiwidHlwZSI6InBjIiwibmNlIjp0cnVlLCJwbGF0IjoiV2luMzIiLCJuYWNuIjoiTW96aWxsYSIsIm5hbiI6Ik5ldHNjYXBlIiwibmxnIjoiemgtQ04iLCJzdyI6MTkyMCwic2giOjEwODAsInNhdyI6MTkyMCwic2FoIjoxMDQwLCJic3ciOjE0MTgsImJzaCI6OTIwLCJlbG9jIjoiaHR0cHMlM0ElMkYlMkZsb2dpbi50YW9iYW8uY29tJTJGbWVtYmVyJTJGbG9naW4uamh0bWwiLCJldHoiOjQ4MCwiZXR0IjoxNTIyMTIxMzYxODIyLCJlY24iOiI5ZjAxYTM5ZDg2OTkxYTY2NzgyMWMyOTQ0MzYzN2U5MzE2NWE3YjM5IiwiZWNhIjoiYzZiNEVrNERCak1DQVhUaW05VmpSNkhsIiwiZXN0IjoyLCJ4cyI6IjQ4NkI3QjEyQzZBQTk1RjJCRkZEOEE3MTA0OUEwN0I5RkEwMzZENzU0RTcxNzU1NkU0RjgwQzhDMzMzODhDOURCQzc3NjZBRkE2MTFDRUNBQ0Q0M0FEM0U3OTVDOTE0QzVBNjcxRTlFNEU2NzhGOUI1MkFBQTNDRTlGM0EyMjlDIiwibXMiOiIzMDM3IiwiZXJkIjoiIiwiY2FjaGVpZCI6IjMxOTRhZWYxZGMyODQ5OGYiLCJ4aCI6IiIsImlwcyI6IjE5Mi4xNjguMTg0LjEsMTkyLjE2OC44MC4xLDE3Mi4yMC42LjIyMSwxOTIuMTY4LjIzLjEsMTkyLjE2OC4xMzcuMSIsImVwbCI6MjAsImVwIjoiN2Y3ZDU0MTJiMDcyOWM2ZDE0ODM2YWNjMGY1ZGQ2NjQzODQ5MTkzZiIsImVwbHMiOiJOOWE2NDk1M2RhOGQ0NGJkOWI1MmE1MmM4ZTAyYTliMGRmYzMyMGMyNSxDMmJkNWQxYmY4YzBmOTc5MmFjMjE5YmIyMDE1Nzk4MTg1MDNmNmM0ZCxTMjI2YmIzZjFjYWM2NTdhZWM5NGIxNDdlNWU4ZTk3ZGFhZDhmMDgzYSxNN2I5ZDA1NTJiYzEwMGI1YWIxOTllMTYzZTQyZWM3OTRkODQxMmZjZSxBZjA4ZDlmZmQxNGFmNDkxYTAzZTBkNTliMzhlYmY5OTAwZGFlZDAwNCxJOTZhYzg0MjFhN2QxYTc4YjJlYjU2MTY3YmIyZDM3ZWExM2RkZTg3YyxGMDRkMDU3NzdhOTgxMDM0MDEwNTVlZTI3NTAzM2QzNjRiZTIxZmQzMixUN2JiYWNjMWM5NDY3MzhlZTI4YTM0NDU5ZTAxNjY1OTdjNWY5NDk0MCxRMjQ2NTlkZTY0NDU4NTg4MGRmY2M2MWU4NDE3OWE4NjhmNWViNzA2NixXOGYyMTEyNGZiZGE3YjdjOWZmZjc2ZWQ1YmY1ODdmMzcyZjViMDVlOCIsImVzbCI6ZmFsc2V9'
# postdata=urllib.parse.urlencode(post).encode(encoding='gbk')
# print(postdata)
# cj=http.cookiejar.CookieJar()
# cookie_su=urllib.request.HTTPCookieProcessor(cj)

def getQRCode(enableCmdQR):
  payload = {'_ksTS': str(time.time()), 'from': 'alimama'}
  qrCodeObj = utils.fetchAPI('https://qrlogin.taobao.com/qrcodelogin/generateQRCode4Login.do', payload,
                "json", None, True, True)

  print(qrCodeObj)
  utils.printQRCode('http:' + qrCodeObj['url'], enableCmdQR)
  lgToken = qrCodeObj['lgToken']
  return lgToken


def login(enableCmdQR=False):
  lgToken = getQRCode(enableCmdQR)
  code = 0
  successLoginURL = ""
  while code != 10006:
    payload = {'lgToken': lgToken,
          'defaulturl': 'http%3A%2F%2Flogin.taobao.com%2Fmember%2Ftaobaoke%2Flogin.htm%3Fis_login%3D1&_ksTS=' + str(
            time.time())}

    rObj = utils.fetchAPI('https://qrlogin.taobao.com/qrcodelogin/qrcodeLoginCheck.do', payload, "json", True,
               False)
    code = int(rObj['code'])
    if 10000 == code:
      # print("请扫描二维码登录")
      continue
    elif 10001 == code:
      print("已扫描二维码，请在确认登录")
    elif 10004 == code:
      print("已过期请重新扫描")
      login()
    elif 10006 == code:
      successLoginURL = rObj["url"]
      print("登录成功，正在跳转")
    else:
      print("未知错误，退出执行")
      sys.exit(0)

    time.sleep(5)

  print("登录成功跳转:" + successLoginURL)
  r = utils.fetchAPI(successLoginURL, None, "raw", True, False, True)
  utils.fetchAPI(r.headers['Location'], None, "raw", True, True, False)