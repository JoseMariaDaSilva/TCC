import paho.mqtt.client as mqtt
from threading import Thread
import sqlite3
from ast import literal_eval
from alter_table import delete_from_table



class My_client_alter(Thread):

    def __init__(self, broker, port, topic):
        Thread.__init__(self)
        self.broker = broker
        self.port = port
        self.topic = topic

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        print("[MSG RECEBIDA] Topico: "+msg.topic+" / Mensagem: "+str(msg.payload.decode('utf-8')))
        data = str(msg.payload.decode('utf-8'))
        
        if delete_from_table('motor.db', data):
            print("Deletado com sucesso!")
        else:
            print("Motor nao registrado")
        

    def run(self):
        print("[STATUS] Inicializando MQTT...")

        client = mqtt.Client('11')
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(self.broker, self.port)
        client.loop_forever()

if __name__ == "__main__":
    my = My_client_alter('mqtt.eclipse.org', 1883, 'alter')
    my.start()