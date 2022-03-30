from flask import Flask, render_template
from data import db_session
from data.user import User
from data.job import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/index')
@app.route('/')
def index():
    res = []
    session = db_session.create_session()
    list_profession = session.query(Jobs).all()
    for i in list_profession:
        res.append(str(i).split('//'))
    return render_template('5.html', title='Работы', lst_prf=res)


def main():
    db_session.global_init('data/db/mars_explorer.sqlite')
    app.run()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
