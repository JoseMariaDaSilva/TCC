from PyQt5.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
from .raspbbery_server import raspGp
from .meansure1 import M1
from .output import Output
from .cut_graph import Cut
from .run import Run





class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        vbox1 = QVBoxLayout()
        
        hbox = QHBoxLayout()
        run = Run()
        run.message.connect(self.show_message)
        #vbox1.addWidget(raspGp(self).rasp())
        vbox1.addWidget(run)
        vbox1.setContentsMargins(0,0,0,0)
        vbox1.setSpacing(0)
        
        hbox.addLayout(vbox1)

        hbox.addWidget(Output(self))

        self.setLayout(hbox)

    def show_message(self, message):
        QMessageBox().about(self, "Alerta!",message)






