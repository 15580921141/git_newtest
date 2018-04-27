#coding:utf-8

class schoolmember:
	'''My name is hu'''
	contunt=0
	def __init__(self,name,age,address):
		self.name=name
		self.age=age
		self.address=address
		schoolmember.contunt+=1
		print '%s  %d岁  住在%s.'%(self.name,self.age,self.address),

	def mem(self):
		schoolmember.contunt-=1
		if schoolmember.contunt>=0:
			print '学生有{}'.format(schoolmember.contunt)
		else:
			print 'Dot{}'.format(self.age)

class teacher(schoolmember):
	'''Teacher'''
	contunt = schoolmember.contunt
	def __init__(self,name,age,address,salary,course,vacation):
		schoolmember.__init__(self,name,age,address)
		self.salary=salary
		self.course=course
		self.vacation=vacation
		teacher.contunt+=2
		schoolmember.contunt=teacher.contunt
		print '薪水:{self.salary}\t课程:{self.course}\t假期:{self.vacation}个月'.format(self=self)

class student(schoolmember):
	def __init__(self,name,age,address,score,tuition):
		schoolmember.__init__(self,name,age,address)
		self.score=score
		self.tuition=tuition
		print '考了%s\t花费了%d'%(self.score,self.tuition)


s=student('王二',18,'上海',98,6300)
t=teacher('李四',25,'长沙',5000,'English',2)
