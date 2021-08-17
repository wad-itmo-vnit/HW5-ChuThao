from flask import Flask, render_template, request, redirect, make_response
from functools import wraps

app = Flask(__name__)

auth_token = "chuphuongthao"

def generate_token(user, pw):
    return "chuphuongthao"

@app.route('/')
def home():
    return redirect('/login')

@app.route('/img/get/<number>')
def sever_img(number):
    file_name = './static/pics/' + number + '.jpg'
    return send_file(file_name)

def auth(request):
    global auth_token
    token = request.cookies.get('login-info')
    return (token == auth_token)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user=request.form.get('user')
        pw=request.form.get('password')
        if (user == 'chupu' and pw == '04121999'):
            token = generate_token(user,pw)
            resp = make_response(redirect('/gallery'))
            resp.set_cookie('login-info', token)
            return resp
        else:
            return redirect('/login'), 403

@app.route('/gallery')
def gallery():
    if auth(request):
        return render_template('index.html')
    else:
        return redirect('/')


app.run(host="localhost", port=5000)