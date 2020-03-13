import paho.mqtt.client as mqtt
from threading import Thread
import sqlite3
from ast import literal_eval



class My_client_receive(Thread):

    def __init__(self, broker, port, topic):
        Thread.__init__(self)
        self.broker = broker
        self.port = port
        self.topic = topic

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        #print("[MSG RECEBIDA] Topico: "+msg.topic+" / Mensagem: "+str(msg.payload))
        data = literal_eval(msg.payload.decode('utf-8'))
        print(data)
        print(type(data))
        try:
            connection = sqlite3.connect('motor.db')
            cursor = connection.cursor()
            query = "INSERT INTO motor VALUES (NULL,?,?,?,?,?,?,?)"
            cursor.execute(query,(data['tag'],data['potencia'],data['fp'],data['rotacao'],data['rendimento'],data['data'],data['ensaios']))
            connection.commit()
            connection.close()
        except:
            print("[STATUS] Error ao inserir no banco de dados")
        else:
            print("[MSG RECEBIDA] Topico: "+msg.topic+" / Armazenamento no banco de dados completo.")

    def run(self):
        print("[STATUS] Inicializando MQTT...")

        client = mqtt.Client('2')
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(self.broker, self.port)
        client.loop_forever()

if __name__ == "__main__":
    my = My_client_receive('mqtt.eclipse.org', 1883, 'joelho1')
    my.start()