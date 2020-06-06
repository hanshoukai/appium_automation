# /usr/bin/env python
# coding=utf-8
from appium import webdriver
from appiumframework.PO import base_page
from selenium.webdriver.common.by import By
import time

#-------------------第一种写法-------------------
class CreatPage(base_page.Action):
    add_button_loc = ("com.smartisan.notes:id/add_button")
    edittext_loc = ("com.smartisan.notes:id/list_rtf_view")
    finish_button_loc = ("com.smartisan.notes:id/send_finish_button")

    def add_button_link(self):
        self.find_element(self.add_button_loc).click()
        time.sleep(3)           #等待3秒，等待登录弹窗加载完成

    def run_case(self,value):
        self.find_element(self.edittext_loc).send_keys(value)
        time.sleep(5)
        self.find_element(self.finish_button_loc).click()
        time.sleep(2)

    def get_finish_button_text(self):
        return self.find_element(self.edittext_loc).text

#-------------------第二种写法-------------------
class CreatPage(base_page.Action):
    _add_button_loc = (By.ID,"com.smartisan.notes:id/add_button")
    _edittext_loc = (By.ID,"com.smartisan.notes:id/list_rtf_view")
    _finish_button_loc = (By.ID,"com.smartisan.notes:id/send_finish_button")

    def add_button_link(self):
        self.find_element(self._add_button_loc).click()
        time.sleep(3)           #等待3秒，等待登录弹窗加载完成

    def run_case(self,value):
        self.find_element(self._edittext_loc).send_keys(value)
        time.sleep(5)
        self.find_element(self._finish_button_loc).click()
        time.sleep(2)

    def get_finish_button_text(self):
        return self.find_element(self._edittext_loc).text
