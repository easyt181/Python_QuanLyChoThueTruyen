from PySide6.QtWidgets import *
from PySide6.QtGui import QAction
from ui_dangnhap import Ui_MainWindow
import mysql.connector


class Login(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quản lý cửa hàng truyện")

        # Kết nối nút đăng nhập với hàm kiemTraDangNhap
        self.btnDangNhap.clicked.connect(self.kiemTraDangNhap)
        self.btnThoat.clicked.connect(self.close)

        # Thiết lập kết nối đến MySQL
        self.db_connection = None
        self.ketNoiCSDL()

    def ketNoiCSDL(self):
        try:
            self.db_connection = mysql.connector.connect(
                host="localhost",  # Địa chỉ máy chủ MySQL
                user="root",  # Tên người dùng MySQL
                password="",  # Mật khẩu MySQL
                database="db_nhom7_python"  # Tên cơ sở dữ liệu
            )
            if self.db_connection.is_connected():
                print("Kết nối cơ sở dữ liệu thành công")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Lỗi kết nối", f"Không thể kết nối đến cơ sở dữ liệu:\n{err}")

    def kiemTraDangNhap(self):
        taiKhoan = self.txtTaiKhoan.toPlainText()
        matKhau = self.txtMatKhau.toPlainText()

        if self.db_connection is None or not self.db_connection.is_connected():
            QMessageBox.critical(self, "Lỗi kết nối", "Không thể kết nối đến cơ sở dữ liệu")
            return

        cursor = self.db_connection.cursor()
        query = "SELECT * FROM taikhoan WHERE tk_username=%s AND tk_password=%s"
        cursor.execute(query, (taiKhoan, matKhau))
        result = cursor.fetchone()

        if result:
            self.dangNhapThanhCong()
        else:
            QMessageBox.warning(self, "Đăng nhập thất bại", "Sai tài khoản hoặc mật khẩu!")

    def dangNhapThanhCong(self):
        # Điều hướng đến màn hình chính (MySidebar)
        from frontPage import MySidebar
        self.mainWindow = MySidebar()
        self.mainWindow.show()
        self.close()
