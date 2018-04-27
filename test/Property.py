__author__ = 'Administrator'


class Screen(object):
	@property
	def width(self):
		return self._width
	@property
	def height(self):
		return self._height
	@property
	def resolution(self):
		return self._height * self._width

	@width.setter
	def width(self,value):
		self._width = value
	@height.setter
	def height(self,value):
		self._height = value

s=Screen()
s.width=25
print(s.width)
s.height=54
print('resolution = ',s.resolution)
if s.resolution == 1350:
	print('测试通过')
else:
	print('测试失败')