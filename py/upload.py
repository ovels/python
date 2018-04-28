# # -*- coding: utf-8 -*-
from py.s_data import AccessKey, SecretKey
from py.s_data import send_message as send
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import hashlib


#需要填写你的 Access Key 和 Secret Key
access_key = AccessKey
secret_key = SecretKey

def upload_image(data,filename):
    
    #构建鉴权对象
    q = Auth(access_key, secret_key)
    #要上传的空间
    bucket_name = 'ovels'
    #上传到七牛后保存的文件名
    # upload_name = hashlib.md5(data).hexdigest()
    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, filename, 3600)
    print('uploood')
    if not data:
        with open(filename,'rb') as f:
            data = f.read()


    #要上传文件的本地路径
    localfile = './files/'+filename
    ret, info = put_file(token, filename, localfile)
    # send('info = '+str(info))
    print('info = '+str(info))
    assert ret['key'] == filename
    assert ret['hash'] == etag(localfile)
    return 'info = '+str(info)