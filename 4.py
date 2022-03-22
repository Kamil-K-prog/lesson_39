from flask import Flask
from data import db_session
from data.user import User
from data.job import Jobs

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

    first_job = Jobs()
    first_job.team_leader = 1
    first_job.job = 'deployment of residential modules 1 and 2'
    first_job.work_size = 15
    first_job.collaborators = '2, 3'
    first_job.is_finished = False

    session.add(first_job)
    session.commit()

    # app.run()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
