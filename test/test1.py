#coding:utf-8
from functools import reduce

#将‘123.456’输出123.456
def odd():
	n=1
	while True:
		n=n+2
		yield n

def ss(n):
	return lambda x:x%n>0
def prime():
	yield 2
	it=odd()
	while True:
		n=next(it)
		yield n
		it=filter(ss(n),it)
def main():
	for n in prime():
		if n <100:
			print(n)
		else:
			break
if __name__=='__main__':
	main()

