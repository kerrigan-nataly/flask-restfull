from flask import jsonify
from flask_restful import Resource, abort

from data import db_session
from data.users import User
from data.users_parser import parser


def abort_if_not_found(user_id):
    session = db_session.create_session()
    users = session.query(User).get(user_id)
    if not users:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('id', 'name', 'email', 'about', 'created_date'))})

    def delete(self, user_id):
        abort_if_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'name', 'about', 'email', 'created_date')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        check = session.query(User).filter(User.email == args['email']).first()
        if check:
            abort(403, message=f'User already exists')
        user = User(
            name=args['name'],
            about=args['about'],
            email=args['email']
        )
        user.set_password(args['password'])
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK', 'user_id': user.id})
