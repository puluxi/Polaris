#coding:utf-8
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from src.common.log import log
from src.common.Base_Page import BasePage
from config import globleparameter as gl

class Login(BasePage):

    logintime =1
    def login(self, driver=gl.driver, url=gl.url, username=gl.username, password=gl.password):
        global logintime
        self.url = url
        self.driver = driver
        self.username = username
        username_loc = (By.XPATH,u"//input[@id='login-form_username']")
        password_loc = (By.XPATH,"//input[@id='login-form_password']")
        buttonlogin_loc = (By.XPATH,u"//button[@type='submit']")

        self.basepage = BasePage(self.driver, self.url)
        self.open(self.url)
        # print('username_loc:',username_loc)
        # print('*password_loc:',*password_loc)
        # print('str(password_loc):',str(password_loc))
        self.basepage.send_keys(username,clear=True,*username_loc)
        # time.sleep(2)
        # self.basepage.send_keys(password_loc,password)
        self.basepage.send_keys(password,*password_loc)
        # time.sleep(2)
        self.basepage.find_element_click(*buttonlogin_loc)

        title = self.basepage.get_title()
        print("Title:",title)
        assert("Polaris" in title), "'首页'不在当前 Title 中：%s"%title


        # 是否显示主界面(导航栏)
        homePage_loc = (By.XPATH,u"//ul[@role='menu']")
        local_loc = (By.XPATH, "//span[.='系统管理']")
        flag =  self.basepage.get_display(*homePage_loc)
        print("是否展示主界面：True/是 False/否")
        print(flag)
        # print("主界面clickable:",self.basepage.clickable(*homePage_loc))

        if flag:
            for i in range(10):
                style = self.driver.find_element_by_xpath("//span//span[.='系统管理']").get_attribute("style")
                print(style)
                if style == "display: block;":
                    print('Login seccess')
                    break
                else:
                    # time.sleep(2)
                    # i +=1
                    pass

        #选择渠道
        elif self.basepage.clickable(*local_loc):
            for m in range(10):
                mainFramePanel_loc = (By.XPATH,"//span//span[.='系统管理']")
                type = self.basepage.get_attribute("style",*mainFramePanel_loc)
                # type = self.driver.find_element_by_xpath("//div[@id='mainFramePanel']").get_attribute("style")
                print(type)
                if type == "display: none;":
                    time.sleep(2)
                    m +=1
                else:
                    print("Login seccess.")
                    break
        else:
            if logintime <3:
                logintime +=1
                print("Login again.")
                print("Logintimes is %s"% logintime)
                Login().login()




# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     login = Login(driver)
#     login.login(driver)
#     driver.quit()












