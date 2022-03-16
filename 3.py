from flask import Flask
from data import db_session
from data.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app


@app.route('/index')
@app.route('/')
def index():
    return f'E'


def main():
    db_session.global_init('data/db/mars_explorer.sqlite')
    session = db_session.create_session()

    captain = User()
    captain.surname = 'Scott'
    captain.name = 'Ridley'
    captain.age = 21
    captain.position = 'captain'
    captain.speciality = 'research engineer'
    captain.address = 'module_1'
    captain.email = 'scott_chief@mars.org'

    staff_1 = User()
    staff_1.surname = 'Ivanov'
    staff_1.name = 'Peter'
    staff_1.age = 22
    staff_1.position = 'crew'
    staff_1.speciality = 'madic'
    staff_1.address = 'medical_module'
    staff_1.email = 'ivanovpetr243@gmail.com'

    staff_2 = User()
    staff_2.surname = 'Jorno'
    staff_2.name = 'John'
    staff_2.age = 20
    staff_2.position = 'crew'
    staff_2.speciality = 'biotechnik'
    staff_2.address = 'farmer_module'
    staff_2.email = 'johnjorn43@mars.org'
    
    staff_3 = User()
    staff_3.surname = 'Gratiano'
    staff_3.name = 'Amberson'
    staff_3.age = 30
    staff_3.position = 'crew'
    staff_3.speciality = 'engineer'
    staff_3.address = 'engineer_module'
    staff_3.email = 'crazyengineer@mars.org'

    session.add(captain)
    session.add(staff_1)
    session.add(staff_2)
    session.add(staff_3)
    session.commit()

    # app.run()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
