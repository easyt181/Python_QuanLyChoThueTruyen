from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui_chitiethoadonban import Ui_Dialog
from chucnangtrahang import ChucNangTraHang

import mysql.connector
from UI_hdb import Ui_Quanlyhodon


class HoaDonBan(QMainWindow, Ui_Quanlyhodon):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quản lý cửa hàng truyện")
        self.setupDatabaseConnection()
        self.loadInvoiceData()
        self.setupSearchFilters()
        self.customizeTableHeader()
        self.selected_employee = None

        # Kết nối sự kiện returnPressed của lineSearch với hàm searchInLineEdit
        self.lineSearch.returnPressed.connect(self.searchInLineEdit)

        # Kết nối sự kiện dateTimeChanged của dateTimeEdit với hàm searchByDate
        self.dateTimeEdit.dateTimeChanged.connect(self.searchByDate)

        # Kết nối sự kiện currentIndexChanged của comboBox với hàm searchInComboBox
        self.comboBox.currentIndexChanged.connect(self.searchInComboBox)

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
                SELECT hdb.hdb_id, nv.nv_ten, hdb.hdb_kh_sdt_id, hdb.hdb_ngayxuat, hdb.hdb_tongtien, hdb.hdb_trangthai
                FROM hoadonban hdb
                INNER JOIN nhanvien nv ON hdb.hdb_nv_id = nv.nv_id
            """
            self.db_cursor.execute(query)
            invoices = self.db_cursor.fetchall()

            self.tableWidget.setRowCount(len(invoices))
            for row_index, invoice in enumerate(invoices):
                for col_index in range(len(invoice)):
                    item = QTableWidgetItem(str(invoice[col_index]))
                    if col_index == 5:
                        item.setText("Đã thanh toán" if invoice[col_index] == 1 else "Chưa thanh toán")
                    self.tableWidget.setItem(row_index, col_index, item)

                button_widget = QWidget()
                layout = QHBoxLayout(button_widget)
                detail_button = QPushButton("Chi tiết")
                detail_button.setStyleSheet("background-color: #8B4513; color: white;")
                detail_button.clicked.connect(lambda checked, idx=row_index: self.showDetail(invoices[idx][0]))
                return_button = QPushButton("Trả hàng")
                return_button.setStyleSheet("background-color: #228B22; color: white;")
                return_button.clicked.connect(lambda checked, idx=row_index: self.returnItem(invoices[idx][0]))
                layout.addWidget(detail_button)
                layout.addWidget(return_button)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setAlignment(Qt.AlignCenter)
                self.tableWidget.setCellWidget(row_index, len(invoice), button_widget)

            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)

        except mysql.connector.Error as e:
            print(f"Error loading invoice data: {e}")

    def setupSearchFilters(self):
        self.comboBox.clear()
        self.comboBox.addItem("Tất cả nhân viên")
        try:
            query = "SELECT nv_ten FROM nhanvien"
            self.db_cursor.execute(query)
            employees = self.db_cursor.fetchall()
            for employee in employees:
                self.comboBox.addItem(employee[0])
        except mysql.connector.Error as e:
            print(f"Lỗi khi tải danh sách nhân viên: {e}")

    def searchInLineEdit(self):
        search_text = self.lineSearch.text().strip()
        if not search_text:
            if self.selected_employee:
                self.searchInComboBox(self.comboBox.currentIndex())
            else:
                self.loadInvoiceData()
            return

        try:
            if self.selected_employee:
                query = (
                    "SELECT hdb.hdb_id, nv.nv_ten, hdb.hdb_kh_sdt_id, hdb.hdb_ngayxuat, hdb.hdb_tongtien, hdb.hdb_trangthai "
                    "FROM hoadonban hdb "
                    "INNER JOIN nhanvien nv ON hdb.hdb_nv_id = nv.nv_id "
                    f"WHERE (nv.nv_ten = '{self.selected_employee}') AND "
                    f"(hdb.hdb_id LIKE '%{search_text}%' OR "
                    f"nv.nv_ten LIKE '%{search_text}%' OR "
                    f"hdb.hdb_kh_sdt_id LIKE '%{search_text}%' OR "
                    f"hdb.hdb_ngayxuat LIKE '%{search_text}%' OR "
                    f"hdb.hdb_tongtien LIKE '%{search_text}%')"
                )
            else:
                query = (
                    "SELECT hdb.hdb_id, nv.nv_ten, hdb.hdb_kh_sdt_id, hdb.hdb_ngayxuat, hdb.hdb_tongtien, hdb.hdb_trangthai "
                    "FROM hoadonban hdb "
                    "INNER JOIN nhanvien nv ON hdb.hdb_nv_id = nv.nv_id "
                    f"WHERE (hdb.hdb_id LIKE '%{search_text}%' OR "
                    f"nv.nv_ten LIKE '%{search_text}%' OR "
                    f"hdb.hdb_kh_sdt_id LIKE '%{search_text}%' OR "
                    f"hdb.hdb_ngayxuat LIKE '%{search_text}%' OR "
                    f"hdb.hdb_tongtien LIKE '%{search_text}%')"
                )

            self.db_cursor.execute(query)
            invoices = self.db_cursor.fetchall()

            self.tableWidget.setRowCount(len(invoices))
            for row_index, invoice in enumerate(invoices):
                for col_index in range(len(invoice)):
                    item = QTableWidgetItem(str(invoice[col_index]))
                    if col_index == 5:  # Cột hdb_trangthai
                        item.setText("Đã thanh toán" if invoice[col_index] == 1 else "Chưa thanh toán")
                    self.tableWidget.setItem(row_index, col_index, item)
                    button_widget = QWidget()
                    layout = QHBoxLayout(button_widget)
                    detail_button = QPushButton("Chi tiết")
                    detail_button.setStyleSheet("background-color: #8B4513; color: white;")
                    detail_button.clicked.connect(lambda checked, idx=row_index: self.showDetail(invoices[idx][0]))
                    return_button = QPushButton("Trả hàng")
                    return_button.setStyleSheet("background-color: #228B22; color: white;")
                    return_button.clicked.connect(lambda checked, idx=row_index: self.returnItem(invoices[idx][0]))
                    layout.addWidget(detail_button)
                    layout.addWidget(return_button)
                    layout.setContentsMargins(0, 0, 0, 0)
                    layout.setAlignment(Qt.AlignCenter)
                    self.tableWidget.setCellWidget(row_index, len(invoice), button_widget)
        except mysql.connector.Error as e:
            print(f"Lỗi khi tìm kiếm hóa đơn: {e}")

    def searchByDate(self, dateTime):
        selected_date = dateTime.toString("yyyy-MM-dd")

        try:
            query = f"SELECT hdb.hdb_id, nv.nv_ten, hdb.hdb_kh_sdt_id, hdb.hdb_ngayxuat, hdb.hdb_tongtien, hdb.hdb_trangthai FROM hoadonban hdb INNER JOIN nhanvien nv ON hdb.hdb_nv_id = nv.nv_id WHERE hdb.hdb_ngayxuat LIKE '{selected_date}%'"
            self.db_cursor.execute(query)
            invoices = self.db_cursor.fetchall()

            self.tableWidget.setRowCount(len(invoices))
            for row_index, invoice in enumerate(invoices):
                for col_index in range(len(invoice)):
                    item = QTableWidgetItem(str(invoice[col_index]))
                    if col_index == 5:  # Cột hdb_trangthai
                        item.setText("Đã thanh toán" if invoice[col_index] == 1 else "Chưa thanh toán")
                    self.tableWidget.setItem(row_index, col_index, item)
                    button_widget = QWidget()
                    layout = QHBoxLayout(button_widget)
                    detail_button = QPushButton("Chi tiết")
                    detail_button.setStyleSheet("background-color: #8B4513; color: white;")
                    detail_button.clicked.connect(lambda checked, idx=row_index: self.showDetail(invoices[idx][0]))
                    return_button = QPushButton("Trả hàng")
                    return_button.setStyleSheet("background-color: #228B22; color: white;")
                    return_button.clicked.connect(lambda checked, idx=row_index: self.returnItem(invoices[idx][0]))
                    layout.addWidget(detail_button)
                    layout.addWidget(return_button)
                    layout.setContentsMargins(0, 0, 0, 0)
                    layout.setAlignment(Qt.AlignCenter)
                    self.tableWidget.setCellWidget(row_index, len(invoice), button_widget)


        except mysql.connector.Error as e:
            print(f"Lỗi khi tìm kiếm hóa đơn theo ngày xuất: {e}")

    def searchInComboBox(self, index):
        if index == 0:
            self.selected_employee = None
            self.loadInvoiceData()
        else:
            self.selected_employee = self.comboBox.currentText()
            try:
                query = (
                    "SELECT hdb.hdb_id, nv.nv_ten, hdb.hdb_kh_sdt_id, hdb.hdb_ngayxuat, hdb.hdb_tongtien, hdb.hdb_trangthai "
                    "FROM hoadonban hdb "
                    "INNER JOIN nhanvien nv ON hdb.hdb_nv_id = nv.nv_id "
                    f"WHERE nv.nv_ten = '{self.selected_employee}'"
                )
                self.db_cursor.execute(query)
                invoices = self.db_cursor.fetchall()

                self.tableWidget.setRowCount(len(invoices))
                for row_index, invoice in enumerate(invoices):
                    for col_index in range(len(invoice)):
                        item = QTableWidgetItem(str(invoice[col_index]))
                        if col_index == 5:
                            item.setText("Đã thanh toán" if invoice[col_index] == 1 else "Chưa thanh toán")
                        self.tableWidget.setItem(row_index, col_index, item)
                        button_widget = QWidget()
                        layout = QHBoxLayout(button_widget)
                        detail_button = QPushButton("Chi tiết")
                        detail_button.setStyleSheet("background-color: #8B4513; color: white;")
                        detail_button.clicked.connect(lambda checked, idx=row_index: self.showDetail(invoices[idx][0]))
                        return_button = QPushButton("Trả hàng")
                        return_button.setStyleSheet("background-color: #228B22; color: white;")
                        return_button.clicked.connect(lambda checked, idx=row_index: self.returnItem(invoices[idx][0]))
                        layout.addWidget(detail_button)
                        layout.addWidget(return_button)
                        layout.setContentsMargins(0, 0, 0, 0)
                        layout.setAlignment(Qt.AlignCenter)
                        self.tableWidget.setCellWidget(row_index, len(invoice), button_widget)
            except mysql.connector.Error as e:
                print(f"Lỗi khi tìm kiếm hóa đơn theo nhân viên: {e}")

    def refreshTable(self):
        self.lineSearch.clear()
        self.comboBox.setCurrentIndex(0)
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.loadInvoiceData()

    def showMessageBox(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec()

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

    def showDetail(self, hdb_id):
        try:

            query_invoice = (
                "SELECT hdb.hdb_id, nv.nv_ten, hdb.hdb_kh_sdt_id, hdb.hdb_ngayxuat, hdb.hdb_tongtien, hdb.hdb_trangthai "
                "FROM hoadonban hdb "
                "INNER JOIN nhanvien nv ON hdb.hdb_nv_id = nv.nv_id "
                f"WHERE hdb.hdb_id = '{hdb_id}'"
            )

            self.db_cursor.execute(query_invoice)
            invoice_data = self.db_cursor.fetchone()


            query_detail = (
                "SELECT cthd.cthd_id, s.s_tensach, cthd.cthd_dongia, cthd.cthd_soluong, cthd.cthd_thanhtien "
                "FROM chitiethoadon cthd "
                "INNER JOIN sach s ON cthd.cthd_s_id = s.s_id "
                f"WHERE cthd.cthd_hdb_id = '{hdb_id}'"
            )

            self.db_cursor.execute(query_detail)
            details = self.db_cursor.fetchall()

            dialog = QDialog()
            ui = Ui_Dialog()
            ui.setupUi(dialog)

            ui.label.setText(f"Chi tiết hóa đơn")
            ui.label_2.setText(f"ID Hóa đơn: {invoice_data[0]}")
            ui.label_5.setText(f"Ngày xuất: {invoice_data[3].strftime('%d/%m/%Y')}")
            ui.label_3.setText(f"Nhân viên: {invoice_data[1]}")
            ui.label_4.setText(f"Tổng tiền: {invoice_data[4]}")
            ui.label_6.setText(f"Khách hàng: {invoice_data[2]}")
            ui.label_7.setText(f"Trạng thái: {'Đã thanh toán' if invoice_data[5] == 1 else 'Chưa thanh toán'}")


            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(["ID", "Tên sản phẩm", "Đơn giá", "Số lượng", "Thành tiền"])

            for row, detail in enumerate(details):
                for column, item in enumerate(detail):
                    model.setItem(row, column, QStandardItem(str(item)))

            ui.tableView.setModel(model)
            ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            ui.tableView.horizontalHeader().setStretchLastSection(True)

            # Thiết lập nền của dialog là màu trắng và chữ là màu đen
            pal = dialog.palette()
            pal.setColor(QPalette.Window, QColor(Qt.white))
            pal.setColor(QPalette.WindowText, QColor(Qt.black))
            dialog.setPalette(pal)

            dialog.exec_()

        except mysql.connector.Error as e:
            print(f"Lỗi khi hiển thị chi tiết hóa đơn: {e}")
    def returnItem(self, hdb_id):
        query_invoice = (
            "SELECT hdb.hdb_id, nv.nv_ten, hdb.hdb_kh_sdt_id, hdb.hdb_ngayxuat, hdb.hdb_tongtien, hdb.hdb_trangthai "
            "FROM hoadonban hdb "
            "INNER JOIN nhanvien nv ON hdb.hdb_nv_id = nv.nv_id "
            f"WHERE hdb.hdb_id = '{hdb_id}'"
        )

        self.db_cursor.execute(query_invoice)
        invoice_data = self.db_cursor.fetchone()

        self.return_window = ChucNangTraHang(invoice_data)
        self.return_window.show()

