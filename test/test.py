#coding:utf-8
import json
import math

def quadratic(a,b,c):
	s=abs(b**2-4*a*c)
	print (s)
	x1=(-b+math.sqrt(s))/2*a
	x2=(-b-math.sqrt(s))/2*a
	return x1,x2

# print quadratic(2,4,4)
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def powe(x,n):
	s=x**n
	return s
# print power(2,0)
def add_end(L=[]):
    L.append('END')
    return L

a=2.5
# if isinstance(a,(int,float)):
# 	print 'ss'
args=[1,2,3,4]
kw={'x':99}


def f1(a, b):
    print ('{a},{b}'.format(a=25,b=36))
def func(a, b, c=0, *args, **kw):
	print ('a =',a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
	if num == 1:
		return 1
	print (num,product)
	return fact_iter(num - 1, num * product)
print (fact(5))