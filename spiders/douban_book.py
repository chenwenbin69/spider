# -*- coding:utf-8 -*-

__author__ = 'wenbin'

import requests
from lxml import etree
import csv

f = open('/files/豆瓣读书top250.csv', 'w', encoding='utf-8')
writer = csv.writer(f)
writer.writerow(('书名','详情链接','作者','评分','建平'))

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
headers = {'User-Agent' : user_agent}

def get_top_book():
    for i in range(0, 250, 25):
        top_url = 'https://book.douban.com/top250?start={}&filter='.format(i)
        res = requests.get(url=top_url, headers=headers).text
        html_etree = etree.HTML(res)
        tables = html_etree.xpath('//tr[@class="item"]')
        for table in tables:
            book_name = table.xpath('td/div/a/@title')[0]
            detail_url = table.xpath('td/div/a/@href')[0]
            book_info = table.xpath('td/p/text()')[0]
            author = book_info.split('/')[0]
            rate = table.xpath('td/div/span[2]/text()')[0]
            comments = table.xpath('td/p/span/text()')
            print(book_name,detail_url,author,rate,comments)
            writer.writerow((book_name,detail_url,author,rate,comments))

if __name__ == '__main__':
    get_top_book()