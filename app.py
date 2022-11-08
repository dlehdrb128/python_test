from flask import Flask
import db

app = Flask(__name__)  # Flask 객체 생성


 
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
 
if __name__ == "__main__":  # 모듈이 실행 됨을 알림
    app.run(debug=True, port=8080) 