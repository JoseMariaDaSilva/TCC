from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QFormLayout, QWidget, QVBoxLayout, QSpinBox, QPushButton, QLabel, QLineEdit, QTabWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QIntValidator, QDoubleValidator, QIcon
from PyQt5.QtCore import Qt, pyqtSignal
from .plot import Plotting
from tools.tests_ea_tag import make_dir_a_tag
import requests
import json
import datetime








class Run(QGroupBox):

    message = pyqtSignal(str)
    dataSignal = pyqtSignal(bool)

    def __init__(self, parent = None):
        super(QGroupBox, self).__init__(parent)
        self.setFixedSize(250,271)

        
        self.vbox = QVBoxLayout(self)
        self.form = QFormLayout(self)
        
        self.icon = QPixmap("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/motor.png")
        self.lbl = QLabel()
        self.lbl.setPixmap(self.icon)

        self.motor_label = QLineEdit(self)

        self.pot = QLineEdit(self)
        self.pot.setValidator(QIntValidator())
        

        self.fp = QLineEdit(self)
        self.fp.setValidator(QDoubleValidator(0,1,2))

        self.rot = QLineEdit(self)
        self.rot.setValidator(QIntValidator())

        self.rendimento = QLineEdit(self)
        self.rendimento.setValidator(QDoubleValidator(0,1,2))

        self.create = QPushButton("criar")
        self.create.clicked.connect(self.post)
        self.create.setObjectName("create")
        
        self.search = QPushButton("procurar")
        self.search.setObjectName("search")

        self.vbox.setSpacing(5)
        self.vbox.addWidget(self.lbl, alignment=Qt.AlignCenter)
        self.form.addRow("tag:", self.motor_label)
        self.form.addRow("potencia (HP):", self.pot)
        self.form.addRow("fp:", self.fp)
        self.form.addRow("rotação:",self.rot)
        self.form.addRow("rendimento:",self.rendimento)
        self.form.addRow(self.create, self.search)
        self.vbox.addLayout(self.form)
        self.setLayout(self.vbox)
        
        
    
    def post(self):
        time_now = datetime.datetime.now().strftime("%d/%m/%y-%H:%M:%S")
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        self.data = {
                        "tag":str(self.motor_label.text()),
                        "potencia":int(self.pot.text()),
                        "fp":float(self.fp.text()),
                        "rotacao":int(self.rot.text()),
                        "rendimento":float(self.rendimento.text()),
                        "data":str(time_now),
                        "ensaios":0
                    }
        
        try:
            result=requests.post("http://127.0.0.1:5000/register", data=json.dumps(self.data), headers=headers)
            make_dir_a_tag(self.data['tag']) 
            
        except:
            self.message.emit("Servidor se encontrola offline")

        else:
            if result.status_code == 400:
                self.message.emit(str(result.json()['message']))
            else:
                self.dataSignal.emit(True)
            

        
 

        




        
  
        
        
 



