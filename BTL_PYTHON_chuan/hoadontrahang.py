from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import mysql.connector
from ui_hoadontrahang import Ui_Quanlyhodon

class HoaDonTraHang(QMainWindow, Ui_Quanlyhodon):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quản lý hóa đơn trả hàng")
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

    def refreshTable(self):
        try:
            self.lineSearch.clear()
            self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
            self.loadInvoiceData()
            print("Data refreshed successfully.")
        except Exception as e:
            print(f"Error refreshing table: {e}")

    def loadInvoiceData(self):
        try:
            query = """
                SELECT hdth.hdth_id, hdth.hdth_hdb_id, nv.nv_ten, hdb.hdb_kh_sdt_id, hdth.hdth_ngaytrahang, hdth.hdth_tongtienhoantra
                FROM hoadontrahang hdth
                INNER JOIN nhanvien nv ON hdth.hdth_nv_id = nv.nv_id
                INNER JOIN hoadonban hdb ON hdth.hdth_hdb_id = hdb.hdb_id
                ORDER BY hdth.hdth_id ASC
            """
            self.db_cursor.execute(query)
            invoices = self.db_cursor.fetchall()

            self.tableWidget.setRowCount(len(invoices))
            for row_index, invoice in enumerate(invoices):
                for col_index in range(len(invoice)):
                    item = QTableWidgetItem(str(invoice[col_index]))
                    self.tableWidget.setItem(row_index, col_index, item)

        except mysql.connector.Error as e:
            print(f"Error loading invoice data: {e}")

    def searchInLineEdit(self):
        search_text = self.lineSearch.text().strip()
        try:
            query = f"""
                SELECT hdth.hdth_id, hdth.hdth_hdb_id, nv.nv_ten, hdb.hdb_kh_sdt_id, hdth.hdth_ngaytrahang, hdth.hdth_tongtienhoantra
                FROM hoadontrahang hdth
                INNER JOIN nhanvien nv ON hdth.hdth_nv_id = nv.nv_id
                INNER JOIN hoadonban hdb ON hdth.hdth_hdb_id = hdb.hdb_id
                WHERE (hdth.hdth_id LIKE '%{search_text}%' OR
                       hdth.hdth_hdb_id LIKE '%{search_text}%' OR
                       nv.nv_ten LIKE '%{search_text}%' OR
                       hdb.hdb_kh_sdt_id LIKE '%{search_text}%' OR
                       hdth.hdth_ngaytrahang LIKE '%{search_text}%' OR
                       CAST(hdth.hdth_tongtienhoantra AS CHAR) LIKE '%{search_text}%')
                ORDER BY hdth.hdth_id ASC
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
                SELECT hdth.hdth_id, hdth.hdth_hdb_id, nv.nv_ten, hdb.hdb_kh_sdt_id, hdth.hdth_ngaytrahang, hdth.hdth_tongtienhoantra
                FROM hoadontrahang hdth
                INNER JOIN nhanvien nv ON hdth.hdth_nv_id = nv.nv_id
                INNER JOIN hoadonban hdb ON hdth.hdth_hdb_id = hdb.hdb_id
                WHERE hdth.hdth_ngaytrahang LIKE '{selected_date}%'
                ORDER BY hdth.hdth_id ASC
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
    mainWindow = HoaDonTraHang()
    mainWindow.show()
    sys.exit(app.exec())
