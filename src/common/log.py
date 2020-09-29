# coding=utf-8
from imp import reload

__author__ = 'renss'

import logging
from config import globleparameter as gl
import sys
# sys.getdefaultencoding()
# sys.setdefaultencoding('utf-8')


'''
配置日志文件，输出INFO 级别以上的日志
'''
class log:
    def __init__(self):
        self.logname = 'mylog'

    def setMSG(self, level, msg):
        logger = logging.getLogger()

        # 定义Handle 输出到文件和控制台
        fh = logging.FileHandler(gl.log_path)
        ch = logging.StreamHandler()

        # 定义日志的输出格式
        formater = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        fh.setFormatter(formater)
        ch.setFormatter(formater)

        # 添加Handle
        logger.addHandler(fh)
        logger.addHandler(ch)

        # 添加日志信息，输出INFO级别的日志
        logger.setLevel(logging.INFO)
        if level == 'debug' :
            logger.debug(msg)
        elif level == 'info' :
            logger.info(msg)
        elif level == 'warning' :
            logger.warning(msg)
        elif level == 'error':
            logger.error(msg)

        # 移除句柄，否则日志会重复输出
        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()

    def debug(self,msg):
        self.setMSG('debug',msg)

    def info(self,msg):
        self.setMSG('info',msg)

    def warning(self,msg):
        self.setMSG('warning',msg)

    def error(self,msg):
        self.setMSG('error',msg)


