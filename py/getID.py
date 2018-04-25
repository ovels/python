# coding utf-8
import requests
import json
from time import sleep
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 38897)
db = client.movie_test
collection = db.douban25


all = collection.find()
idList = []
for item in all:
    print(item['id'])
    idList.append(item['id'])




for id in idList:

    url = 'http://api.douban.com/v2/movie/subject/'+id
    t = 1
    r = requests.get(url)
    # print('processing %s' % r.url)
    res = r.json()  # return dict
    collection.update_one({'id': id},
                      {'$set': {'genres': res}}
                      )
    sleep(0.1)

# collection.update_one({'subtype': 'aka'},
#                       {'$set': {'subtype': 'movie'}}
#                       )
