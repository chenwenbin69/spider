# -*- coding:utf-8 -*-

__author__ = 'wenbin'

import requests
import time

base_url = "https://app.api.ke.com" # 贝壳app域名
search_secondhand_api = "/house/ershoufang/searchv5"    # 搜索小区二手房

cityid_list = [320600]
garden_list = ["rs高迪晶城"]

secondhand_params = {
    "cityId" : cityid_list[0],
    "condition" : garden_list[0],
    "containerType" : 1,
    "from" : "history_click",
    "fullFilters" : 1,
    "limitCount" : 20,
    "limitOffset" : 0,
    "refer" : "ershoulistsearch",
    "request_ts" : int(time.time())
}

print(int(time.time()))

headers = {
    "Lianjia_Device_Id" : "9B2C6D9A-2494-46D0-A69A-820AD05C65BD",
    "Authorization" : "MjAxODAxMTFfaW9zOjEwNTM4NjU1N2U2MTlmNjQ5NTdlZDJjMmE3N2Q5N2NiN2Q4ZDFjNTg=",
    "User-Agent" : "Beike 2.29.0;iPhone10,3;iOS 13.4;"
}

cookies = {
    "lianjia_uuid" : "A8BB9CAB-41DF-4B06-B1D6-86C31455B929",
    "lianjia_ssid" : "D7D8C620-81B0-476B-A2A4-16F5709BB9FD",
    "lianjia_udid" : "9B2C6D9A-2494-46D0-A69A-820AD05C65BD",
    "lianjia_token" : "2.0015cd12ae69dfb44404603b9f9dbcc01f"
}

beike_session = requests.session()
requests.utils.add_dict_to_cookiejar(beike_session.cookies, cookies)

secondhand_res = beike_session.get("{}{}".format(base_url,search_secondhand_api,secondhand_params),headers=headers)
# print(secondhand_res.text)

