import os
from flask import Flask, render_template, redirect, abort, url_for, request
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_required, \
    login_user, current_user, logout_user
import datetime


app = Flask(__name__)


correct = ['2', '3', '1', '3', '2', '2', '2', '3', '1', '2', '1', '1', '2', '1', '2', '1', '2']


@app.route('/')
@app.route('/index')
def index():
    return render_template('main-temp.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    k = 0
    if request.method == 'GET':
        return render_template('questions.html')
    elif request.method == 'POST':
        for i in range(1, 18):
            if request.form[f"v{i}"] == correct[i - 1]:
                k += 1
        return redirect(f'/check_answers/{k}')


@app.route('/check_answers/<int:correct_ans>')
def check_answers(correct_ans):
    c = correct_ans
    if c == 17:
        zv = 'ЭКСПЕРТ'
    elif 13 <= c <= 16:
        zv = "Историк"
    elif 7 <= c <= 13:
        zv = 'Ученик'
    else:
        zv = 'Чайник'
    return render_template('check_answers.html', zv=zv, c=c)


def main():

    app.run(host="127.0.0.1", port=5000)


if __name__ == '__main__':
    main()
