chạy lệnh pyside6-rcc resources.qrc -o resources.py
copy file resources.py vào thư mục ui
trong thư mục ui đổi dòng 'from PySide6 import QtCore' thành 'from PyQt6 import QtCore'
