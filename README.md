1. chạy lệnh pyside6-rcc resources.qrc -o resources.py
2. copy file resources.py vào thư mục ui
3. trong thư mục ui đổi dòng 'from PySide6 import QtCore' thành 'from PyQt6 import QtCore'
