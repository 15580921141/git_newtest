#!usr/bin/env python3
#coding:utf-8
__author__ = 'Administrator'
from types import MethodType

class Student(object):
    # __slots__=('name','setage','age')
    def run(self):
        print("My is a student")
def set_age(self,age):
    self.age=age
def set_score(self, score):
    self.score = score

s=Student()
s.set_score=MethodType(set_score,s)
s.setage=MethodType(set_age,s)
s.set_score(100)
s2=Student()

s.name='hha'


s.setage(25) # 调用实例方法

print(s.name) # 测试结果

