from PyQt5.QtWidgets import (
                            QWidget, QTableView, QHeaderView, QPushButton, 
                            QTableView, QListView, QHBoxLayout,
                            QVBoxLayout, QComboBox, QItemDelegate, QStyledItemDelegate, QAbstractItemView, QLineEdit
                            )

from PyQt5.QtCore import (Qt, pyqtSignal, QSortFilterProxyModel, QModelIndex,
                         QPersistentModelIndex, QSize, QRegExp, pyqtSlot, QAbstractTableModel, QVariant, pyqtSignal, pyqtSlot, QObject,
                         QTimer
                            )
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
import requests
from .run import Run
import operator






class TableModel(QAbstractTableModel):
    
    tabSignal = pyqtSignal(str)
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

        self.header = "id,tag,potencia,fp,rotacao,rendimento,data,ensaios".split(',')
    
    def rowCount(self, parent=QModelIndex()): 
        return len(self._data)

    def columnCount(self, parent=QModelIndex()): 
        return len(self.header)

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self._data[index.row()][index.column()]

    def setData(self, index, value, role=Qt.DisplayRole):
        result = index.sibling(index.row(),1).data()
        self.tabSignal.emit(result)
        #print("setData", index.row(),1, result)

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header[col])
        return QVariant()

    def sort(self, Ncol, order):
        """Sort table by given column number."""
        self.layoutAboutToBeChanged.emit()
        self._data = sorted(self._data, key=operator.itemgetter(Ncol))        
        if order == Qt.AscendingOrder:
            self._data.reverse()
        self.layoutChanged.emit()
    

    def changeData(self, datain):
        self.layoutAboutToBeChanged.emit()
        self._data = datain
        self.layoutChanged.emit()

    def flags(self, index):
        if index.column() in [0]:
            return Qt.ItemIsEditable | Qt.ItemIsEnabled
        else:
            return Qt.ItemIsEnabled

    
class TableView(QTableView):
    def __init__(self, parent=None):
        super(QTableView, self).__init__(parent)

        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    

class TableWidget(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        try:
            self.data = requests.get("http://192.168.15.86/list", timeout=2).json()['motors']

        except:
            self.data = [["-" for _ in range(8)]]

        finally:
            
            self.tm = TableModel(self.data)
            self.tv = TableView(self)
            #self.refresh = QPushButton('refresh')
            #self.refresh.clicked.connect(self.show_data)
            
            self.tv.setItemDelegateForColumn(0,ButtonDelegate(self))
            self.tv.setModel(self.tm)
            self.tv.setSortingEnabled(True)
            self.hbox = QHBoxLayout()
            self.vbox = QVBoxLayout()
            #self.vbox.addWidget(self.refresh)
            self.vbox.addWidget(self.tv)
            self.setLayout(self.vbox)

        
    def show_data(self):
        try:
            
            self.tm.changeData(new_data)
            self.tv = TableView()
            self.tv.setModel(self.tm)
            print('to funcionando!')
        except:
            pass




class ButtonDelegate(QItemDelegate):
    
    def __init__(self, parent):
        QItemDelegate.__init__(self, parent)
        self.icon = QIcon("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/tab_icon.png")



    def createEditor(self, parent, option, index):
        combo = QPushButton("show", parent)
        combo.setIcon(self.icon)
        combo.setObjectName('mostrar')
        combo.clicked.connect(self.currentIndexChanged)
        return combo
        
    def setEditorData(self, editor, index):
        editor.blockSignals(True)
        editor.blockSignals(False)
        
    def setModelData(self, editor, model, index):
        model.setData(index, editor.text())
        
    @pyqtSlot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender())







    

    




   


