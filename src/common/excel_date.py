# coding:utf-8
__author__ = "renss"

import xlrd
from src.common import log
from config import globleparameter as gl

'''
读取 excel 文件
'''
class excel :
    def __init__(self):
        self.mylog = log.log()

    def open_excel(self,file):
        '''
        读取excel文件
        :param file: excel 文件目录
        :return: excel 文件信息
        '''
        try:
            xls = xlrd.open_workbook(file)
            return xls
        except Exception:
            self.mylog.info(r"打开 excel 文件失败")

    def excel_table(self,file,sheetNumber):
        '''
        将 excel 文件中数据装载 dict
        :param file: excel文件
        :param sheetName: excel文件中sheetName 的名字
        :return: excel文件中的数据
        '''
        # 打开 excel 文件
        data = self.open_excel(file)
        # 根据sheetName 名称获取一个工作表
        table = data.sheets()[sheetNumber]
        # 获取行数
        rows = table.nrows
        # 获取 第一行数据
        Tco1name = table.row_values(0)
        # lister = []
        # for rownumber in range(1,rows):
        #     row = table.row_values(rownumber)
        #     if row:
        #         app ={}
        #         for i in range(len(Tco1name)):
        #             app[Tco1name[i]] = row[i]
        #             lister.append(app)
        # return lister
        ele_dict = {}
        value = []
        for rownumber in range(1,rows):
            row_value = table.row_values(rownumber)
            # print(row_value)
            value.append(row_value)
        # print(value)
        ele_dict.update(dict(value))
        return ele_dict


    def get_LocElements_SheetNum(self,sheetNumber,file=gl.test_data_path):
        try:
            date_dict = self.excel_table(file,sheetNumber)
            # assert len(date_list)>=0 ,u'excel 标签页：'+sheetname+r'为空'
            return date_dict
        except Exception as e:
            print(e)
            self.mylog.error(u'excel 标签页：sheetNumber='+sheetNumber+u'为空')

    def get_LocElements_SheetName(self,sheetName,file=gl.test_data_path):
        try:
            data = xlrd.open_workbook(file)
            table = data.sheet_by_name(sheetName)
            rows = table.nrows
            ele_dict = {}
            for rownumber in range(1,rows):
                value = table.row_values(rownumber)
                ele_dict.update(dict([value]))
            return ele_dict
        except Exception as e:
            print(e)
            self.mylog.error(u'excel 标签页：sheetName='+sheetName+u'为空')


# if __name__ == '__main__':
#     Excel = excel()
#     print(Excel.get_LocElements_SheetNum(0))
#     print(Excel.get_LocElements_SheetName('NewCustomer'))
    # print(Excel.get_LocElements_SheetNum(1))
    # print(Excel.get_LocElements_SheetName('1'))







