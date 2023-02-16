from flask import Flask

from data import db_session
from data.users import User

db_session.global_init("db/mars_explorer.db ")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_sess = db_session.create_session()
info = [['Ridley', 'Scott', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org', 'cap'],
        ['Derek', 'Scott', 27, 'mechanic', 'mechanic', 'module_3', 'd.scott@mars.org', 'mech'],
        ['Lewis', 'Johnson', 58, 'doctor', 'medecine', 'module_2', 'doc_lewis@mars.org', 'doc'],
        ['Mark', 'Andreas', 34, 'scientist', 'biology', 'module_1', 'mr.anreas@mars.org', 'mab']]
for elem in info:
    user = User()
    user.surname = elem[1]
    user.name = elem[0]
    user.age = elem[2]
    user.position = elem[3]
    user.speciality = elem[4]
    user.address = elem[5]
    user.email = elem[-2]
    user.hashed_password = elem[-1]
    db_sess.add(user)
db_sess.commit()
