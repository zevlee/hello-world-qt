#!/bin/sh

# This script is meant to be run through MinGW

pacman -S --noconfirm mingw-w64-$(uname -m)-pyside6 mingw-w64-$(uname -m)-python-pip mingw-w64-$(uname -m)-nsis mingw-w64-$(uname -m)-nsis-nsisunz zip unzip

echo "Done"
