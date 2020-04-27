from flask import Flask, render_template

app = Flask(__name__)


@app.route('/table_param/<sex>/<int:age>')
def table_param(sex, age):
    return render_template('table.html', sex=sex, age=age)


if __name__ == '__main__':
    app.run(port=80, host='127.0.0.1')
