from flask import Flask
import datetime
from data import db_session
from data.jobs import Jobs

db_session.global_init("db/mars_explorer.db ")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_sess = db_session.create_session()
user = Jobs()
user.team_leader = 1
user.job = 'deployment of residential modules 1 and 2'
user.work_size = 15
user.collaborators = '2, 3'
user.start_date = datetime.datetime.now()
user.is_finished = False
db_sess.add(user)
db_sess.commit()
