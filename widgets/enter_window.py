from PyQt5.QtWidgets import QLabel, QDialog, QPushButton, QLineEdit, QLabel, QFormLayout, QVBoxLayout, QHBoxLayout, QComboBox, QStatusBar
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from .main_window import MainWindow
from .table import TableModel, TableView
import paho.mqtt.client as mqtt
import requests
from ast import literal_eval

class My_entry(QDialog):
    addres_signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(My_entry, self).__init__(parent)
        self.setFixedSize(400,250)
        
        self.setWindowTitle('Home')
        my_icon = QIcon("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/rsp2.png")
        my_pix = QPixmap("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/rsp2.png")
        self.name_ = QLabel('PypiMotor')
        self.name_.setFont(QFont('Arial',30))
        self.setWindowIcon(my_icon)
        self.large_ICON = QLabel()
        self.large_ICON.setPixmap(my_pix)
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.add_addres = QLineEdit()
        self.add_bt = QPushButton('+')
        self.add_bt.clicked.connect(self.add_addres_)
        self.addres = QComboBox()
        self.addres.addItems(['mqtt.eclipse.org','iot.eclipse.org'])
        self.connection = QPushButton('conectar')
        self.status = QLabel('status: ')
        self.setObjectName('status')
        self.result = QLabel()
        self.result.setObjectName('result')
        self.connection.clicked.connect(self.mainwindow)
        self.vbox.addWidget(self.large_ICON, alignment=Qt.AlignHCenter)
        self.vbox.addWidget(self.name_, alignment=Qt.AlignHCenter)
        self.vbox.addStretch()
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox)
        self.hbox2.addWidget(self.add_addres)
        self.hbox2.addWidget(self.add_bt)
        self.hbox.addWidget(self.addres)
        self.hbox.addWidget(self.connection)
        self.forming = QFormLayout()
        self.forming.addRow(self.status, self.result)
        self.vbox.addLayout(self.forming)
        self.setLayout(self.vbox)
        
        self.flag = 0
        

        

    def mainwindow(self):

        self.wind = MainWindow()
        mm = My_client_register(self.addres.currentText(),1883,'zezin2')
        
        try:
            requests.get("https://"+self.addres.currentText())
            
        except:
            self.result.setText("Offline.")
            
        else:
            self.addres_signal.emit(self.addres.currentText())
            mm.start()
            self.wind.show()
            self.close()

    def add_addres_(self):
        self.addres.addItem(QIcon("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/net_icon.png"),self.add_addres.text())



class My_client_register(QThread):
    msg_signal = pyqtSignal(str)
    def __init__(self, broker, port, topic ,parent=None):
        super(My_client_register,self).__init__(parent)
        self.broker = broker
        self.port = port
        self.topic = topic

    
    def on_connect(self, client, userdata, flags, rc):
        print("[STATUS] Conectado ao Broker. Resultado de conexao: "+str(rc))

        client.subscribe(self.topic)
 
    
    def on_message(self, client, userdata, msg):
        pass
        

    def run(self):
        print("[STATUS] Inicializando MQTT...")
        #inicializa MQTT:
        client = mqtt.Client('1')
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        try:
            client.connect(self.broker, self.port)
        except:
            self.msg_signal.emit('Falha na conexão.')
            return True
        else:
            self.msg_signal.emit('Conexão feita com sucesso.')
            client.loop_forever()
