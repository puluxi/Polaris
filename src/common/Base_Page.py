#coding:utf-8
__author__ = 'renss'
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from src.common import log
from config import globleparameter as gl
import random

'''
project : 封装页面的公共方法
'''
class BasePage(object):
    def __init__(self, selenium_driver=gl.driver, base_url=gl.url):
        self.driver = selenium_driver
        self.url = base_url
        #self.title = page_title
        self.mylog = log.log()

    #打开页面，校验连接是否正确加载
    def open(self,url):
        '''打开浏览器'''
        try :
            self.driver.get(url)
            self.driver.maximize_window()
            # 通过断言输入的title 是否在当前的title 中
            #assert page_title in self.driver.title,u'打开页面失败%s'%url
        except:
            self.mylog.error(u'未能正确打开页面：'+url)

    # def open(self):
    #     '''打开浏览器'''
    #     self._open(self.url)

    def refresh(self):
        '''刷新页面'''
        self.driver.refresh()

    def maximize_window(self):
        '''浏览器页面最大化'''
        self.driver.maximize_window()

    def back(self):
        '''回退'''
        self.driver.back()

    def quit(self):
        '''退出驱动程序和所有的窗口'''
        self.driver.quit()

    def close_browser(self):
        '''关闭当前窗口'''
        self.driver.close()

    def get_title(self):
        '''获取页面的Title'''
        return self.driver.title

    def get_url(self):
        '''获取页面的 URL'''
        return self.driver.current_url

    def implicitly_wait(self,seconds):
        '''隐式等待'''
        self.driver.implicitly_wait(seconds)

    # 重写 find_element 方法，增加定位元素的健壮性
    def find_element(self,*loc):
        '''
        确保所有的元素是可见的
        :param loc: 注意：入参的是元组，需要加*， 注意：以下入参本身是元组，不需要加*
        # WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*loc).display())
        :return:
        '''
        '''
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc),message='元素不可见')
        return element
        '''
        try :
            WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc),message='元素不可见')
            return self.driver.find_element(*loc)
        except:
            self.mylog.error(u'找不到元素'+str(loc))

    def find_element_click(self,*loc):
        '''点击某个元素'''
        # self.find_element(*loc).click()
        try:
            element=WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(loc),message='元素不可见')
            element.click()
        except WebDriverException:
            self.mylog.error(u'找不到元素'+str(loc))



    # # 重写 send_keys 方法
    # def send_keys(self,loc,value,clear=True):
    #     try:
    #         if clear:
    #             self.find_element(*loc).clear()
    #         self.find_element(*loc).send_keys(str(value))
    #     except AttributeError:
    #         self.mylog.error(u'输入失败,Loc='+str(loc)+';value='+value)
    #     except ArithmeticError:
    #         self.mylog.error(u'页面中找不到元素：'+str(loc))


    def send_keys(self,value,*loc,clear=True):
        '''重写 send_keys 方法'''
        try:
            if clear:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(str(value))
        except AttributeError:
            self.mylog.error(u'输入错误，loc='+str(loc)+';value='+value)
        except ArithmeticError:
            self.mylog.error(u'页面找不到元素：'+str(loc))


    def get_attribute(self,attribute,*loc):
        '''获取元素值'''
        try:
            return self.find_element(*loc).get_attribute(attribute)
        except:
            self.mylog.error(u'获取元素的属性值失败：'+str(loc))

    def get_text(self,*loc):
        '''获取元素文本信息'''
        try:
            return self.find_element(*loc).text
        except:
            self.mylog.error(u'获取元素文本信息失败：'+str(loc))

    def get_display(self,*loc):
        '''获取元素是否可见'''
        try:
            return self.find_element(*loc).is_displayed()
        except:
            self.mylog.error(u'获取元素不可见：'+str(loc))

    def get_enabled(self,*loc):
        '''获取元素是否可点击'''
        try:
            return bool(self.find_element(*loc).is_enabled())
        except:
            self.mylog.error(u'获取元素不可见')

    # 截图
    def img_screenshot(self,img_name):
        try:
            self.driver.get_screenshot_as_file(gl.img_path+img_name+'.png')
        except:
            self.mylog.error(u'截图失败：'+gl.img_path+img_name+'.png')

    def execute_script(self,src):
        try:
            self.driver.execute_script(src)
        except:
            self.mylog.error(u'执行脚本失败：'+src)

    def switch_frame(self,loc):
        try:
            self.driver.switch_to_frame(loc)
        except:
            self.mylog.error(u'切换frame失败：'+str(loc))

    def wait_not_visible(self,*loc):
        '''
        等待元素消失
        :param loc:定位器
        :return: Web_Element
        '''
        try:
            WebDriverWait(self.driver,30).until_not(EC.visibility_of_element_located(loc),message=u'元素没有消失')
            return True
        except TimeoutException:
            self.mylog.error(u'仍然存在指定元素：'+str(loc))


    def find_mistake(self,*loc):
        '''
        用来查询错误，如果查询不到不报错
        :param loc: 定位器
        :return: Web_Element
        '''
        try:
            web_element = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc),
                                                                          message=u'定位失败')
            self.mylog.debug(u'有错误提示信息：%s'%web_element.text)
            return web_element
        except WebDriverException:
            return False

    def right_click(self,*loc):
        '''
        对定位到的元素执行鼠标右键操作
        :param loc:定位器
        :return:
        '''
        element_RightClick = self.find_element(*loc)
        ActionChains(self.driver).context_click(element_RightClick).perform()

    def move_to(self,*loc):
        '''
        鼠标移动
        :param loc:定位器
        :return:
        '''
        element = self.find_element(*loc)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self,*loc):
        '''
        对定位到的元素执行双击操作
        :param loc: 定位器
        :return:
        '''
        element = self.find_element(*loc)
        ActionChains(self.driver).double_click(element).perform()

    def is_on_dom(self,*loc):
        '''
        在页面Dom结果中查找element
        :param loc: 定位器
        :return: bool
        '''
        try:
            self.mylog.debug(u"查找页面中是否存在:%s"%loc[1])
            WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc),message=u'元素不可见')
            return  True
        except WebDriverException:
            self.mylog.error(u'未找到元素：%s'%loc[1])
            return False

    def find_text_in_element(self,text,*loc):
        '''
        当前元素是否存在期望文字
        :param loc: 定位器
        :return: bool
        '''
        try:
            WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(loc,text))
            return True
        except WebDriverException:
            self.mylog.error(u"元素text不存在：%s"%text)
            return False

    def clickable(self,*loc):
        '''
        查找元素是否可点击
        :param loc: 定位器
        :return:
        '''
        try:
            WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(loc))
            return True
        except WebDriverException:
            self.mylog.error(u'元素不可点击：%s'%str(loc))
            return False

    def get_page_source(self):
        '''获取页面源码'''
        return self.driver.page_source

    def text_in_page_source(self,text):
        '''查看页面是否存在特定值'''
        return text in self.get_page_source()

    def strTotuple(self,dict):
        '''字典中的values 转换为元组tuple'''
        for key,value in dict.items():
            value = eval(value)
            dict[key] = value
        return dict

    def randrom_str(self,string,length,char=False):
        '''生成固定长度的随机数'''
        string = list(string)
        if char:
            for i in range(length):
                x = random.randint(1,2)
                if x == 1:
                    y = str(random.randint(0,9))
                else:
                    y = chr(random.randint(97,122))
                string.append(y)

        else:
            for i in range(length):
                y = str(random.randint(0,9))
                string.append(y)

        string = ''.join(string)
        return string


