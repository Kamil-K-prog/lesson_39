from flask import Flask, render_template, redirect
from data import db_session
from data.user import User
from data.job import Jobs
from forms.register_form import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/index')
@app.route('/')
def index():
    res = []
    session = db_session.create_session()
    list_profession = session.query(Jobs).all()
    for i in list_profession:
        res.append([i.id, i.team_leader, i.job, i.work_size, i.collaborators, i.start_date, i.end_date, i.is_finished])
    return render_template('5.html', title='Работы', lst_prf=res)


@app.route('/register', methods=['GET', 'POST'])
def register():
    global User
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('hw6.html', title='Регистрация',
                                   form=form,
                                   message='Пароли не совпадают!')
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.login.data).first():
            return render_template('hw6.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть!")
        user = User(surname=form.surname.data,
                    name=form.name.data,
                    age=form.age.data,
                    position=form.position.data,
                    speciality=form.speciality.data,
                    address=form.address.data,
                    email=form.login.data,
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/')
    return render_template('hw6.html', title='Регистрация', form=form)


def main():
    db_session.global_init('data/db/mars_explorer.sqlite')
    app.run()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
