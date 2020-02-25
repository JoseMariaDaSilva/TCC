from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from .widgets import MyWidget

class MainWindow(QMainWindow):

    def __init__(self, parent = None):
        super(QMainWindow, self).__init__(parent)
        
        self.setFixedSize(1200, 600)
        self.setWindowTitle("tcc")

        self.menubar = self.menuBar()
        self.saveAct = QAction('Save log', self)
        self.save_asAct = QAction('Save As log...', self)
        self.exitAct = QAction('Exit', self)
        self.restart = QAction("restart",self)
        
        self.fileMenu = self.menubar.addMenu('File')
        
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.save_asAct)
        self.fileMenu.addAction(self.exitAct)
        self.fileMenu.addAction(self.restart)
      
        self.editMenu = self.menubar.addMenu('Edit')
        self.helpMenu = self.menubar.addMenu('Help')
        
        self.aboutMenu = self.menubar.addMenu("About")

        wid = MyWidget(self)
        self.setCentralWidget(wid)
        self.new_window = list()

    def tuto(self):
        window = SecondWindow()
        self.new_window.append(window)

        window.show()

class SecondWindow(QMainWindow):
    def __init__(self, parent = None):
        super(QMainWindow, self).__init__(parent)

        self.icon = QPixmap("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/tuto_test.png")
        self.label = QLabel()
        self.label.setPixmap(self.icon)
        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

    

        
