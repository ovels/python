# -*- coding: utf-8 -*-

from sevencow import Cow
from sevencow import CowException

import s_data
# 需要填写你的 Access Key 和 Secret Key
access_key = s_data.AccessKey
secret_key = s_data.SecretKey


def up(data):
    cow = Cow(access_key, secret_key)
    b = cow.get_bucket('ovels')
    filename = ''
    info = ''
    try:
        b.put(filename, data=data, keep_name=False, override=True)
    except CowException as e:
        print(e.url)         # 出错的url
        print(e.status_code) # 返回码
        print(e.content)     # api 错误的原因
        info = 'url='+e.url+'   status_code'+e.status_code+'  content'+e.content
        return info
    qnurl = b.stat(filename)
    return qnurl
