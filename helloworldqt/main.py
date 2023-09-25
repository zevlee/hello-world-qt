#!/usr/bin/env python3

from sys import exit
from .application import Application
from .window import Window


def main(argv):
    app = Application(argv)
    window = Window()
    window.show()
    exit(app.exec())
