# -*- coding:utf-8 -*-
from __future__ import division
import requests
from bs4 import BeautifulSoup
import math
import sys
import datetime
reload(sys)

sys.setdefaultencoding('utf-8')

begin = datetime.datetime.now()
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
url = 'https://shop.48.cn/Goods'
start_html = requests.get(url, headers=headers).content
soup = BeautifulSoup(start_html, "lxml")
shop = soup.find('div', class_='body-content').find('span', class_='pink')
num = int(shop.get_text())
pagecount = 80
pagenum = 0
data = []

with open('data.txt', 'w') as f:
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
            name = soup.find('li', class_='i_tit').get_text().encode('utf-8')
            price = soup.find('li', class_='i_jg').find('span').get_text().encode('utf-8')
            group = soup.find('li', class_='i_num').find_all('span')[1].get_text().encode('utf-8')
            goodtype = soup.find('li', class_='i_num').find_all('span')[3].get_text().encode('utf-8')
            img = soup.find('div', class_='pic_m').find('a')['href']
            k = ', '.join([name, price, group, goodtype, img])
            f.write(k + '\n')
            f.flush()
        pagenum += 1
end = datetime.datetime.now()
print 'Exec time: ', end - begin


