# /usr/bin/env python
# coding=utf-8

#--------------------------第一种方式--------------------------
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
            
#--------------------------第二种方式--------------------------

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    #黑名单：升级，广告弹窗等
    _black_list = [
        (By.ID,"image_cancel"),
        (By.ID,"tips")
    ]
    def __init__(self,driver:WebDriver):
        self.driver = driver

    #查找元素的时候加上一些异常处理
    def find_element(self,locator):
        print(locator)
        try:
            return self.driver.find_element(*locator)
        except:
            self.handle_exception()
            return self.driver.find_element(*locator)

    #重写定位后点击方法，也加上了一些异常处理
    def find_element_and_click(self,locator):
        print("click")
        try:
            self.find_element(locator).click()
        except:
            self.handle_exception()
            self.find_element(locator).click()

    #定义异常处理的方法
    def handle_exception(self):
        self.driver.implicitly_wait(0)
        for locator in self._black_list:
            elements = self.driver.find_elements(*locator)
            if len(elements) >= 1:
                # elements.click()
                self.find_element_and_click(*locator)
            else:
                print("%s not found"%str(locator))
        self.driver.implicitly_wait(20)
