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
    now_handle = browser.current_window_handle
    for new_handle in all_handles:
        if new_handle != now_handle:
            browser.switch_to.window(new_handle)

file = open('/Users/chenwenbin/PycharmProjects/Jarvis/toutiao_news_data.csv','w',encoding='utf-8-sig')
writer = csv.writer(file)
writer.writerow(('新闻标题','新闻发布时间','新闻作者','新闻正文','新闻插图'))

# 搜索关键词
keyword = "托育"

# 驱动，打开头条门户首页
browser = webdriver.Chrome("/usr/local/bin/chromedriver")
browser.get('https://www.toutiao.com/search/?keyword={}'.format(keyword))
sleep(3)

# 下拉3次，获取足够资讯操作
js="var q=document.documentElement.scrollTop=100000"
for i in range(3):
    browser.execute_script(js)
    sleep(3)

# 逐条打开搜索结果中的链接，gne提取
for i in range(2,12):
    browser.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[3]/div/div/div[{}]/div/div/div[1]/div/div[1]/a/span".format(i)).click()
    switch_new_window()
    extractor = GeneralNewsExtractor()
    result = extractor.extract(browser.page_source)
    writer.writerow((result['title'],result['publish_time'],result['author'],result['content'],result['images']))
    browser.close()
    browser.switch_to.window(browser.window_handles[0])

sleep(2)
browser.quit()