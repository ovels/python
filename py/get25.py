# coding utf-8
import requests
import json
from time import sleep
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 38897)
db = client.movie_test
collection = db.douban25

url = 'http://api.douban.com/v2/movie/top250'

r = requests.get(url, params={'start': 0, 'count': 25})
# print('processing %s' % r.url)
res = r.json()  # return dict
for movie in res['subjects']:
    collection.insert_one(movie)
    print(movie['title'], 'saved')
sleep(0.1)

