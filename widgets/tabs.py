from PyQt5.QtWidgets import (
                             QTabWidget, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, 
                             QLabel, QGroupBox, QComboBox, QLineEdit, QFormLayout, QTextEdit, QMessageBox
                             )

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
from .table import TableWidget
from .plot import Plotting
from .run import Run
import numpy as np
import random



class Tabs(QTabWidget):

    def __init__(self, parent = None):
        super(QTabWidget, self).__init__(parent)
        self.setTabsClosable(True)
        self.icon = QIcon("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/motor.png")
        self.tabCloseRequested.connect(self.closeTab)

        self.setMovable(True)
        self.setElideMode(Qt.ElideRight)
        self.setUpdatesEnabled(True)
        self.tab1 = TableWidget(self)
        self.tab1.tm.tabSignal.connect(self.addTabs)
        self.addTab(self.tab1, 'histórico')
        self.setObjectName('tab1')
        self.tab_alternative = self
    
    def closeTab(self, index):
        
        if self.tabText(index) == "histórico":
            pass
        else:
            self.widget(index)
            self.removeTab(index)

    def addTabs(self, name):
        
        for count_tab in range(self.count()):
            if self.tabText(count_tab) == name:
                break
        else:
            self.addTab(options(), str(name))






        

class options(QWidget):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent)
        self.setStyleSheet("background-color:qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #59595e, stop:1 #0b0b0d);")
        self.vbox = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.real = Plotting(self)
        self.rms = Plotting(self)
        #self.new_plot = Plotting(self)
        self.vbox.addWidget(self.real)
        self.vbox.addWidget(self.rms)
        #self.hbox.addWidget(self.new_plot)
        self.hbox.addLayout(self.vbox)
        self.vbox2.addWidget(self.config())
        self.vbox2.addWidget(self.cnn())
        self.hbox.addLayout(self.vbox2)
        self.setLayout(self.hbox)

        

        x = [x for x in range(10)]
        y1 = np.array([x**2 for x in range(10)])
        y2 = np.array(sorted([x**2 for x in range(10)], reverse=True))

        self.real.plot(x, y1, "real")
        self.rms.plot(x, y2, "rms")
        
        
        

    def config(self):
        gp1 = QGroupBox()
        gp1.setFixedSize(250,237)
        self.configV = QVBoxLayout(self)
        self.configV.setAlignment(Qt.AlignHCenter)
        self.cnnV = QVBoxLayout(self)
        self.form = QFormLayout(self)
        

        self.iniciar = QPushButton('iniciar')
        self.iniciar.setStyleSheet(""" QPushButton{
                                            width:110px;
                                            background-color:#524e4e;
                                            color:#e4ede4;
                                            padding: 1px;
                                            border-style: solid;
                                            border: 1px solid #524e4e;
                                            border-radius: 7px;
                                        }
                                        
                                        QPushButton:hover:pressed {
                                            background-color:#7f8a7f;
                                            }
                                        """)
        self.iniciar.clicked.connect(self.finish_require)

        self.parar = QPushButton('parar')
        self.parar.setStyleSheet(""" QPushButton{
                                            width:100px;
                                            background-color:#524e4e;
                                            color:#e4ede4;
                                            padding: 1px;
                                            border-style: solid;
                                            border: 1px solid #524e4e;
                                            border-radius: 7px;
                                        }
                                        
                                        QPushButton:hover:pressed {
                                            background-color:#7f8a7f;
                                            }
                                        """)

        self.save = QPushButton("salvar")
        self.save.setStyleSheet(""" QPushButton{
                                            width:110px;
                                            background-color:#524e4e;
                                            color:#e4ede4;
                                            padding: 1px;
                                            border-style: solid;
                                            border: 1px solid #524e4e;
                                            border-radius: 7px;
                                        }

                                        QPushButton:hover:pressed {
                                            background-color:#7f8a7f;
                                            }
                                        """)

        self.extension = QComboBox(self)
        self.extension.addItems(['csv','txt'])
        self.extension.setStyleSheet("""
                                    QComboBox{
                                        background-color: #c4bcbb;
                                        border-style: solid;
                                        border: 1px solid #c4bcbb;
                                        border-radius: 3px;
                                        
                                    }
                                    QComboBox::hover{
                                        border-radius:5px;
                                        background-color:#c5ced1;
                                    }
                                    QComboBox:editable {
                                        background: #524e4e;
                                    }
                                        """)
        self.log = QTextEdit(self)
        self.log.setStyleSheet("""
                                QTextEdit {
                                    border: 0px;
                                    background-color: #59595e;
                                    border-radius: 5px;
                                }
                                """)
        self.log.setReadOnly(True)

        
        self.form.addRow(self.iniciar, self.parar)
        self.form.addRow(self.save, self.extension)
        self.configV.addLayout(self.form)
        self.configV.addWidget(self.log)
        gp1.setLayout(self.configV)
        
        return gp1

    def cnn(self):
        gp1 = QGroupBox()
        
        gp1.setFixedSize(250,237)
        return gp1

    
    def finish_require(self):
        msg_ok = QMessageBox()
        
        msg_ok.question(options(self), "Test?", "Deseja salvar?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    
        if msg_ok == QMessageBox.Yes:
            print('Yes clicked.')
        else:
            print('No clicked.')








    

    

