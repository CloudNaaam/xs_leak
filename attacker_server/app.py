from flask import Flask, request, render_template, make_response, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

flag = 'CLOUD{'

# 구한 flag 출력
@app.route('/')
def index():
    global flag
    param = request.arg.get("flag","")

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
    return render_template('frame_count.html')

# timing 기반
@app.route('/timing')
def timing():
    global flag
    return render_template('timing.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
