#coding:utf-8
__author__='wanghuanhuan'

from selenium import webdriver
from src.common import excel_date,login ,log,openPage,Base_Page
from selenium.webdriver.common.by import By
import time,unittest

class NewCustomer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mylog = log.log()
        login.Login().login()
        cls.basepage = Base_Page.BasePage()
        # cls.customerDict = excel_date.excel().get_LocElements_SheetNum(0)


    def test_001_CreateNewCustomer(self):

        self.customerDict = excel_date.excel().get_LocElements_SheetNum(0)
        customerDict = self.basepage.strTotuple(self.customerDict)
        openPage.OpenPage().page('营业管理','个人客户')
        flag = openPage.OpenPage().page('营业管理','个人客户')

        if flag:
            self.basepage.find_element_click(*customerDict['newCustomer'])
            code = self.basepage.randrom_str('auto',6)
            self.basepage.send_keys(code,*customerDict['code'])
            name = self.basepage.randrom_str('autoName',5)
            self.basepage.send_keys(name,*customerDict['name'])
            self.basepage.find_element_click(*customerDict['certificateTypeId'])
            self.basepage.find_element_click(*customerDict['certificateType'])

            certificateCode = self.basepage.randrom_str('certificate',5)
            self.basepage.send_keys(certificateCode, *customerDict['certificateCode'])
            self.basepage.find_element_click(*customerDict['addressId'])
            self.basepage.find_element_click(*customerDict['address'])

            customerAddress = self.basepage.randrom_str('创业街路,门牌号：',5)
            self.basepage.send_keys(customerAddress, *customerDict['customerAddress'])
            self.basepage.find_element_click(*customerDict['saleAreaId'])
            self.basepage.find_element_click(*customerDict['saleArea'])

            linkTel = self.basepage.randrom_str('185',8)
            self.basepage.send_keys(linkTel, *customerDict['linkTel'])
            self.basepage.find_element_click(*customerDict['certain'])

            text_message = self.basepage.get_text(*customerDict['seccess'])
            self.assertEqual(text_message,'保存成功')

            flag = self.basepage.get_display(*customerDict['messagebox'])
            if flag:
                self.basepage.find_element_click(*customerDict['messagebox'])
            print('新建个人客户成功。')
            self.mylog.info('新建个人客户成功')
            time.sleep(2)

        else:
            self.mylog.error('新建个人客户失败')

    def test_002_ModifyCustomer(self):
        '''客户资料修改-wanghuanhuan'''
        self.customerDict = excel_date.excel().get_LocElements_SheetNum(0)
        customerDict = self.basepage.strTotuple(self.customerDict)
        self.basepage.find_element_click(*customerDict['baseInfo'])
        flag = self.basepage.get_display(*customerDict['messageModify'])
        if flag:
            self.basepage.find_element_click(*customerDict['messageModify'])
            code = self.basepage.randrom_str('Mauto', 5)
            self.basepage.send_keys(code, *customerDict['code'])
            name = self.basepage.randrom_str('MautoName', 5)
            self.basepage.send_keys(name, *customerDict['name'])
            # self.basepage.find_element_click(*customerDict['certificateTypeId'])
            # self.basepage.find_element_click(*customerDict['certificateType'])

            certificateCode = self.basepage.randrom_str('Mcertificate', 5)
            self.basepage.send_keys(certificateCode, *customerDict['certificateCode'])
            # self.basepage.find_element_click(*customerDict['addressId'])
            # self.basepage.find_element_click(*customerDict['address'])

            customerAddress = self.basepage.randrom_str('Modify-创业街路,门牌号：', 5)
            self.basepage.send_keys(customerAddress, *customerDict['customerAddress'])
            # self.basepage.find_element_click(*customerDict['saleAreaId'])
            # self.basepage.find_element_click(*customerDict['saleArea'])

            linkTel = self.basepage.randrom_str('185', 8)
            self.basepage.send_keys(linkTel, *customerDict['linkTel'])
            self.basepage.find_element_click(*customerDict['certain'])

            text_message = self.basepage.get_text(*customerDict['seccessMessage'])
            self.assertEqual(text_message, '操作成功')

            flag = self.basepage.get_display(*customerDict['messagebox'])
            if flag:
                self.basepage.find_element_click(*customerDict['messagebox'])
            print('修改个人客户成功。')
            self.mylog.info('修改个人客户成功')
            time.sleep(2)

        else:
            self.mylog.error('修改客户资料失败')


    def test_003_ModifyPhone(self):
        '''电话信息修改-wanghuanhuan'''
        self.customerDict = excel_date.excel().get_LocElements_SheetNum(0)
        customerDict = self.basepage.strTotuple(self.customerDict)
        flag = self.basepage.get_display(*customerDict['modifyPhone'])
        if flag:
            self.basepage.find_element_click(*customerDict['modifyPhone'])
            contactTel = self.basepage.randrom_str('185',8)
            self.basepage.send_keys(contactTel,*customerDict['contactTel-ModifyPhone'])
            mobileTel = self.basepage.randrom_str('175',8)
            self.basepage.send_keys(mobileTel,*customerDict['mobileTel-ModifyPhone'])
            self.basepage.send_keys(mobileTel,*customerDict['mobileTelConfirm'])

            self.basepage.find_element_click(*customerDict['certain-modifyPhone'])
            text_message = self.basepage.get_text(*customerDict['seccessMessage'])
            self.assertEqual(text_message,'操作成功')
            self.basepage.find_element_click(*customerDict['messagebox'])
            print('电话信息修改成功')
            self.mylog.info('电话信息修改成功')
            time.sleep(1)
        else:
            print('电话信息修改失败')
            self.mylog.error('电话信息修改按钮不可点击')

    def test_004_ModifyPassWord(self):
        '''密码修改-wanghuanhuan'''
        self.customerDict = excel_date.excel().get_LocElements_SheetNum(0)
        customerDict = self.basepage.strTotuple(self.customerDict)
        flag = self.basepage.get_display(*customerDict['ModifyPassWord'])
        if flag:
            self.basepage.find_element_click(*customerDict['ModifyPassWord'])
            newPassword = self.basepage.randrom_str('1',9)
            self.basepage.send_keys(newPassword,*customerDict['newPassword'])
            self.basepage.send_keys(newPassword,*customerDict['confirmPassword'])
            self.basepage.find_element_click(*customerDict['certain-modifyPassWord'])
            text_message = self.basepage.get_text(*customerDict['seccessMessage'])
            self.assertEqual(text_message,'操作成功')
            self.basepage.find_element_click(*customerDict['messagebox'])
            print('密码修改成功')
            self.mylog.info('密码修改成功')
            time.sleep(1)
        else:
            print('密码修改失败')
            self.mylog.error('密码修改按钮不可点击')

    def test_005_ResetPassword(self):
        '''密码重置-wanghuanhuan'''
        self.customerDict = excel_date.excel().get_LocElements_SheetNum(0)
        customerDict = self.basepage.strTotuple(self.customerDict)
        flag = self.basepage.get_display(*customerDict['passwordReset'])
        if flag:
            self.basepage.find_element_click(*customerDict['passwordReset'])
            self.basepage.find_element_click(*customerDict['messagebox-yes'])
            text_message = self.basepage.get_text(*customerDict['seccessMessage'])
            self.assertEqual(text_message, '操作成功',msg='密码重置失败')
            self.basepage.find_element_click(*customerDict['messagebox'])
            print('密码重置成功')
            self.mylog.info('密码重置成功')
            time.sleep(1)
        else:
            print('密码重置失败')
            self.mylog.error('密码修改按钮不可点击')

    def test_006_InvalidCustomer(self):
        '''客户注销-wanghuanhuan'''
        self.customerDict = excel_date.excel().get_LocElements_SheetNum(0)
        customerDict = self.basepage.strTotuple(self.customerDict)
        flag = self.basepage.get_display(*customerDict['Invalid'])
        if flag:
            self.basepage.find_element_click(*customerDict['Invalid'])
            self.basepage.find_element_click(*customerDict['invalidReasonId'])
            self.basepage.find_element_click(*customerDict['invalidReasonId-Move'])
            self.basepage.find_element_click(*customerDict['certain-Invalid'])
            text_message = self.basepage.get_text(*customerDict['seccessMessage'])
            self.assertEqual(text_message,'操作成功',msg='注销失败')
            self.basepage.find_element_click(*customerDict['messagebox'])
            print('注销成功')
            self.mylog.info('注销成功')
            time.sleep(1)
        else:
            print('注销失败')
            self.mylog.error('注销按钮不可点击')

    def test_007_ValidCustomer(self):
        '''客户恢复-wanghuanhuan'''
        self.customerDict = excel_date.excel().get_LocElements_SheetNum(0)
        customerDict = self.basepage.strTotuple(self.customerDict)
        flag = self.basepage.get_display(*customerDict['Valid'])
        if flag:
            self.basepage.find_element_click(*customerDict['Valid'])
            self.basepage.find_element_click(*customerDict['validReasonId'])
            self.basepage.find_element_click(*customerDict['validReasonId-reason'])
            self.basepage.find_element_click(*customerDict['certain-Invalid'])
            text_message = self.basepage.get_text(*customerDict['seccessMessage'])
            self.assertEqual(text_message,'操作成功',msg='恢复失败')
            self.basepage.find_element_click(*customerDict['messagebox'])
            print('恢复成功')
            self.mylog.info('恢复成功')
            time.sleep(1)
        else:
            print('恢复失败')
            self.mylog.error('恢复按钮不可点击')



    @classmethod
    def tearDownClass(cls):
        cls.basepage = Base_Page.BasePage()
        cls.basepage.quit()

if __name__ == '__main__':
    unittest.main()










