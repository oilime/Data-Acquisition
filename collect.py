# -*- coding:utf-8 -*-
from __future__ import division
import requests
from bs4 import BeautifulSoup
import math
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

__metaclass__ = type


class Good:
    def __init__(self, name, price, group, img, goodtype, weight=0):
        self.__name = name
        self.__price = price
        self.__group = group
        self.__img = img
        self.__type = goodtype
        self.__weight = weight

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

    def get_good_weight(self):
        return self.__weight


f = open('data.txt', 'w')
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
url = 'https://shop.48.cn/Goods'
start_html = requests.get(url, headers=headers).content
soup = BeautifulSoup(start_html, "lxml")
shop = soup.find('div', class_='body-content').find('span', class_='pink')
num = int(shop.get_text())
pagecount = 80
pagenum = 0
data = []

while pagenum < math.ceil(num/pagecount):
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
        price = soup.find('li', class_='i_jg').find('span')
        group = soup.find('li', class_='i_num').find_all('span')[1].get_text()
        goodtype = soup.find('li', class_='i_num').find_all('span')[3].get_text()
        img = soup.find('div', class_='pic_m').find('a')['href']

        print name.encode('utf-8')
        # data.append(Good(name, price, group, img, goodtype))
        k = ''.join(name.encode('utf-8')) #.join(' ').join(price.encode('utf-8')).join(' ').join(group.encode('utf-8')).join(' ').join(goodtype.encode('utf-8'))
        f.write(k + '\n')
        f.flush()
    pagenum += 1
f.close()
print 'over!!!'


