from PyQt5.QtWidgets import (QGroupBox, QHBoxLayout, QFormLayout, QPushButton, QLineEdit, QLabel, QWidget, 
                             QVBoxLayout, QTextEdit)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class raspGp(QGroupBox):
    def __init__(self, parent = None):
        super(QGroupBox, self).__init__(parent)

        self.setFixedSize(250,275)
        self.form = QFormLayout()
        self.apply = QPushButton("aplicar")
        self.ping = QPushButton("ping")

        self.addres = QLineEdit("192.168.5.1")
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

        

    