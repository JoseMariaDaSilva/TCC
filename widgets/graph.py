from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QTabWidget, QVBoxLayout, QWidget
from widgets.tab_graph import Tabs
from widgets.plot import Plotting


class Graph(QGroupBox):
    def __init__(self, parent = None):
        super(QGroupBox, self).__init__(parent)
        self.setFixedSize(500,475)
        self.vbox = QVBoxLayout()
        self.dash = Tabs()
        self.vbox.addWidget(self.dash)
        self.setLayout(self.vbox)


    def graph(self):
        self.dash.plot([x for x in range(1000)],[x**2 for x in range(1000)])
        return self
