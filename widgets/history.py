from PyQt5.QtWidgets import (
                            QWidget, QTableWidget, QTableView, QTableWidgetItem, QHeaderView, QPushButton, qApp, 
                            QTableView, QListView, QAbstractItemView, QRadioButton, QHBoxLayout, QSizePolicy, 
                            QAbstractScrollArea, QVBoxLayout, QLineEdit, QCheckBox, QComboBox, QItemDelegate, QStyledItemDelegate
                            )

from PyQt5.QtCore import Qt, pyqtSignal, QSortFilterProxyModel, QModelIndex, QPersistentModelIndex, QSize, QRegExp, pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
import requests
import json


class Tablet(QWidget):

    signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.headers = "id,motor_tag,potencia,fator_potencia,rotação,rendimento,n_ensaios,data,apagar".split(',')
        self.model = QStandardItemModel(100,8)
        self.model.setHorizontalHeaderLabels(self.headers)
        self.table = QTableView(self)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label = ["motor_"+str(x) for x in range(10)]
        self.addTab = QIcon("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/tab_icon.png")
        self.clear = QPushButton('limpar')
        self.hbox = QHBoxLayout()
        

        for row, item in enumerate(self.label):
                tabletItem = QStandardItem(item)
                tabletItem.setTextAlignment(Qt.AlignHCenter)
                self.model.setItem(row,1,tabletItem)


        for row, item in enumerate(self.label):
                delete_row = QPushButton()
                delete_row.setStyleSheet("""background-color:qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #e4ede4, stop:1 #d1e3d1);
                                            border-radius:0px;
                                            border:0px;
                                          """)
                                          
                delete_row.setIcon(QIcon("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/delete_icon.png"))
                delete_row.setIconSize(QSize(20,20))
                delete_row.clicked.connect(self.deleteRow)
                self.table.setIndexWidget(self.model.index(row,8), delete_row)


        show_tab = QPushButton(str(row))
        show_tab.setIcon(self.addTab)
        show_tab.setStyleSheet("""background-color:qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #e4ede4, stop:1 #d1e3d1);
                                    border-radius:0px;
                                    border:0px;
                                    color:black;
                                    """)
        show_tab.setIconSize(QSize(20,20))
        show_tab.clicked.connect(self.handleButtonClicked)
        self.table.setItemDelegateForColumn(0, ShowButton(self))

        self.proxy = QSortFilterProxyModel()
        self.proxy.setSourceModel(self.model)
        self.table.setModel(self.proxy)
        
        self.search = QLineEdit()
        self.search.textChanged.connect(self.find_tag)
        
        
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
        

        self.vbox = QVBoxLayout(self)
        self.hbox.addWidget(self.search)
        self.hbox.addWidget(self.clear)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.table)
        self.setLayout(self.vbox)


    def handleButtonClicked(self):
        button = qApp.focusWidget()
        # or button = self.sender()
        index = self.table.selectionModel().currentIndex()
        value = index.sibling(index.row(), 1)
        
        if index.isValid():
            self.signal.emit(value.data())

    def deleteRow(self):
        button = qApp.focusWidget()
        row = self.table.selectionModel().currentIndex().row()
        self.model.removeRow(row)
        
    
    def find_tag(self, text):
        search = QRegExp(text, 
                         Qt.CaseInsensitive,
                         QRegExp.RegExp 
                         )
        self.proxy.setFilterRegExp(search)
        self.proxy.setFilterKeyColumn(1)

    
class Delegate(QStyledItemDelegate):
    def __init__(self, owner):
        super().__init__(owner)
 

    def createEditor(self, parent, option, index):
        editor = QPushButton("show", parent)
        return editor

    def paint(self, painter, option, index):
        if isinstance(self.parent(), QAbstractItemView):
            self.parent().openPersistentEditor(index, 1)
        QStyledItemDelegate.paint(self, painter, option, index)


