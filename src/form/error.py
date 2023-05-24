from PySide6.QtWidgets import QWidget
from ui.error import Ui_Dialog

# class MySlot(QObject)

class ErrorDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()

        self.ui.setupUi(self)


        