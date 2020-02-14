from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QTabWidget, QVBoxLayout, QWidget, QLabel
from .tabs import Tabs
from .plot import Plotting
from .run import Run





class Output(QGroupBox):
    def __init__(self, parent = None):
        super(QGroupBox, self).__init__(parent)
        self.setFixedSize(900,540)
        self.hbox = QHBoxLayout(self)
        self.tab = Tabs(self)
        self.hbox.addWidget(self.tab)
        self.setLayout(self.hbox)


        






