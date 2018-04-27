#coding=utf-8
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['udid'] = '9755f780'
desired_caps['deviceName'] = '9755f780'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# driver.find_element_by_name("1").click()
driver.find_element_by_id("com.android.calculator2:id/digit5").click()
driver.find_element_by_id("com.android.calculator2:id/mul").click()
driver.find_element_by_id("com.android.calculator2:id/digit9").click()
# driver.find_element_by_name("5").click()
driver.find_element_by_id("com.android.calculator2:id/plus").click()
driver.find_element_by_id("com.android.calculator2:id/digit6").click()
driver.find_element_by_id("com.android.calculator2:id/equal").click()
# driver.find_element_by_name("=").click()
driver.quit()
