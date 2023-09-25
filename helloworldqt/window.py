#!/usr/bin/env python3

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
