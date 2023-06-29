import pandas as pd
from flask import Flask, render_template, request, redirect
from preprocess_user import normalize_user_feature_vector, decode_levels, make_user_feature_vector

from sklearn.metrics import classification_report
from knn_model import knn_get_level
app = Flask(__name__)


github_token = ""
github_name = ""


@app.route('/', methods=['GET', 'POST'])
def index():
    # Домашняя страница
    global github_name, github_token
    if request.method == 'POST':
        for key in request.form:
            print(request.form[key])
            if request.form[key] == '':
                return render_template('index.html', error='Все поля должны быть заполнены!')
        github_name = request.form['github_name']
        github_token = request.form['github_token']
        return render_template('loading.html')
    return render_template('index.html')


@app.route('/get_result')
def get_result():
    global level, github_name, github_token

    developer = make_user_feature_vector(
        github_name, github_token=github_token)

    # normalize every feature column
    developer = normalize_user_feature_vector(developer)
    level = knn_get_level(developer, 3)
    level = decode_levels(level)

    level = knn_get_level(github_name=github_name, k=3)
    return level


@app.route('/result')
def result():
    global level
    return render_template('result.html', level=level)


if __name__ == "__main__":
    app.run()
