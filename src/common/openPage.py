# coding:utf-8
__author__ = 'wanghuanhuan'

from src.common import Base_Page,log,login
from config import globleparameter as gl
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class OpenPage():
    def __init__(self):
        pass


    def page(self, subPage, desPage):
        '''
        打开目的页面
        :return:
        '''
        flag = True
        n=0
        while flag:
            try:
                self.basepage = Base_Page.BasePage()
                #打开主菜单、子页面、目的页面
                locator_mian = (By.XPATH,u"//span[@class='antd-pro-layouts-styles-header-title']")
                locator_sub = (By.XPATH,u"//div[@class='ant-menu-submenu-title']//span//span[text()='"+subPage+"']")
                locator_des = (By.XPATH,u"//span[text()='"+desPage+"']")

                self.basepage.find_element_click(*locator_mian)
                self.basepage.find_element_click(*locator_sub)
                self.basepage.find_element_click(*locator_des)
                print('登录到：%s 页面成功'%desPage)
                time.sleep(2)
                return flag

            except:
                n = n +1
                if n==5:
                    print('登录到：%s 页面失败'%desPage)
                    return flag

# if __name__ == '__main__':
#     loginpage = login.Login()
#     loginpage.login()
#     opensubpage = OpenPage()
#     opensubpage.page('营业管理','个人客户')






