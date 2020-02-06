from PyQt5.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
from .raspbbery_server import raspGp
from .meansure1 import M1
from .meansure2 import M2
from .meansure3 import M3
from .meansure4 import M4
from .graph import Graph
from .cut_graph import Cut
from .run import Run





class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()
        vbox4 = QVBoxLayout()
        
        hbox = QHBoxLayout()
        
        vbox1.addWidget(raspGp().rasp())
        vbox1.addWidget(Run().run())
        vbox1.setContentsMargins(0,0,0,0)
        vbox1.setSpacing(0)
        
        hbox.addLayout(vbox1)

        vbox2.addWidget(Graph().graph())
        vbox2.addWidget(Cut().cut())

        hbox.addLayout(vbox2)

        vbox3.addWidget(M1().m1())
        vbox3.addWidget(M2().m2())

        hbox.addLayout(vbox3)

        vbox4.addWidget(M3().m3())
        vbox4.addWidget(M4().m4())

        hbox.addLayout(vbox4)




        
        
        self.setLayout(hbox)





