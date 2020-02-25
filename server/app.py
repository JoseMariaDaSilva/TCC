from flask import Flask, jsonify
from flask_restful import Api
from resources.motor_register import MotorRegister, MotorsList

app = Flask(__name__)
api = Api(app)


@app.route('/test',methods=['GET'])
def index():
    return jsonify({"message":"server: on",
                    "status":"status: 200",
                    "testes":"testes: completed!"})

api.add_resource(MotorRegister,'/register')
api.add_resource(MotorsList,'/list')

if __name__ == "__main__":
    app.run(port=5000, debug=True)