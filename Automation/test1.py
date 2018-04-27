# coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'OPPO A33'
desired_caps['appPackage'] = 'com.songheng.eastsports'
desired_caps['appActivity'] = '.business.splash.view.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_element_by_id('com.songheng.eastsports:id/newsTitle').click()
time.sleep(3)
# driver.find_element_by_id('com.songheng.eastsports:id/layout_back').click()
# time.sleep(3)
# driver.find_element_by_name('NBA').click()
# time.sleep(3)

# driver.find_element_by_class_name('android.widget.RelativeLayout').click()
# time.sleep(3)
# driver.find_element_by_id('com.songheng.eastsports:id/layout_share').click()
# time.sleep(3)

# driver.find_element_by_id('com.songheng.eastsports:id/layout_addTopic').click()


# 获得机器屏幕大小x,y
def getSize():
	x = driver.get_window_size()['width']
	y = driver.get_window_size()['height']
	return (x, y)

# 向上滑动
def swipUp(t):
	l = getSize()
	x1 = int(l[0] * 0.5)
	y1 = int(l[1] * 0.75)
	y2 = int(l[1] * 0.25)
	driver.swipe(x1, y1, x1, y2, t)


# 屏幕向下滑动
def swipeDown(t):
	l = getSize()
	x1 = int(l[0] * 0.5)  # x坐标
	y1 = int(l[1] * 0.25)  # 起始y坐标
	y2 = int(l[1] * 0.75)  # 终点y坐标
	driver.swipe(x1, y1, x1, y2, t)



# time.sleep(7)
swipUp(1000)
swipeDown(1000)
driver.quit()