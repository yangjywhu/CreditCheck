# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from form.start import MainForm


if __name__ == "__main__":
    icon_file = "doc/icons/icon.ico"
    note_file = "doc/text/note.txt"

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(icon_file))
 
    window = MainForm()
    window.show()
    
    sys.exit(app.exec())