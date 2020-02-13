from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox
from PyQt5.QtGui import QIntValidator

class Cut(QGroupBox):
    def __init__(self, parent = None):
        super(QGroupBox, self).__init__(parent)
        self.setFixedSize(500,50)

        self.hbox = QHBoxLayout()

        self.label1 = QLabel("split")
        self.label2 = QLabel(":")  

        self.apply = QPushButton("aplicar")
        self.save = QPushButton("save")

        self.start = QLineEdit()
        self.start.setCursorPosition(0)
        self.start.setValidator(QIntValidator())

        self.stop = QLineEdit()
        self.stop.setValidator(QIntValidator())

        

    
    def cut(self):
        self.hbox.addWidget(self.label1)
        self.hbox.addWidget(self.start)
        self.hbox.addWidget(self.label2)
        self.hbox.addWidget(self.stop)
        self.hbox.addWidget(self.apply)
        self.hbox.addWidget(self.save)
        self.setLayout(self.hbox)
        return self