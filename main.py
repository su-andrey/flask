from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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

class LoginForm(FlaskForm):
    surname = StringField('фамилия', validators=[DataRequired()])
    name = StringField('имя', validators=[DataRequired()])
    education = StringField('образование', validators=[DataRequired()])
    profession = StringField('Профессия', validators=[DataRequired()])
    sex = StringField('пол', validators=[DataRequired()])
    motivation = StringField('мотивация', validators=[DataRequired()])
    ready = BooleanField('Готов остаться', validators=[DataRequired()])
    submit = SubmitField('Отправить')


@app.route('/answer',  methods=['GET', 'POST'])
@app.route('/auto_answer',  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        param = {}
        param['title'] = 'Анкета'
        param['surname'] = form.surname.data
        param['name'] = form.name.data
        param['education'] = form.education.data
        param['profession'] = form.profession.data
        param['sex'] = form.sex.data
        param['motivation'] = form.motivation.data
        param['ready'] = form.ready.data
        return render_template('auto_answer.html', **param)
    return render_template('login.html', title='Аварийный доступ', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
