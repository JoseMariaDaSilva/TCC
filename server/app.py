from flask import Flask, jsonify
from flask_restful import Api
from resources.motor_register import MotorRegister, MotorsList, MotorManager, Capture

app = Flask(__name__)
api = Api(app)


@app.route('/test',methods=['GET'])
def index():
    return jsonify({"message":"server: on",
                    "status":"status: 200",
                    "testes":"testes: completed!"})

api.add_resource(MotorRegister,'/register')
api.add_resource(MotorsList,'/list')
api.add_resource(MotorManager,'/motor/<string:name>')
api.add_resource(Capture,'/capture/<string:name>')

if __name__ == "__main__":
    app.run(port=5000, debug=True)