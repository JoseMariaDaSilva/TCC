from PyQt5.QtWidgets import (
                             QTabWidget, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, 
                             QLabel, QGroupBox, QComboBox, QLineEdit, QFormLayout, QTextEdit, QMessageBox
                             )

from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QThread
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from .table import TableWidget
from .plot import Plotting
from tools.deep_path import delete_folder_exists, deep_folder_location
import paho.mqtt.client as mqtt
import requests
import numpy as np
from ast import literal_eval
import os
import pandas as pd
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
            
            if (self.tabText(count_tab) == name) or name == "?":
                break
              
        else:
            self.addTab(options(name), str(name))




class options(QWidget):
    
    def __init__(self, name, parent = None):
        self.name = name
        super(QWidget, self).__init__(parent)
        
        self.ad = Receive_from_ad('mqtt.eclipse.org', 1883, 'request')
        self.vbox = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.real = Plotting()
        self.rms = Plotting()
        
        self.tabb = Tabs()
        self.tabb.index_signal.connect(self.delete_from_table_func)
        self.nav = NavigationToolbar(self.rms, self.tabb, coordinates=False)
        self.nav.setStyleSheet('background-color: 0;')
        self.nav.setFixedHeight(25)
        self.nav2 = NavigationToolbar(self.real, self.tabb, coordinates=False)
        self.nav2.setFixedHeight(25)
        self.nav2.setStyleSheet('background-color: 0;')
        self.vbox.setSpacing(0)
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
        self.setStyleSheet("""QWidget {
                                background-color:qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #59595e, stop:1 #0b0b0d);
                            }
                              QLabel {
                                background-color:0;
                            }
                              QIcon {
                                  background-color:0;
                            }
                            """)

        
        """
        x = [x for x in range(10)]
        y1 = np.array([x**2 for x in range(10)])
        y2 = np.array(sorted([x**2 for x in range(10)], reverse=True))

        self.real.plot(x, y1, "real")
        self.rms.plot(x, y2, "rms")
        """
        self.ploti()
        self.ad.start()
        self.ad.data_signal.connect(self.plot_anything)

    def ploti(self):
        x = os.path.join(deep_folder_location('motores_registrados'),self.name)
        x1 = os.path.join(x,'ensaios')
        k = os.listdir(x1)
        for files in k:
            pt = pd.read_csv(os.path.join(x1,files))
            dim = len(pt)
            z = np.arange(len(pt))
            b = np.array(pt).reshape(1,dim)
            self.real.plot(z, b[0])

        

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
        gp1 = QGroupBox()
        gp1.setFixedSize(250,237)
        self.vbox = QVBoxLayout()
        return gp1
    
    def plot_anything(self, data):
        x = data
        my_path1 = os.path.join(deep_folder_location('motores_registrados'),self.name)
        my_path2 = os.path.join(my_path1,'ensaios')

        try:
            n_files = len(os.listdir(my_path2))
            my_last_path = os.path.join(my_path2,'ensaio_{}'.format(n_files))
        except:
            pass
        df_ensaio = pd.DataFrame([x]).transpose()
        df_ensaio.to_csv(my_last_path, index=False)
        self.ploti()

    def start(self):
        try:
            mqttc = mqtt.Client('999')
            mqttc.connect('mqtt.eclipse.org', 1883)
            mqttc.publish('ad', 'on')
            self.log.append('Leitura iniciada...')
        except:
            pass

    def stop(self):
        try:
            mqttc = mqtt.Client('999')
            mqttc.connect('mqtt.eclipse.org', 1883)
            mqttc.publish('ad', 'off')
            self.log.append('Fim da leitura...')
        except:
            pass

    def delete_from_table_func(self):
        
        buttonReply=QMessageBox.question(self, 'Menssagem', "Deseja deletar este motor?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            delete_folder_exists(str(self.name))
            mqttc = mqtt.Client('100')
            mqttc.connect('mqtt.eclipse.org', 1883)
            mqttc.publish('alter', self.name)
            self.close()
        else:
            pass
        
class Receive_from_ad(QThread):
    data_signal = pyqtSignal(list)
    def __init__(self, broker, port, topic, parent=None):
        super(Receive_from_ad, self).__init__(parent)
        self.broker = broker
        self.port = port
        self.topic = topic
        print("[STATUS] Inicializando MQTT...")
        #inicializa MQTT:
        self.client = mqtt.Client('10010')
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.broker, self.port)


    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(self.topic)
 
    
    def on_message(self, client, userdata, msg):
        self.data_signal.emit(literal_eval((msg.payload).decode('utf-8')))
        
    def run(self):
        self.client.loop_forever()
        




    








    

    

