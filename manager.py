from flask import Flask, url_for, request, render_template
from jinja2 import Template

#mongodb对象转json要用这个转
from bson.json_util import dumps
# import sys
# sys.path.append(r'/www/wwwroot/flaskweb/python')
# import movieapi


app = Flask(__name__,static_folder='static', static_url_path='/static')

@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    # template = Template('Hello {{ name }}!')
    #return template.render(name='John Doe')
    return render_template('index.html')

@app.route('/bt')
def bt():
    return render_template('bt/Documentation/index.html')

@app.route('/hello')
def hello(name=None):
    name = 'wangzz'
    return render_template('index.html', name=name)

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

@app.route('/get', methods=['GET', 'POST'])
def get():
    if request.method == 'POST':
        return 'post'
    else :
        return 'get111'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)