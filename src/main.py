# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from parse_ui import MainForm


if __name__ == "__main__":
    icon_file = "doc/icons/icon.ico"
    note_file = "doc/text/note.txt"

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(icon_file))

    with open(note_file, 'r', encoding = "utf-8") as f:
        note_text = f.read()
 
    window = MainForm(note_text)
    window.show()
    
    sys.exit(app.exec())