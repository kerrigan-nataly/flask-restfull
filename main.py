from flask import Flask
from flask_restful import Api
from data import db_session, users_resource
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)

api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')


def prep_db(session):
    cap = User()
    cap.surname = "Scott"
    cap.name = "Ridley"
    cap.age = 21
    cap.position = "captain"
    cap.speciality = "research engineer"
    cap.address = "module_1"
    cap.email = "cap@mars.org"
    cap.city_from = "Саут-Шилдс"
    cap.set_password('test')

    nav = User()
    nav.surname = "Watny"
    nav.name = "Mark"
    nav.age = 25
    nav.position = "rover navigator"
    nav.speciality = "navigator"
    nav.address = "module_2"
    nav.city_from = "Москва"
    nav.email = "mark_wanty@mars.org"

    session.add(cap)
    session.add(nav)

    session.commit()

def main():
    db_session.global_init("db/blogs.sqlite")
    session = db_session.create_session()
    users = session.query(User).all()
    if not users:
        prep_db(session)
    app.run()


if __name__ == '__main__':
    main()