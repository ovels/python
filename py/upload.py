# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu.utils import etag, urlsafe_base64_encode
from qiniu.auth import Auth
from .services.storage.uploader import put_file
import qiniu.config

import s_data
# 需要填写你的 Access Key 和 Secret Key
access_key = s_data.AccessKey
secret_key = s_data.SecretKey
# 构建鉴权对象
q = Auth(access_key, secret_key)
# 要上传的空间
bucket_name = 'ovels'
# 上传到七牛后保存的文件名
# 获取原文件名
key = 'my-python-logo.png'

# 生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)

# 要上传文件的本地路径
localfile = './sync/bbb.jpg'
ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)

def get_upload_token():
    return token
