# =============================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-05-30
# @Author  : wenbin
# @FileName: main.py
# @Software: PyCharm
# =============================================

from spiders.COVID import data_get
from spiders.COVID import data_wordcloud
from spiders.COVID import data_map

data_dict = data_get.init()
data_get.china_total_data(data_dict)
data_get.global_total_data(data_dict)
data_get.china_daily_data(data_dict)
data_get.foreign_daily_data(data_dict)

data_map.all_map()