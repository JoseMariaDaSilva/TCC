from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QFormLayout, QVBoxLayout, QSpinBox, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QIntValidator, QDoubleValidator, QIcon
from PyQt5.QtCore import Qt


class Run(QGroupBox):
    def __init__(self, parent = None):
        super(QGroupBox, self).__init__(parent)
        self.setFixedSize(250,275)

        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.form = QFormLayout()
        
        self.icon = QPixmap("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/motor.png")
        self.lbl = QLabel()
        self.lbl.setPixmap(self.icon)

        self.motor_label = QLineEdit()

        self.pot = QLineEdit()
        self.pot.setValidator(QIntValidator())
        

        self.fp = QLineEdit()
        
        self.fp.setValidator(QDoubleValidator(0,1,2))

        self.start = QPushButton("START")
        self.start.setObjectName("bt_play")

        self.stop = QPushButton("STOP")
        self.stop.setObjectName("bt_stop")
        
    
    def run(self):
        self.vbox.addWidget(self.lbl, alignment=Qt.AlignCenter)
        self.form.addRow("motor label:", self.motor_label)
        self.form.addRow("potencia(KW):", self.pot)
        self.form.addRow("fp:", self.fp)
        self.vbox.addLayout(self.form)
        self.hbox.addWidget(self.start)
        self.hbox.addWidget(self.stop)
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)
        
        return self

        