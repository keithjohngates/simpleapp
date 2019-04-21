#from flask import Flask
#app = Flask(__name__)
#


from flask import Flask, request, render_template, url_for
from flask_restful import Resource, Api

app = Flask(__name__, static_url_path='/var/flaskapp/simpleapp/static')
api = Api(app)

@app.route('/')
def hello_world():
	return "Welcome"

@app.route('/map')
def get(self):
	return render_template(url_for("static", filename="map.html"))

class Users(Resource):
    def get(self):
        return {'Users': [{'id':1, 'name':'Keith'},{'id':2, 'name':'James'}]} 


api.add_resource(Users, '/users') # Route_1


