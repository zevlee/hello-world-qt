#!/usr/bin/env python3

from PySide6 import QtWidgets


class Application(QtWidgets.QApplication):

    def __init__(self, args):
        super().__init__(args)
