from flask import Flask
app = Flask(__name__)
#程序是flask类的对象

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
#处理url和函数之间的关系

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s</h1>' % name


if __name__ == "__main__":
    app.run(debug=True)
