# coding:utf-8
# -*- coding: utf-8 -*-
#__author__ = 'renss'

from selenium import webdriver

'''
@author: renss'
@time : 2020/07/20
'''

import time,os

'''
配置全局参数
'''
#获取项目路径
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print("project_path:",project_path)

#默认浏览器
driver = webdriver.Chrome()

'''登录配置'''
url = "http://172.16.6.108/dashboard"
username = "admin"
password = "yjg123456"

'''
path1 = os.path.realpath(__file__)   #D:\HBBoss0726\config\globleparameter.py
print("os.path.realpath(__file__):",path1)
path2 = os.path.realpath(__file__)[0]   #D
print("os.path.realpath(__file__)[0]:",path2)
project_path = os.path.dirname(os.path.realpath(__file__))   #D:\HBBoss0726\config
print("os.path.dirname(os.path.realpath(__file__)):",project_path)
project_path2 = os.path.join(os.path.dirname(os.path.realpath(__file__)[0]),'.')
project_path3 = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]),'.'))  #D:\HBBoss0726\config
print(project_path2)
print(project_path3)
'''

'''测试用例代码存放位置路径（用于构建suite，注意该文件夹下的文件都应该以test_ 开头命名）'''
test_case_path = project_path+"\\src\\test_case"

'''excel测试数据文档存放路径'''
test_data_path = project_path+"\\data\\123.xlsx"

'''日志文件存放路径'''
log_path = project_path+"\\log\\mylog.log"

'''测试报告文件存放路径,并以当前时间作为测试报告的前缀'''
report_path = project_path+"\\report\\"
report_name = report_path+time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
print("report_path:",report_path)
print("report_name:",report_name)

'''异常截图存储路径，并以当前时间作为报名名称前缀'''
img_path = project_path+"\\error_img\\"+time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime())

'''发送邮箱的信息'''
smtp_server = 'smtp.XXXX.com.cn'
email_name = '470971464@qq.com'    #发件人邮箱
email_password = 'Puluxi@470971'  #发件人密码
email_to = '470971464@qq.com'   #收件人