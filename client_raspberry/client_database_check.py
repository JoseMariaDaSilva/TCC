import threading
import paho.mqtt.client as mqtt

import sqlite3
from ast import literal_eval

def on_connect(client, userdata, rc):
    if rc != 0:
        print("Habilite a conexão com o Broker...")
    else:
        print("Conectado com o Broker: ")

def on_publish(client, userdata, mid):
	pass
		
def on_disconnect(client, userdata, rc):
	if rc !=0:
	    pass
		
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect('mqtt.eclipse.org', 1883)

def publish(topic, message):
    mqttc.publish(topic,message)

def senderLoop():
    threading.Timer(3.0, senderLoop).start()
    connection = sqlite3.connect('motor.db')
    cursor = connection.cursor()
    query = "SELECT * FROM motor"
    result = cursor.execute(query)
    rows = result.fetchall()
    connection.close()

    publish('zezin3', str(rows))

if __name__ == "__main__":
    senderLoop()

