# /usr/bin/env python
# coding=utf-8
from appium import webdriver
import unittest
from appiumframework.PO.creat_page import CreatPage
import time

class Test(unittest.TestCase):
    """自动化"""
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',#可有可无
            'platformVersion': '5.0',
            # apk包名
            'appPackage': 'com.smartisan.notes',
            # apk的launcherActivity
            'appActivity': 'com.smartisan.notes.NewNotesActivity',
            #如果存在activity之间的切换可以用这个
            # 'appWaitActivity':'.MainActivity',
            'unicodeKeyboard': True,
            #隐藏手机中的软键盘
            'resetKeyboard': True
            }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        time.sleep(5)
        self.verificationErrors = "今天天气不错在家学习！"

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

    def test_saveedittext(self):
        """保存编辑的文本"""
        sp = CreatPage(self.driver)
        sp.add_button_link()
        sp.run_case("今天天气不错在家学习！")
        #断言：实际结果，预期结果，错误信息
        self.assertEqual(sp.get_finish_button_text(),self.verificationErrors,msg="验证失败！")
  
        
#setup中的启动APP参数可以单独放在一个App.py的文件中，单独提取出来
