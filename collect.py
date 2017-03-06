# -*- coding:utf-8 -*-
from __future__ import division
import requests
from bs4 import BeautifulSoup
import math
import os


__metaclass__ = type
class Good:
    def __init__(self, name, price, group, img, goodtype):
        self.__name = name
        self.__price = price
        self.__group = group
        self.__img = img
        self.__type = goodtype

    def get_good_name(self):
        return self.__name

    def get_good_price(self):
        return self.__price

    def get_good_group(self):
        return self.__group

    def get_good_type(self):
        return self.__type

    def get_good_img(self):
        return self.__img


headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
url = 'https://shop.48.cn/Goods'
start_html = requests.get(url, headers=headers).content
soup = BeautifulSoup(start_html, "lxml")
shop = soup.find('div', class_='body-content').find('span', class_='pink')
num = int(shop.get_text())
pagecount = 80
pagenum = 1

while pagenum <= math.ceil(num/pagecount):
    url = 'https://shop.48.cn/Goods?totalCount={}&brand_id=-1&pageNum={}&numPerPage={}'.format(num, pagenum, pagecount)
    shop_html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(shop_html, 'lxml')
    shop = soup.find('div', class_='goods').find_all('div', class_='gs_xx')
    for good in shop:
        link = good.find('li', class_='gs_1').find('a')['href']
        url = 'https://shop.48.cn{}'.format(link)
        good_html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(good_html, 'lxml')
        name = soup.find('li', class_='i_tit').get_text()
        print name
        price = soup.find('li', class_='i_jg')
        print price
    pagenum += 1


