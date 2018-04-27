from flask import Flask, url_for, request, render_template
from jinja2 import Template

#mongodb对象转json要用这个转
from bson.json_util import dumps
# import sys
# sys.path.append(r'/www/wwwroot/flaskweb/python')
# import movieapi
from py.upload import upload_image


app = Flask(__name__,static_folder='static', static_url_path='/static')

@app.route('/')
def hello_world(name=None):
     
    # template = Template('Hello {{ name }}!')
    #return template.render(name='John Doe')
    return render_template('index.html')


@app.route('/u', methods=['GET', 'POST'])
def u():
    print('post0000')
    if request.method =='GET':
        return render_template('upload.html')
    if request.method == 'POST':
        print('postttttt')
        file = request.files['file']            # 获取文件信息用 request.FILES.get
                                         # 这里的get('file') 相当于 name = file
        upload_image(file)
        # print(file) 可以直接显示文件名，是因为django FILES内部 重写了 __repr__ 方法 
        # if file:                                      # 如果文件存在
        #     with open(file.name,'wb') as f:               #  新建1张图片 ，图片名称为 上传的文件名
        #         for temp in file.chunks():                #  往图片添加图片信息
        #             f.write(temp)
        return 'ok'
    


@app.route('/up', methods=['GET', 'POST'])
def get():
    file = request.files['file']
    
    # s = up(file)
    return s

@app.route('/hello')
def hello(name=None):
    name = 'wangzz'
    return render_template('ins.html', name=name)

@app.route('/s')
@app.route('/s/<name>')
def s(name=None):
    return render_template('baidu.html', name=name)

@app.route('/user/<username>')
def user(username):
    #return 'user= %s' % username
        
    return 'user = '+username



from pymongo import MongoClient

def getValues():

    client = MongoClient('localhost', 38897)
    db = client.movie_test
    collection = db.douban25
    all = collection.find( { } )
    return all

@app.route('/api/top250')
def top250():
    alls = getValues()
    return dumps(alls)
    # return str(all)+"111"


@app.route('/api/ins20')
def ins20():
    client = MongoClient('localhost', 38897)
    db = client.instagram
    collection = db.mylike.collection
    data = collection.find_one()
    onedata = data['data']

    return dumps(onedata)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)