from PyQt5.QtWidgets import QApplication
from widgets.main_window import MainWindow

import sys




if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open("front.qss","r") as file:
        app.setStyleSheet(file.read())

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())