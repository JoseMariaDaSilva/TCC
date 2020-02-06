from PyQt5.QtWidgets import QGroupBox, QHBoxLayout


class M2(QGroupBox):
    def __init__(self, parent = None):
        super(QGroupBox, self).__init__(parent)
        self.setFixedSize(200,275)

    
    def m2(self):
        return self