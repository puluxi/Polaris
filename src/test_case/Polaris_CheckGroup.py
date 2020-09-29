from src.common import excel_date,log,login,openPage,Base_Page
import  time,unittest
class CheckGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mylog = log.log()
        login.Login().login()
        cls.basepage = Base_Page.BasePage()

    def test_CheckGroup_001(self):
        self.customerDict = excel_date.excel().get_LocElements_SheetNum(0)
        customerDict = self.basepage.strTotuple(self.customerDict)
        flag = self.basepage.get_display(*customerDict['homePageCheck'])
        if flag:
            self.basepage.find_element_click(*customerDict['systemManageBar'])
            self.basepage.find_element_click(*customerDict['areaManageBar'])
            text_message = self.basepage.get_text(*customerDict['enterAreaPageFlag'])
            self.assertEqual(text_message, '区域名称')
            print('查看区域分组成功。')
            self.mylog.info('查看区域分组成功')
            time.sleep(2)
        else:
            print('查看区域失败')
            self.mylog.error('查看区域分组失败')
    def test_CreateArea_002(self):
        self.customerDict = excel_date.excel().get_LocElements_SheetNum(0)
        customerDict = self.basepage.strTotuple(self.customerDict)
        flag = self.basepage.get_display(*customerDict['homePageCheck'])
        if flag:
            self.basepage.find_element_click(*customerDict['systemManageBar'])
            self.basepage.find_element_click(*customerDict['areaManageBar'])
            areaNumber = '区域1'
            self.basepage.send_keys(areaNumber, *customerDict['areaNumber'])
            self.basepage.find_element_click(*customerDict['areaSearchButton'])
            text_message = self.basepage.get_text(*customerDict['areaItemVerify'])
            self.assertEqual(text_message, '查询区域1成功')
            print('查询区域1成功。')
            self.mylog.info('查询区域1成功')
            time.sleep(2)
        else:
            print('查看区域1失败')
            self.mylog.error('查看区域分1失败')

    @classmethod
    def tearDownClass(cls):
        cls.basepage = Base_Page.BasePage()
        cls.basepage.quit()

if __name__ == '__main__':
    unittest.main()