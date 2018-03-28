from flask import Flask, url_for, request, render_template
from jinja2 import Template

app = Flask(__name__,static_folder='static', static_url_path='/static')

@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    template = Template('Hello {{ name }}!')
    #return template.render(name='John Doe')
    return render_template('index.html')

@app.route('/bt')
def bt():
    return render_template('bt/Documentation/index.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/s')
@app.route('/s/<name>')
def s(name=None):
    return render_template('baidu.html', name=name)

@app.route('/user/<username>')
def user(username):
    #return 'user= %s' % username
    
    '''vs sync''' 
    return 'user = '+username

@app.route('/get', methods=['GET', 'POST'])
def get():
    if request.method == 'POST':
        return 'post'
    else :
        return 'get'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)