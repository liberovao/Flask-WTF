from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    astronauts = ['Ридли Скотт', 'Алиша Матинс', 'Марк Уолкер',
                  'Вендетта Мисс', 'Тедди Шон', 'Гоша Артимонов']
    return render_template('distribution.html', astronauts=astronauts)


if __name__ == '__main__':
    app.run(port=80, host='127.0.0.1')
