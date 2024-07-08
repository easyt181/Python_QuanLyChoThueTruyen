from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import mysql.connector
from ui_hoadonthuetruyen import Ui_Quanlyhoadonchothue

class HoaDonChoThue(QMainWindow, Ui_Quanlyhoadonchothue):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quản lý hóa đơn cho thuê")
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
                SELECT hdct.hdct_id, hdct.hdct_kh_sdt_id, hdct.hdct_nv_id, hdct.hdct_ngaythue, hdct.hdct_ngayhethan,
                       pct.pct_s_id, pct.pct_dongia, pct.pct_soluong, hdct.hdct_tongtien
                FROM hoadonchothue hdct
                INNER JOIN phieuchothue pct ON hdct.hdct_id = pct.pct_hdct_id
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
                SELECT hdct.hdct_id, hdct.hdct_kh_sdt_id, hdct.hdct_nv_id, hdct.hdct_ngaythue, hdct.hdct_ngayhethan,
                       pct.pct_s_id, pct.pct_dongia, pct.pct_soluong, hdct.hdct_tongtien
                FROM hoadonchothue hdct
                INNER JOIN phieuchothue pct ON hdct.hdct_id = pct.pct_hdct_id
                WHERE (hdct.hdct_id LIKE '%{search_text}%' OR
                       CAST(hdct.hdct_kh_sdt_id AS CHAR) LIKE '%{search_text}%' OR
                       hdct.hdct_nv_id LIKE '%{search_text}%' OR
                       hdct.hdct_ngaythue LIKE '%{search_text}%' OR
                       hdct.hdct_ngayhethan LIKE '%{search_text}%' OR
                       CAST(pct.pct_s_id AS CHAR) LIKE '%{search_text}%' OR
                       CAST(pct.pct_dongia AS CHAR) LIKE '%{search_text}%' OR
                       CAST(pct.pct_soluong AS CHAR) LIKE '%{search_text}%' OR
                       CAST(hdct.hdct_tongtien AS CHAR) LIKE '%{search_text}%')
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
                SELECT hdct.hdct_id, hdct.hdct_kh_sdt_id, hdct.hdct_nv_id, hdct.hdct_ngaythue, hdct.hdct_ngayhethan,
                       pct.pct_s_id, pct.pct_dongia, pct.pct_soluong, hdct.hdct_tongtien
                FROM hoadonchothue hdct
                INNER JOIN phieuchothue pct ON hdct.hdct_id = pct.pct_hdct_id
                WHERE hdct.hdct_ngaythue LIKE '{selected_date}%'
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
    mainWindow = HoaDonChoThue()
    mainWindow.show()
    sys.exit(app.exec())
