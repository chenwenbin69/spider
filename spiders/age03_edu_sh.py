# -*- coding:utf-8 -*-

__author__ = 'wenbin'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv
import json

"""
参考爬取页面的html源码
动态加载数据的取数逻辑
"""
class DataSeeker:
    def __init__(self,json_data):
        self.__json_data = json.loads(json_data)

    # 获取公司名称
    def get_name(self):
        name = self.__json_data['dislst'][0]['Name']
        return name

    # 获取机构号
    def get_licNo(self):
        licNo = self.__json_data['dislst'][0]['LicNo']
        return licNo

    # 获取机构类型
    def get_type(self):
        def __get():
            nJGSX = self.__json_data['dislst'][0]['nJGSX']
            if nJGSX == 1:
                return '非营利性托育机构'
            elif nJGSX == 2:
                return '免费福利性托育点'
            elif nJGSX == 3:
                return '营利性托育机构'
        return __get()

    # 获取服务形式
    def get_division(self):
        def __get():
            sJGLX = self.__json_data['dislst'][0]['sJGLX']
            if sJGLX[1] != -1:
                return '全日制'
            elif sJGLX[2] != -1:
                return '半日制'
            elif sJGLX[3] != -1:
                return '计时制'
        return __get()

    # 获取区托育服务管理机构
    def get_sDept(self):
        SDept = self.__json_data['dislst'][0]['SDept']
        return SDept

    # 获取机构负责人
    def get_captain(self):
        captain = self.__json_data['dislst'][0]['Captain']
        return captain

    # 获取联系电话
    def get_mobile(self):
        sFZRDH = self.__json_data['dislst'][0]['sFZRDH']
        return sFZRDH

    # 获取举办者
    def get_IssueBy(self):
        IssueBy = self.__json_data['dislst'][0]['IssueBy']
        return IssueBy

    # 获取地址
    def get_address(self):
        Address = self.__json_data['dislst'][0]['Address']
        return Address

    # 获取供餐情况
    def get_food(self):
        def __get():
            nGCQK = self.__json_data['dislst'][0]['nGCQK']
            if nGCQK == 1:
                return '自行加工膳食'
            elif nGCQK == 2:
                return '不自行加工膳食，但提供供餐服务'
            elif nGCQK == 3:
                return '不提供膳食'
        return __get()

    # 获取收费标准
    def get_fee(self):
        dSFBZ = self.__json_data['dislst'][0]['dSFBZ']
        return dSFBZ

# 打开文件，准备写入数据
file = open('/files/age03_edu_sh_data.csv', 'w', encoding='utf-8-sig')
writer = csv.writer(file)
writer.writerow(('机构名称','机构编号','机构类型','服务形式','区托育服务管理机构','机构负责人','机构联系电话','举办者','地址','供餐情况','收费情况[元/月]'))

# 实例化浏览器对象，打开爬取页面
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('http://age03.edu.sh.cn/schoolall.aspx')
sleep(1)

def next_page():
    browser.find_element_by_xpath('//*[@id="lvSch_Pager"]/a[2]').click()

def for_each():
    for index in range(14):
        browser.find_element_by_xpath('//*[@id="lvSch_ctrl{}_ImageButton1"]'.format(index)).click()
        # 显示等待元素出现，最多等待10秒
        # try:
        #     element = WebDriverWait(browser, 10).until(
        #         EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[3]/input[1]'))
        #     )
        # finally:
        #     sleep(3)  # 绝对粗暴等待，双保险

        sleep(3)
        try:
            source_data = browser.find_element_by_id('hideDataSource').get_attribute('value')
            if len(json.loads(source_data)['dislst']) != 0:
                info = DataSeeker(source_data)
            else:
                source_data = browser.find_element_by_id('hideDataSourcehavepoint').get_attribute('value')
                info = DataSeeker(source_data)
            print(info.get_name(), info.get_fee(), info.get_IssueBy(), info.get_food())
            writer.writerow((info.get_name(), info.get_licNo(), info.get_type(), info.get_division(),
                             info.get_sDept(), info.get_captain(), info.get_mobile(), info.get_IssueBy(),
                             info.get_address(), info.get_food(), info.get_fee()))
        finally:
            browser.refresh()
            sleep(1)
            browser.back()
            sleep(1)
            browser.refresh()
            sleep(2)

# page_source = browser.page_source
# print(page_source)


def dealwith_one_page():
    for_each()
    next_page()

for counter in range(19):
    if counter < 19:
        dealwith_one_page()

# browser.quit()
