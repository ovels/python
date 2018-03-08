#!/usr/bin/env python
# encoding=utf-8
import requests
import re
import codecs
from bs4 import BeautifulSoup
from openpyxl import Workbook
wb = Workbook()
dest_filename = 'bt0.xlsx'
ws1 = wb.active
ws1.title = "第一页"

DOWNLOAD_URL = 'http://bt0.com'


def download_page(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data


def get_div(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    div = soup.find('div', class_='masonry__container')

    name = []  # 名字
    score = []  # 评分
    image = []  # 图片
    for i in div.find_all('div', attrs={'class': 'masonry__item col-md-3 col-sm-6 col-xs-6'}):
        detail = i.find(
            'figure', attrs={'class': 'effect-sadie'})
        movie_name = detail.img['alt']  # 电影名字
        img = detail.img['data-original']
        level_star = i.find(
            'span', attrs={'class': 'tag-sm tag-picture2'}).get_text()  # 评分
        name.append(movie_name)
        score.append(level_star)
        image.append(img)


    return name, score, image, None


def main():
    url = DOWNLOAD_URL
    mname = []
    mimg = []
    mscore = []

    while url:
        doc = download_page(url)
        name, score, img, url = get_div(doc)
        mname = mname + name
        mscore = mscore + score
        mimg = mimg + img

    for (i, m, o) in zip(mname, mscore, mimg):
        col_A = 'A%s' % (mname.index(i) + 1)
        col_B = 'B%s' % (mname.index(i) + 1)
        col_C = 'C%s' % (mname.index(i) + 1)
        ws1[col_A] = i
        ws1[col_B] = m
        ws1[col_C] = o

    wb.save(filename=dest_filename)


if __name__ == '__main__':
    main()
