from PyQt5.QtWidgets import QTabWidget
from widgets.plot import Plotting


class Tabs(QTabWidget):
    def __init__(self, parent = None):
        super(QTabWidget, self).__init__(parent)

        self.canvas1 = Plotting()
        self.canvas2 = Plotting()
        self.canvas3 = Plotting()

        self.tab1 = self.canvas1
        self.tab1.setObjectName("tab1")

        
        self.tab2 = self.canvas2
        self.tab2.setObjectName("tab2")

        
        self.tab3 = self.canvas3
        self.tab3.setObjectName("tab3")
        
        self.addTab(self.tab1,"grafico_1")
        self.addTab(self.tab2,"grafico_2")
        self.addTab(self.tab3,"grafico_3")

    def plot(self, x, y):
        self.canvas1.plot(x,y)
        
        #self.canvas2.plot(x,y)
        #self.canvas2.draw()
        #self.canvas3.plot(x,y)
        #self.canvas3.draw()



    

    

