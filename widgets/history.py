from PyQt5.QtWidgets import QWidget, QTableWidget, QTableView, QTableWidgetItem, QHeaderView, QPushButton, qApp
from PyQt5.QtCore import Qt, pyqtSignal



class Tablet(QTableWidget):

    signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(QTableWidget, self).__init__(parent)
        self.headers = "id,motor_tag,potencia,fator_potencia,rotação,rendimento,n_ensaios,data".split(',')
        self.setFixedSize(400,475)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setRowCount(10)
        self.setColumnCount(len(self.headers))
        self.setHorizontalHeaderLabels(self.headers)
        self.setObjectName('tablet1')
        self.setStyleSheet("background:#c4bcbb")
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        
        
        self.keys = ["show_"+str(x) for x in range(10)]
        
        for row, item in enumerate(self.keys):
            button = QPushButton(str(item))
            button.setStyleSheet("""QPushButton{
                                        background-color:#524e4e;
                                    }
                                    QPushButton:hover:pressed {
                                        background-color:#d1e3d1;
                                    }
                                    """)
            button.clicked.connect(self.handleButtonClicked)
            self.setCellWidget(row, 0, button)

        motor_labels = ["Motor_"+str(x) for x in range(10)]

        for row, item in enumerate(motor_labels):
            tabletItem = QTableWidgetItem(item)
            tabletItem.setFlags(tabletItem.flags()|Qt.ItemIsUserCheckable)
            tabletItem.setCheckState(Qt.Unchecked)
            self.setItem(row,1,QTableWidgetItem(tabletItem))

    def handleButtonClicked(self):
        button = qApp.focusWidget()
        # or button = self.sender()
        index = self.indexAt(button.pos())
        if index.isValid():
            self.signal.emit(self.item(index.row(),1).text())
            

