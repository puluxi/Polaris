# coding:utf-8
__author__ = 'renss'
import os,smtplib,os.path
from config import globleparameter as gl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from log import log
from src.common import log

'''
邮件发送最新的测试报告
'''

class send_email:
    def __init__(self):
        self.mylog = log.log()

    # 定义邮件内容
    def email_init(self,report,reportName):
        with open(report,'rb') as f:
            mail_body = f.read()

        #创建一个带附件的邮件实例
        msg = MIMEMultipart()
        # 以测试报告作为邮件正文
        msg.attach(MIMEText(mail_body,'html','utf-8'))
        report_file = MIMEText(mail_body,'html','utf-8')

        #定义附件名称
        report_file['Content-Disposition'] = 'attachment;filename='+reportName

        # 添加附件
        msg.attach(report_file)
        #邮件标题、发件人、收件人
        msg['Subject'] = 'Polaris-UI自动化测试报告：'+reportName
        msg['From'] = gl.email_name
        msg['To'] = gl.email_to
        try:
            server = smtplib.SMTP_SSL(gl.smtp_server,465)
            server.login(gl.email_name,gl.email_password)
            # server.sendmail(msg['From'],msg['To'].split(';'), msg.as_string())
            server.sendmail(msg['From'],msg['To'], msg.as_string())
            print(u'邮件发送成功，文件名称：',reportName)
            self.mylog.info(u'邮件发送成功，文件名称：'+reportName)
            server.quit()
        except smtplib.SMTPException as e:
            print(e)
            self.mylog.error(u'邮件发送测试结果失败 at'+__file__)

    def sendReport(self):
        # 找到最近的测试文件（包含路径）
        report_list = os.listdir(gl.report_path)
        report_list.sort(key = lambda fn:os.path.getmtime(gl.report_path+fn) if not os.path.isdir(gl.report_path+fn) else 0)
        new_report = os.path.join(gl.report_path,report_list[-1])
        print("new_report:",new_report)
        print("report_list:",report_list)
        print("report_list[-1]:",report_list[-1])
        # 发送邮件
        self.email_init(new_report,report_list[-1])

# if __name__ == '__main__':
#     email = send_email()
#     email.sendReport()









