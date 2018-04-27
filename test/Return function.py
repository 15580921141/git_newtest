#!usr/bin/env python3
#coding:utf-8


import functools
import time

# def metric(fn):
#     def wrapper(*args,**kwargs):
#         s_time=time.time()
#         print('呵呵呵，嘻嘻嘻')
#         r=fn(*args,**kwargs)
#         print ('%s executed in %s ms'%(fn.__name__,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))))
#         print('end_list')
#         return r
#     return wrapper
#
# def log(text=None):
#     def func(fn):
#         @functools.wraps(fn)
#         def wrapper(*args,**kwargs):
#
#             print('begin call')
#             if text==None:
#                 print("%s():"% fn.__name__)
#             else:
#                 print("%s %s():"% (text,fn.__name__))
#             r=fn(*args,**kwargs)
#             print('end call')
#             return r
#         return wrapper
#     return func
# @log()
# def now():
#     print('2017-12-13')
# @log('今天是公祭日')
# def _now():
#     print('2017-12-13')
# now()
# _now()

max2=functools.partial(max,1)
print(max2(2,3,5))
