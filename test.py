from PyQt5.QtWidgets import QApplication, QTableView, QAbstractItemView, QPushButton
from PyQt5.QtGui import QStandardItemModel, QStandardItem

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    tab = QTableView()
    sti = QStandardItemModel()
    sti.appendRow([QStandardItem(str(i)) for i in range(4)])
    tab.setModel(sti)
    tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
    tab.setIndexWidget(sti.index(0, 3), QPushButton("button"))
    tab.show()
    sys.exit(app.exec_())