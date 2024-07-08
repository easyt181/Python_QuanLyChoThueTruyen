from PySide6.QtWidgets import QApplication
from frontPage import MySidebar
from hoadonban import HoaDonBan
from dangnhap import Login

import mysql.connector
import sys

app = QApplication(sys.argv)

window = MySidebar()

window.show()
app.exec()