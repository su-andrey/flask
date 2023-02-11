from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def start():
    return 'Nothing to show here, choose another url'


@app.route('/index/<name>')
def name(name):
    return render_template('index.html', title=name)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        return render_template('training.html', name='tex.png')
    else:
        return render_template('training.html', name='science.png')


@app.route('/list_prof/<param>')
def list_prof(param):
    professions = ['штурман', 'пилот', 'экзобиолог', 'инженер - исследователь', 'строитель', 'врач', 'пилот дронов']
    if param == 'ol':
        return render_template('list_prof.html', profs=professions, type=param)
    elif param == 'ul':
        return render_template('list_prof.html', profs=professions, type=param)
    else:
        return 'Bad param. Use ul/ol'


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {}
    param['title'] = 'Анкета'
    param['surname'] = 'Watny'
    param['name'] = 'Mark'
    param['education'] = 'выше среднего'
    param['profession'] = 'штурман марсохода'
    param['sex'] = 'male'
    param['motivation'] = 'Всегда мечтал застрять на Марсе!'
    param['ready'] = 'True'
    return render_template('auto_answer.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
