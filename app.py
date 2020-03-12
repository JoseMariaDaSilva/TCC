from PyQt5.QtWidgets import QApplication
from widgets.main_window import MainWindow
from widgets.enter_window import My_entry


import sys




if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open("front.qss","r") as file:
        app.setStyleSheet(file.read())
    
    main = My_entry()
    main.show()
    main.repaint()
    main.update()

    sys.exit(app.exec_())