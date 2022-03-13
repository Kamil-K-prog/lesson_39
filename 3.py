from flask import Flask
from data import db_session
from data.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('data/db/mars_explorer.sqlite')
    sess = db_session.create_session()

    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'

    sess.add(user)
    sess.commit()

    app.run()

if __name__ == '__main__':
    main()