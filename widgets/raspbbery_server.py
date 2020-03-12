from PyQt5.QtWidgets import (QGroupBox, QHBoxLayout, QFormLayout, QPushButton, QLineEdit, QLabel, QWidget, 
                             QVBoxLayout, QTextEdit)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QThread
import paho.mqtt.client as mqtt
import requests
import json




class raspGp(QGroupBox):
    
    mark_signal = pyqtSignal(bool)
    def __init__(self, parent = None):
        super(QGroupBox, self).__init__(parent)

        self.mark = False
        self.setFixedSize(250,271)
        self.form = QFormLayout()
        
        self.apply = QPushButton("test_refresh")
        self.ping = QPushButton("conectar")
        self.ping.clicked.connect(self.ping_)

        self.addres = QLineEdit('mqtt.eclipse.org')
        self.addres.setReadOnly(True)
        

        self.label1 = QLabel("endereço:")

        self.textOutput = QTextEdit()
        self.textOutput.setReadOnly(True)
    
    #==== only icon =========================================================================
        self.icon = QPixmap("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/rsp2.png")
        self.lbl = QLabel()
        self.lbl.setPixmap(self.icon)
    #========================================================================================
        self.vbox = QVBoxLayout()
        

    
    def rasp(self):
        self.vbox.addWidget(self.lbl,alignment=Qt.AlignCenter)
        self.form.addRow(self.label1 ,self.addres)
        self.form.addRow(self.ping, self.apply)
        self.vbox.addLayout(self.form)
        self.vbox.addWidget(self.textOutput)
        self.setLayout(self.vbox)
        return self


    def ping_(self):

        try:
            mm = My_client_register(self.addres.text(), 1883, 'zezinho', parent=self)
            mm.start()
            self.mark_signal.emit(True)
            self.textOutput.append("[STATUS] Inicializando MQTT...")
            self.textOutput.append("[STATUS] Conectado ao Broker: {}".format(self.addres.text()))

        except:
            self.textOutput.append("[STATUS] Error ao se conectar com o endereços.")
            self.textOutput.append("[STATUS] Endereço se encontra inativo ou não existe.")
            self.textOutput.append("[STATUS] Verifique sua conexão.")
            
class My_client_register(QThread):
    signal_register = pyqtSignal(list)
    def __init__(self, broker, port, topic ,parent=None):
        super(My_client_register,self).__init__(parent)
        self.broker = broker
        self.port = port
        self.topic = topic

    
    def on_connect(self, client, userdata, flags, rc):
        print("[STATUS] Conectado ao Broker. Resultado de conexao: "+str(rc))

        client.subscribe(self.topic)
 
    
    def on_message(self, client, userdata, msg):
        print("[MSG RECEBIDA] Topico: "+msg.topic+" / Mensagem: "+str(msg.payload))

    def run(self):
        print("[STATUS] Inicializando MQTT...")
        #inicializa MQTT:
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(self.broker, self.port)
        client.loop_forever()
            
            


    