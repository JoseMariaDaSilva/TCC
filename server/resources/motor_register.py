from flask_restful import Resource, reqparse
from flask import Flask, request, jsonify
from models.motor_model import MotorModel
from resources.runner import run
import RPi.GPIO as GPIO
import threading
from queue import Queue
from time import sleep
import sqlite3


class MotorRegister(Resource):
    parse = reqparse.RequestParser()

    parse.add_argument("tag",
                type = str,
                required=True,
                help="Este Campo nao pode estar vazio"
                )

    parse.add_argument("potencia",
                type = int,
                required=True,
                help="Este Campo nao pode estar vazio"
                )
            
    parse.add_argument("fp",
                type = float,
                required=True,
                help="Este Campo nao pode estar vazio"
                )

    parse.add_argument("rotacao",
                type = int,
                required=False,
                help="Este Campo nao pode estar vazio"
                )

    parse.add_argument("rendimento",
                type = float,
                required=True,
                help="Este Campo nao pode estar vazio"
                )

    parse.add_argument("data",
                type = str,
                required=True,
                help="Auto seleciona"
                )

    parse.add_argument("ensaios",
                type = int,
                required=True,
                help="Auto seleciona"
                )
    

    def post(self):
        data = self.parse.parse_args()
        print(data['tag'])
        connection = sqlite3.connect('motor.db')
        cursor = connection.cursor()
        print(data['tag'])
        if MotorModel.find_by_tag(data['tag']):
            return {"message":"motor com esta tag ja esta cadastrado!"},400

        query = "INSERT INTO motor VALUES (NULL,?,?,?,?,?,?,?)"
        cursor.execute(query,(data['tag'],data['potencia'],data['fp'],data['rotacao'],data['rendimento'],data['data'],data['ensaios']))
        connection.commit()
        connection.close()
        return {"message":"Motor created sucessfully"}

class MotorsList(Resource):

    def get(self):
        connection = sqlite3.connect('motor.db')
        cursor = connection.cursor()
        query = "SELECT * FROM motor"
        result = cursor.execute(query)
        row = result.fetchall()
        connection.close()
        return {"motors":row}

    
class MotorManager(Resource):

    def delete(self, name):
        motor = MotorModel.find_by_tag(name)
        if motor:
            motor.delete_from_db()

        return {"message":"motor deletado"}

class Capture(Resource):
    myq = Queue()
    t = threading.Thread(target=run, args=(myq,))

    def get(self,name):
        if name == 'off':
            try:
                self.t.do_run = False
                self.t.join()
                data = self.myq.get() 
                return {"message":data}
            except:
                return {"message":"operação invalida"}

        if name == 'on':
            try:
                self.t.start()
                return {"message":"Leitura de dados iniciada"}
            except:
                self.t.do_run = False
                self.t.join()
                return {"message":"operação invalida"}
        else:
            return {"message":"comando inexistente"}
    


    
        



        
