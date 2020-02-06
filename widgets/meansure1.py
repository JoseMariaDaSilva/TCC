from PyQt5.QtWidgets import QGroupBox, QHBoxLayout


class M1(QGroupBox):
    def __init__(self, parent = None):
        super(QGroupBox, self).__init__(parent)
        self.setFixedSize(200,275)

    
    def m1(self):
        return self