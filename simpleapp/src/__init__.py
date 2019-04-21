from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__, static_url_path='/simpleapp/static')
api = Api(app)
CORS(app)  #P revents CORS errors


@app.route('/')
def welcome():
    return "Welcome"


@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)


class Users(Resource):
    def get(self):
        return {'Users': [{'id': 1, 'name': 'Keith'}, {'id': 2, 'name': 'James'}]}


api.add_resource(Users, '/users')  # Route_1


