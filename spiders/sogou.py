# -*- coding:utf-8 -*-

__author__ = 'wenbin'

from selenium import webdriver
from gne import GeneralNewsExtractor
from time import sleep
import csv

"""switch to new open window
"""
def switch_new_window():
    all_handles = browser.window_handles
    current_handle = browser.current_window_handle
    for new_handle in all_handles:
        if new_handle != current_handle:
            browser.switch_to.window(new_handle)


file = open('/Users/chenwenbin/PycharmProjects/Jarvis/sogou_news_data.csv','w',encoding='utf-8-sig')
writer = csv.writer(file)
writer.writerow(('新闻标题','新闻发布时间','新闻作者','新闻正文','新闻插图'))

# 搜索关键词
keyword = "托育"

# 驱动，打开头条门户首页
browser = webdriver.Chrome("/usr/local/bin/chromedriver")
browser.get("https://www.sogou.com/sogou?ie=utf8&interation=1728053249&interV=&pid=sogou-wsse-9fc36fa768a74fa9&mode=1&p=31040300&query={}".format(keyword))
sleep(3)

for i in range(1,11):
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div/div[{}]/div/h3/a'.format(i)).click()
    switch_new_window()
    extractor = GeneralNewsExtractor()
    result = extractor.extract(browser.page_source)
    writer.writerow((result['title'], result['publish_time'], result['author'], result['content'], result['images']))
    browser.close()
    browser.switch_to.window(browser.window_handles[0])

sleep(3)
browser.quit()