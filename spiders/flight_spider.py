# -*- coding:utf-8 -*-

__author__ = 'wenbin'

"""
携程低价机票网址
https://flights.ctrip.com/itinerary/roundtrip/sha-hld?date=2020-05-09%2C2020-05-12&sortByPrice=true
"""

import requests
import json
from datetime import datetime,timedelta

city_map = {'上海' : 'sha',
             '北京' : 'bjs',
             '呼伦贝尔' : 'hld'
}
city_dict_to_reverse = { v:k for k,v in city_map.items()}  # 翻转dict，调换key和value的位置，便于在屏幕上输出地名
source = city_map['上海']
destination = city_map['呼伦贝尔']
weeks = [0,1,2,3,4,5,6] # 判断日期为周几时使用
days = []
duration = 4    # 游玩周期3天
url = 'https://flights.ctrip.com/itinerary/api/12808/lowestPrice'
headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

payload = {"flightWay":"Roundtrip","dcity":source,"acity":destination,"army":False}
res = requests.post(url=url,json=payload)
res = json.loads(res.text)
# print(res['data']['roundTripPrice'])

# 遍历所有旅程开始日期
for k in res['data']['roundTripPrice'].keys():
    days.append(k)

for firstday in days:
    week = datetime.strptime(firstday,"%Y%m%d").weekday()
    if week == weeks[4]:    # 4是周五，预计周五出发，好请假
        firstday_date = datetime.strptime(firstday,'%Y%m%d').date()
        lastday_date = firstday_date + timedelta(days=duration)
        print("出发地：{}，目的地：{}".format(city_dict_to_reverse[source],city_dict_to_reverse[destination]))
        print("出发日期：{}，返程日期：{}。".format(firstday_date,lastday_date))
        lastday = datetime.strftime(lastday_date,'%Y%m%d')
        price_list = res['data']['roundTripPrice'][firstday]
        if lastday in price_list.keys():
            print("间隔{}天往返票价：￥{}".format(duration,price_list[lastday]) + '\n' + '#'*20 + '\n')
        else:
            print("懒得处理了！" + '\n')

