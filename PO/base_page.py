# /usr/bin/env python
# coding=utf-8
from appium import webdriver
class Action(object):
    #初始化
    def __init__(self,se_driver):
        self.driver = se_driver

    #重写元素定位的方法
    def find_element(self,loc):
        try:
            # WebDriverWait(self.driver,20).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.driver.find_element_by_id(loc)
        except Exception as e:
            print("未找到%s"%(self,loc))

