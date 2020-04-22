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


@app.route('/list_prof/<list>')
def list_prof(list):
    professions = ['Аудитор',
                   'Актуарий',
                   'Аналитик',
                   'Банкир',
                   'Брокер',
                   'Бухгалтер',
                   'Дилер',
                   'Продавец',
                   'Инкассатор',
                   'Коммерческий директор',
                   'Кредитный консультант',
                   'Маркетолог',
                   'Маклер биржевой',
                   'Менеджер по работе с клиентами',
                   'Налоговый инспектор',
                   'Операционист',
                   'Предприниматель',
                   'Сметчик',
                   'Снабженец',
                   'Страховой агент',
                   'Релайтер',
                   'Товаровед',
                   'Торговый представитель',
                   'Тренд-вотчер',
                   'Трейдер',
                   'Экономист',
                   'Экспедитор',
                   'Финансист',
                   'Кассир']
    return render_template('list_prof.html', professions=professions, type_list=list)

if __name__ == '__main__':
    app.run(port=80, host='127.0.0.1')
