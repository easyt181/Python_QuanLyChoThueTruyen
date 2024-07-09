from PySide6.QtWidgets import QApplication
from dangnhap import Login
import sys

app = QApplication(sys.argv)

# Mở màn hình đăng nhập
loginWindow = Login()
loginWindow.show()

app.exec()
