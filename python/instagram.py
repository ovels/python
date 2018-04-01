# coding utf-8
import requests
import json
from time import sleep
import s_data

from pymongo import MongoClient

BASE_URL = 'https://api.instagram.com/v1/users/self/media/liked?access_token='

MAX_LIKE_ID = '&max_like_id='


def conn_db():
    client = MongoClient('127.0.0.1', 38897)
    db = client.instagram
    collection = db.mylike
    return collection


 # 就是获取一条url所携带的数据
def get_data_from_ins():
    url = BASE_URL+s_data.TOKEN
    data = get(url)
    code = data['meta']['code']
    if(code is not 200):
        s_data.send_message('api获取数据失败，error code='+code)
        print('失败')
        return
    max_id = data['pagination']['next_max_like_id']
    next_url = data['pagination']['next_url']
    print(code)
    print(max_id)
    print(next_url)
    conn_db().collection.insert_one(data)

    get_max_like(next_url)

'''https://api.instagram.com/v1/users/self/media/liked?access_token=&max_like_id=1610100422982514638'''


def get_max_like(next):

    data = get(next)
    try:
        id = data['pagination']['next_url']
    except:
        print('id为空了，获取完了')
        s_data.send_message('id为空了，获取完了')
    conn_db().collection.insert_one(data)

    sleep(1)
    get_max_like(id)
    s_data.send_message('get all data')


def get(url):
    r = requests.get(url)
    res = r.json()  # return dict
    return res

if __name__ == "__main__":
    get_data_from_ins()