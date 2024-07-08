from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import mysql.connector
from ui_hoadonnhap import Ui_Quanlyhoadonnhap

class HoaDonNhap(QMainWindow, Ui_Quanlyhoadonnhap):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quản lý hóa đơn nhập")
        self.setupDatabaseConnection()
        self.loadInvoiceData()
        self.customizeTableHeader()

        # Kết nối sự kiện returnPressed của lineSearch với hàm searchInLineEdit
        self.lineSearch.returnPressed.connect(self.searchInLineEdit)

        # Kết nối sự kiện dateTimeChanged của dateTimeEdit với hàm searchByDate
        self.dateTimeEdit.dateTimeChanged.connect(self.searchByDate)

        # Kết nối sự kiện clicked của btnLamMoi với hàm refreshTable
        self.btnLamMoi.clicked.connect(self.refreshTable)

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

    def loadInvoiceData(self):
        try:
            query = """
                SELECT hdn.hdn_id, ls.ls_tensach, hdn.hdn_ngayxuat, hdn.hdn_dongia, hdn.hdn_soluong, hdn.hdn_thanhtien
                FROM hoadonnhap hdn
                INNER JOIN losach ls ON hdn.hdn_ls_id = ls.ls_id
            """
            self.db_cursor.execute(query)
            invoices = self.db_cursor.fetchall()

            self.tableWidget.setRowCount(len(invoices))
            for row_index, invoice in enumerate(invoices):
                for col_index in range(len(invoice)):
                    item = QTableWidgetItem(str(invoice[col_index]))
                    self.tableWidget.setItem(row_index, col_index, item)

            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)

        except mysql.connector.Error as e:
            print(f"Error loading invoice data: {e}")

    def searchInLineEdit(self):
        search_text = self.lineSearch.text().strip()
        try:
            query = f"""
                SELECT hdn.hdn_id, ls.ls_tensach, hdn.hdn_ngayxuat, hdn.hdn_dongia, hdn.hdn_soluong, hdn.hdn_thanhtien
                FROM hoadonnhap hdn
                INNER JOIN losach ls ON hdn.hdn_ls_id = ls.ls_id
                WHERE (hdn.hdn_id LIKE '%{search_text}%' OR
                       ls.ls_tensach LIKE '%{search_text}%' OR
                       hdn.hdn_ngayxuat LIKE '%{search_text}%' OR
                       CAST(hdn.hdn_dongia AS CHAR) LIKE '%{search_text}%' OR
                       CAST(hdn.hdn_soluong AS CHAR) LIKE '%{search_text}%' OR
                       CAST(hdn.hdn_thanhtien AS CHAR) LIKE '%{search_text}%')
            """
            self.db_cursor.execute(query)
            invoices = self.db_cursor.fetchall()

            self.tableWidget.setRowCount(len(invoices))
            for row_index, invoice in enumerate(invoices):
                for col_index in range(len(invoice)):
                    item = QTableWidgetItem(str(invoice[col_index]))
                    self.tableWidget.setItem(row_index, col_index, item)

            if len(invoices) == 0:
                self.showMessageBox("Thông báo", "Không có hóa đơn nào được tìm thấy.")

        except mysql.connector.Error as e:
            print(f"Error searching invoices: {e}")

    def searchByDate(self, dateTime):
        selected_date = dateTime.toString("yyyy-MM-dd")
        try:
            query = f"""
                SELECT hdn.hdn_id, ls.ls_tensach, hdn.hdn_ngayxuat, hdn.hdn_dongia, hdn.hdn_soluong, hdn.hdn_thanhtien
                FROM hoadonnhap hdn
                INNER JOIN losach ls ON hdn.hdn_ls_id = ls.ls_id
                WHERE hdn.hdn_ngayxuat LIKE '{selected_date}%'
            """
            self.db_cursor.execute(query)
            invoices = self.db_cursor.fetchall()

            self.tableWidget.setRowCount(len(invoices))
            for row_index, invoice in enumerate(invoices):
                for col_index in range(len(invoice)):
                    item = QTableWidgetItem(str(invoice[col_index]))
                    self.tableWidget.setItem(row_index, col_index, item)

        except mysql.connector.Error as e:
            print(f"Error searching invoices by date: {e}")

    def refreshTable(self):
        self.lineSearch.clear()
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.loadInvoiceData()

    def customizeTableHeader(self):
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        header.setStyleSheet("""
                    QHeaderView::section {
                        background-color: black;
                        color: white;
                        height: 50px;
                        font-size: 14px;
                        font-weight: bold;
                    }
                """)

    def showMessageBox(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = HoaDonNhap()
    mainWindow.show()
    sys.exit(app.exec())
