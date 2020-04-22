from flask import flask, url_for, request, render_template
import json

app = Flask(__name__)

@app.route('/index')
def index(title=''):
    params = {'title': title}
    return render_template('base.html', **params)


@app.route('/training/<prof>')
def training(prof):
    params = {'prof': prof, 'title': 'Тренинг'}
    return render_template('training.html', **params)

if __name__ == '__main__':
    app.run(port=80, host='127.0.0.1')
