from flask import Flask, render_template, request
from preprocess_user import normalize_user_feature_vector, decode_levels, make_user_feature_vector

from sklearn.metrics import classification_report
from knn_model import knn_get_level
app = Flask(__name__)

github_token = ""
github_name = ""


@app.route('/', methods=['GET', 'POST'])
def index():
    # Домашняя страница
    if request.method == 'POST':
        for key in request.form:
            print(request.form[key])
            if request.form[key] == '':
                return render_template('index.html', error='Все поля должны быть заполнены!')
        return render_template('loading.html')
    return render_template('index.html')


@app.route('/loading')
def loading():
    '''
    developer = make_user_feature_vector(github_name)
    # normalize every feature column
    developer = normalize_user_feature_vector(developer)
    level = knn_get_level(developer, 3)
    level = decode_levels(level)
    '''
    level = knn_get_level("test", 3)
    return render_template('result.html', level = level)

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run()
