# coding utf-8
import requests
import json
from time import sleep
from pymongo import MongoClient
import re
import codecs
from bs4 import BeautifulSoup

# DOWNLOAD_URL = 'http://bt0.com'


def download_page(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data

mtime = 0
def get_div(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    # div = soup.find('span ', property="v:runtime")
    # time = str(div)
    # mtime = time
    print(soup.find('span', property="v:runtime"))
    time = soup.find('span', property="v:runtime").span
    print(time)
    # name = []  # 名字
    # score = []  # 评分
    # image = []  # 图片
    # for i in div.find_all('div', attrs={'class': 'masonry__item col-md-3 col-sm-6 col-xs-6'}):
    #     detail = i.find(
    #         'figure', attrs={'class': 'effect-sadie'})
    #     movie_name = detail.img['alt']  # 电影名字
    #     img = detail.img['data-original']
    #     level_star = i.find(
    #         'span', attrs={'class': 'tag-sm tag-picture2'}).get_text()  # 评分
    #     name.append(movie_name)
    #     score.append(level_star)
    #     image.append(img)


def qandi():

    client = MongoClient('127.0.0.1', 38897)
    db = client.movie_test
    collection = db.douban25

    # all = collection.find({})

    # idList = []
    # for item in all:
    #     print(item['id'])
    #     idList.append(item['id'])
    # for id in idList:
    #     url = 'https://movie.douban.com/subject/'+id
    #     get_div(download_page(url))

    get_div(download_page('https://movie.douban.com/subject/1764798'))
    

    # url = 'http://api.douban.com/v2/movie/top250'

    # r = requests.get(url, params={'start': 0, 'count': 25})
    # # print('processing %s' % r.url)
    # res = r.json()  # return dict
    # for movie in res['subjects']:
    #     collection.insert_one(movie)
    #     print(movie['title'], 'saved')
    # sleep(0.1)

    # collection.update_one({'id': '1292052'},
    #                       {'$push_all': {"extra": {
    #                           "durations": "132",
    #                           "languages": ['chinese'],
    #                       }
    #                       }}
    #                       )

# push 后面格式不对，按照现在的格式存的是extra[...,{},...],正常应该是extra{“”：“”}或者extra[。。。，。。。]
    # collection.update_one({'id': '1292052'},
    #                       {'$push': {"extra": {"lan": 'chine', "time": '123'}
    #                                  }}
    #                       )

if __name__ == '__main__':
    qandi()