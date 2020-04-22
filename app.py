@app.route('/index')
def index(title=''):
    params = {'title': title}
    return render_template('base.html', **params)


@app.route('/training/<prof>')
def training(prof):
    params = {'prof': prof, 'title': 'Тренинг'}
    return render_template('training.html', **params)
