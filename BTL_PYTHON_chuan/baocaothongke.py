import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QAction
from ui_main import Ui_MainWindow
import mysql.connector
from datetime import datetime, date
from bieudothongke import BieuDo
from ui_baocaothongke import Ui_ThongKe
class BaoCaoThongKe(QMainWindow, Ui_ThongKe):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quản lý cửa hàng truyện")
        self.dothi = BieuDo()  # Đây là đoạn khởi tạo MainWindow hoặc lớp con của QWidget

        # Đặt MainWindow vào layout của MySidebar
        self.verticalLayout_13.addWidget(self.dothi)

        # Kết nối đến cơ sở dữ liệu
        self.setupDatabaseConnection()

        # Lấy tổng số lượng sách từ bảng `sach`
        total_books_query = "SELECT SUM(s_soluong) FROM sach"
        self.db_cursor.execute(total_books_query)
        total_books = self.db_cursor.fetchone()[0]
        self.label_9.setText(f"{total_books}")

        # Lấy tổng số hóa đơn bán ngày hôm nay từ bảng `hoadonban`
        today = date.today()
        today_str = today.strftime("%Y-%m-%d")
        total_sales_today_query = f"""
                    SELECT COUNT(*) FROM hoadonban WHERE DATE(HDB_NgayXuat) = '{today_str}'
                """
        self.db_cursor.execute(total_sales_today_query)
        total_sales_today = self.db_cursor.fetchone()[0]
        self.label_10.setText(f"{total_sales_today}")

        # Lấy tổng số hóa đơn nhập ngày hôm nay từ bảng `hoadonnhap`
        total_purchases_today_query = f"""
                    SELECT COUNT(*) FROM hoadonnhap WHERE DATE(hdn_ngayxuat) = '{today_str}'
                """
        self.db_cursor.execute(total_purchases_today_query)
        total_purchases_today = self.db_cursor.fetchone()[0]
        self.label_11.setText(f"{total_purchases_today}")

        # Lấy tổng số hóa đơn thuê truyện ngày hôm nay từ bảng `hoadonchothue`
        total_rentals_today_query = f"""
                    SELECT COUNT(*) FROM hoadonchothue WHERE DATE(hdct_ngaythue) = '{today_str}'
                """
        self.db_cursor.execute(total_rentals_today_query)
        total_rentals_today = self.db_cursor.fetchone()[0]
        self.label_12.setText(f"{total_rentals_today}")

        # Đóng kết nối cơ sở dữ liệu
        self.db_cursor.close()
        self.db_connection.close()


    def setupDatabaseConnection(self):
        try:
            self.db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db_nhom7_python"
            )
            self.db_cursor = self.db_connection.cursor()
            print("Connected to database successfully!")
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL database: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = BaoCaoThongKe()
    mainWindow.show()
    sys.exit(app.exec())