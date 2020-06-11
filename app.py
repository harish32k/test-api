from flask import Flask,jsonify
from flask_restful import Api
from resources.emp import Emp, Dept, EmpLogin
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['JWT_SECRET_KEY']='coscskillup'
api = Api(app)

jwt=JWTManager(app)

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error': 'authorization_required',
        "description": "Request does not contain an access token."
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'invalid_token',
        'message': 'Signature verification failed.'
    }), 401

api.add_resource(Emp, '/emp')
api.add_resource(Dept, '/dept')
api.add_resource(EmpLogin,'/login')

@app.route('/')
def home():
    return("<h1 style='font-family: sans-serif;'>This is an API to interact with the EMP and DEPT tables</h1>.")

app.run(debug=True)
