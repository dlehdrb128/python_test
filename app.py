from flask import Flask, jsonify
from db import config
from routes import main

 
app = Flask(__name__)  # Flask 객체 생성


app.register_blueprint(main.main, url_prefix='/main')


@app.route('/')
def free():
    db_class = config.Database()
    sql      = "SELECT * FROM kospi_005930_d WHERE day BETWEEN '2000-10-05' AND '2000-10-20';"
    row      = db_class.executeAll(sql)

    return jsonify(row)

@app.route('/profile/<username>') #/profile/ 경로에 뒤에 입력한 문자열대로 페이지가 동적 접속.
def get_profile(username):
    data = {"profile" : username}
    return jsonify(data)


if __name__ == "__main__":  # 모듈이 실행 됨을 알림
    app.run(debug=True, port=8080) 
   
    

