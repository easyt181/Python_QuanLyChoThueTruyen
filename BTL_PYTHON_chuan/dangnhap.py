from PySide6.QtWidgets import *
from PySide6.QtGui import QAction
from ui_dangnhap import Ui_MainWindow

class Login(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quản lý cửa hàng truyện")

        