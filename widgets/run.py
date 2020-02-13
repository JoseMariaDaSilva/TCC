from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QFormLayout, QVBoxLayout, QSpinBox, QPushButton, QLabel, QLineEdit, QTabWidget
from PyQt5.QtGui import QPixmap, QIntValidator, QDoubleValidator, QIcon
from PyQt5.QtCore import Qt, pyqtSignal
from .plot import Plotting






class Run(QGroupBox):

    signal = pyqtSignal(str)

    def __init__(self, parent = None):
        super(QGroupBox, self).__init__(parent)
        self.setFixedSize(250,271)

        
        self.vbox = QVBoxLayout(self)
        self.hbox = QHBoxLayout(self)
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
        self.create.setObjectName("create")
        
        self.search = QPushButton("procurar")
        self.search.setObjectName("search")


        self.vbox.addWidget(self.lbl, alignment=Qt.AlignCenter)
        self.form.addRow("tag:", self.motor_label)
        self.form.addRow("potencia (HP):", self.pot)
        self.form.addRow("fp:", self.fp)
        self.form.addRow("rotação:",self.rot)
        self.form.addRow("rendimento:",self.rendimento)
        self.vbox.addLayout(self.form)
        self.hbox.addWidget(self.create, alignment=Qt.AlignHCenter)
        self.hbox.addWidget(self.search, alignment=Qt.AlignHCenter)
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)

        




        
  
        
        
 



