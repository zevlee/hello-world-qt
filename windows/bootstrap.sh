#!/bin/sh

# This script is meant to be run through MinGW

pacman -S --noconfirm mingw-w64-x86_64-pyside6 mingw-w64-x86_64-python-pip mingw-w64-x86_64-nsis mingw-w64-x86_64-nsis-nsisunz mingw-w64-x86_64-gcc zip unzip

echo "Done"
