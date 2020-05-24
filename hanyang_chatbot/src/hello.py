from flask import Flask
app = Flask(__name__)

@app.route("/")
def Index(): # 뷰 함수
    return '<h1>Hello Flask!</h1>'

# @app.route('/Flask/<name>')
# def index():
#     return '<h1>Hello, %s!</h1>' %name

if __name__ == '__main__':
    app.run()