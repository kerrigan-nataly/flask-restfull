from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, nullable=False)
parser.add_argument('about', required=True, nullable=False)
parser.add_argument('email', required=True, nullable=False, trim=True)
parser.add_argument('password', required=True)
