from PyQt5.QtWidgets import (
                             QTabWidget, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, 
                             QLabel, QGroupBox, QComboBox, QLineEdit, QFormLayout, QTextEdit, QMessageBox
                             )

from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from .table import TableWidget
from .plot import Plotting
import paho.mqtt.client as mqtt
import requests
import numpy as np
import random



class Tabs(QTabWidget):
    name_signal = pyqtSignal(str)
    index_signal = pyqtSignal(int)
    def __init__(self, parent = None):
        super(QTabWidget, self).__init__(parent)
        self.setTabsClosable(True)
        self.icon = QIcon("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/motor.png")
        self.tabCloseRequested.connect(self.closeTab)
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
            self.index_signal.emit(index)
            self.widget(index)
            self.removeTab(index)

    def addTabs(self, name):
        
        for count_tab in range(self.count()):
            print(count_tab,'oi')
            if self.tabText(count_tab) == name:
                break
        else:
            self.addTab(options(name), str(name))




class options(QWidget):
    
    def __init__(self, name, parent = None):
        self.name = name
        super(QWidget, self).__init__(parent)
        self.setStyleSheet("background-color:qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #59595e, stop:1 #0b0b0d);")
    
        self.vbox = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.real = Plotting(self)
        self.rms = Plotting(self)
        self.tabb = Tabs()
        self.tabb.index_signal.connect(self.delete_from_table_func)
        self.nav = NavigationToolbar(self.rms, self.tabb, coordinates=False)
        self.nav2 = NavigationToolbar(self.real, self.tabb, coordinates=False)
        
        self.vbox.addWidget(self.real)
        self.vbox.addWidget(self.nav2)
        self.vbox.addWidget(self.rms)
        self.vbox.addWidget(self.nav)
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
        gp1 = QGroupBox(self)
        gp1.setFixedSize(250,237)
        self.configV = QVBoxLayout(self)
        self.configV.setAlignment(Qt.AlignHCenter)
        self.cnnV = QVBoxLayout(self)
        self.form = QFormLayout(self)
        self.trash = QIcon("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/trash_icon.png")
        self.delete_from_table = QPushButton(self.trash, "remover")
        self.delete_from_table.clicked.connect(self.delete_from_table_func)
        self.delete_from_table.setStyleSheet('QPushButton {border:0px; background-color:0;}')

        self.iniciar = QPushButton('iniciar')
        self.iniciar.clicked.connect(self.start)
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

        self.parar = QPushButton('parar')
        self.parar.clicked.connect(self.stop)
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
                                    background-color: qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #59595e, stop:1 #0b0b0d);
                                    border-radius: 5px;
                                }
                                """)
        self.log.setReadOnly(True)
        
        
        self.form.addRow(self.iniciar, self.parar)
        self.form.addRow(self.save, self.extension)
        self.configV.addLayout(self.form)
        self.configV.addWidget(self.log, alignment=Qt.AlignRight)
        self.configV.addWidget(self.delete_from_table, alignment=Qt.AlignRight)
        
        gp1.setLayout(self.configV)
        
        return gp1

    def cnn(self):
        gp1 = QGroupBox(self)
        gp1.setFixedSize(250,237)
        self.vbox = QVBoxLayout()
        
        return gp1

    def start(self):
        print(self.name)
        try:
            pass
        except:
            pass

    def stop(self):
        try:
            pass
        except:
            pass

    def delete_from_table_func(self):
        mqttc = mqtt.Client('100')
        mqttc.connect('mqtt.eclipse.org', 1883)
        mqttc.publish('alter', self.name)
        
        self.close()
        
        
        




    








    

    

