@app.route('/index')
def index(title=''):
    params = {'title': title}
    return render_template('base.html', **params)
