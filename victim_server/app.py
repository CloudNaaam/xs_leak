from flask import Flask, request, render_template, make_response, redirect, url_for, session
import os
import time
import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='cloud',
                             password='cloud',
                             database='board_db',
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__)
app.secret_key = os.urandom(32)

user_info = {
    "cloud": "cloud"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        for un,pw in user_info.items():
            if username == un:
                if password == pw:
                    session['username'] = username
                    session['password'] = password

                    return redirect('/')
        return "<script>alert('땡!')</script>"

@app.route('/save', methods=['GET','POST'])
def save():
    if request.method == 'GET':
        return render_template('save.html')
    else:
        post = request.form.get("post","")
        
        with connection.cursor() as cursor:
            sql = "INSERT INTO board (`post`, `secret`) VALUES (%s, 0)"
            cursor.execute(sql, (post,))
        connection.commit()

        return render_template('save.html', result="Saved!")

@app.route('/iframe', methods=['GET'])
def search_iframe():
    query = request.args.get("query","")
    print(query)
    with connection.cursor() as cursor:
        sql = "SELECT * FROM board WHERE post LIKE %s;"
        params = (f'{query}%',)
        cursor.execute(sql, params)
        row = cursor.fetchall()
    
    result = row[0] # 첫 번째 결과만
    # print(result)
    # print(result['secret'])
    if result['secret'] == 1:
        result['post'] = "this is flag lololololol"

    return render_template('iframe.html', result=result)

@app.route('/timing', methods=['GET'])
def search_timing():
    query = request.args.get("query","")
    with connection.cursor() as cursor:
        sql = "SELECT * FROM board WHERE post LIKE %s;"
        params = (f'{query}%',)
        cursor.execute(sql, params)
        row = cursor.fetchall()
    
    if row:
        time.sleep(2)
    
    result = '검색 완료^^'

    return render_template('timing.html', result=result)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
