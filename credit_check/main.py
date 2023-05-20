# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication
from parse_ui import MainForm


if __name__ == "__main__":
    note_file = "credit_check/ui/note.txt"
    with open(note_file, 'r', encoding = "UTF-8") as f:
        note_text = f.read()

    app = QApplication(sys.argv)
 
    window = MainForm(note_text)
    window.show()
    
    sys.exit(app.exec())