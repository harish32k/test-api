from flask import Flask,jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.emp import Emp
from resources.emp import EmpLogin

app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS']=True
app.config['JWT_SECRET_KEY'] = 'coscskillup'

api = Api(app)
api.add_resource(Emp, '/emp')
api.add_resource(EmpLogin, '/login')
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

@app.route('/')
def home():
    return(f"""<h1 style="font-family: 'Palatino Linotype';">This is an API to interact with the EMP table</h1>
                <p style="font-size:2em">Developed by Harish Akula</p>""")

if __name__ == '__main__':
    app.run(debug=True)
