# coding : utf-8
__author__ = 'wanghuanhuan'

import unittest,time,HTMLTestRunner
from config import globleparameter as gl
from src.common import send_mail

'''
创建测试套件，并执行用例
'''

#构建测试集，包含 src/test_case 文件夹下所有的以 test 开头的 .py 文件
suite = unittest.defaultTestLoader.discover(start_dir=gl.test_case_path,pattern='Polaris*.py')

#执行测试
if __name__ == "__main__":
    report = gl.report_name+"Report.html"
    fb = open(report,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb,
                                           title=u'UI自动化测试报告',
                                           description=u'测试用例执行情况：')
    runner.run(suite)
    fb.close()

    #发送邮件
    time.sleep(10)
    email = send_mail.send_email()
    email.sendReport()

