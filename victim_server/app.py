from flask import Flask, request, render_template, make_response, redirect, url_for, session
import os
import time
import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='user',
                             password='',
                             database='db',
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__)
app.secret_key = os.urandom(32)

user_info = {
    "cloud": "cloud"
}

@app.route('/')
def index():
    return render_template('index.html')
# index.html 에 각 라우트로 가는 버튼 있어야 함


@app.route('login', ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        for un,pw in user_info.item:
            if username == un:
                if password == pw:
                    session['username'] = username
                    session['password'] = password

                    return redirect('/')
        return "<script>alert('땡!')</script>"


@app.route('/iframe', ['GET','POST'])
def search_iframe():
    if request.method == 'GET':
        return render_template('iframe.html')
    else:
        query = request.form.get("query","")

        with connection.cursor() as cursor:
            sql = "SELECT * FROM board WHERE post LIKE '%s';"
            params = (f'%{query}%',)
            cursor.execute(sql, params)
            row = cursor.fetchone()

        result = row[0] # 첫 번째 결과만
        if result[2] == 1:
            result[1] = "this is flag lololololol"

        return render_template('index.html', result)

@app.route('/timing', ['GET','POST'])
def search_timing():
    if request.method == 'GET':
        return render_template('timing.html')
    else:
        query = request.form.get("query","")

        with connection.cursor() as cursor:
            sql = "SELECT * FROM board WHERE post LIKE '%s';"
            params = (f'%{query}%',)
            cursor.execute(sql, params)
            row = cursor.fetchone()

        # time.sleep(2) # 이건 최후의 수단

        return render_template('timing.html', '검색 완료^^')
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
