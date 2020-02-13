from PyQt5.QtWidgets import QTabWidget, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt
from .history import Tablet



class Tabs(QTabWidget):

    

    def __init__(self, parent = None):
        super(QTabWidget, self).__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)
        self.setMovable(True)
        self.setElideMode(Qt.ElideRight)
        self.setUpdatesEnabled(True)
        self.tab1 = Tablet(self)
        self.addTab(self.tab1, 'histórico')
        self.setObjectName('tab1')
        self.tab1.signal.connect(self.addTabs)
        self.tab_alternative = self
        
    
    def closeTab(self, index):
        
        if self.tabText(index) == "histórico":
            pass
        else:
            
            self.widget(index)
            self.removeTab(index)

    def addTabs(self, name):
        
        self.addTab(options(self), str(name))




class hist(QWidget):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent)
        self.hbox = QHBoxLayout(self)
        self.hbox.addWidget(Tablet(self))
        self.setLayout(self.hbox)

class options(QWidget):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent)

        self.hbox = QHBoxLayout(self)
        self.setLayout(self.hbox)







    

    

