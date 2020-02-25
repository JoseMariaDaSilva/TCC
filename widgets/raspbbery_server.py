from PyQt5.QtWidgets import (QGroupBox, QHBoxLayout, QFormLayout, QPushButton, QLineEdit, QLabel, QWidget, 
                             QVBoxLayout, QTextEdit)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import requests
import json



class raspGp(QGroupBox):
    def __init__(self, parent = None):
        super(QGroupBox, self).__init__(parent)

        self.setFixedSize(250,271)
        self.form = QFormLayout()
        
        self.apply = QPushButton("aplicar")
        self.ping = QPushButton("ping")
        self.ping.clicked.connect(self.ping_)

        self.addres = QLineEdit("http://127.0.0.1:5000/")
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
            data = dict(requests.get("http://127.0.0.1:5000/test").json())
            
        except:
            self.textOutput.append("server: off")
            self.textOutput.append("error request!.")
            self.textOutput.append("=========================")
            
        else:
            for item in data.values():
                self.textOutput.append(item)
            self.textOutput.append("=========================")


    