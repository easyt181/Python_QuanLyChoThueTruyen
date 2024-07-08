import decimal
from datetime import datetime
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QDialog, QHeaderView, QMessageBox
from PySide6.QtCore import Qt, QDateTime
from ui_chucnangtrahang import Ui_chucnangtrahang
import mysql.connector

class ChucNangTraHang(QDialog, Ui_chucnangtrahang):
    def __init__(self, invoice_data):
        super().__init__()
        self.setupUi(self)
        self.db_connection = None
        self.db_cursor = None
        self.setupDatabaseConnection()
        self.setStyleSheet("background-color: white; color: black;")
        self.customizeTableHeader()
        self.setupTxtId(self.txtID)
        self.setupDateTime(self.dateTimeTraHang)
        self.setupCbbNhanVien(self.cbbNhanVien)
        self.setupCbbSach(self.cbbSanPham, invoice_data)
        self.so_lan_doi_tra = {}

        self.hdb_id = f"{invoice_data[0]}"
        print(f"{invoice_data[0]}")
        self.kh_sdt_id = f"Khách hàng: {invoice_data[2]}"

        self.nv_ten = f"Nhân viên bán hàng: {invoice_data[1]}"

        self.label_2.setText(str(self.hdb_id))
        self.label_5.setText(self.kh_sdt_id)
        self.label_6.setText(self.nv_ten)

        self.btnThem.clicked.connect(self.addToTableEdit)
        self.btnXoa.clicked.connect(self.removeSelectedRow)
        self.btnLuu.clicked.connect(self.luuDuLieu)

        self.model = QStandardItemModel()
        self.model.setColumnCount(6)
        self.model.setHorizontalHeaderLabels(["ID Hóa đơn", "Ngày trả hàng", "Nhân viên", "Sách", "Số lượng", "Tổng tiền hoàn trả"])
        self.tableView.setModel(self.model)


        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
    def setupDatabaseConnection(self):
        try:
            self.db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db_nhom7_python"
            )
            self.db_cursor = self.db_connection.cursor()
            print("Kết nối đến cơ sở dữ liệu thành công!")
        except mysql.connector.Error as e:
            print(f"Lỗi kết nối đến cơ sở dữ liệu MySQL: {e}")
    def setupTxtId(self, txtID):
        try:
            if self.db_cursor:
                self.db_cursor.execute("SELECT MAX(hdth_id) FROM hoadontrahang")
                last_id = self.db_cursor.fetchone()[0]

                if last_id is None:
                    new_id = "hdth001"
                else:
                    last_num = int(last_id[4:])
                    new_num = last_num + 1
                    new_id = f"hdth{new_num:03d}"

                txtID.setText(new_id)
            else:
                print("Đối tượng con trỏ cơ sở dữ liệu chưa được khởi tạo.")
        except mysql.connector.Error as e:
            print(f"Lỗi truy vấn id cuối cùng từ cơ sở dữ liệu: {e}")
    def setupDateTime(self, dateTimeTraHang):
        try:
            if self.db_cursor:
                current_datetime = QDateTime.currentDateTime()
                dateTimeTraHang.setDateTime(current_datetime)
            else:
                print("Đối tượng con trỏ cơ sở dữ liệu chưa được khởi tạo.")
        except Exception as e:
            print(f"Lỗi thiết lập datetime: {e}")
    def setupCbbNhanVien(self, cbbNhanVien):
        try:
            if self.db_cursor:
                query = "SELECT nv_id, nv_ten FROM nhanvien"
                self.db_cursor.execute(query)
                nhan_vien_list = self.db_cursor.fetchall()
                for nv_id, nv_ten in nhan_vien_list:
                    cbbNhanVien.addItem(f"{nv_ten}", nv_id)
            else:
                print("Đối tượng con trỏ cơ sở dữ liệu chưa được khởi tạo.")
        except mysql.connector.Error as e:
            print(f"Lỗi truy vấn danh sách nhân viên từ cơ sở dữ liệu: {e}")

    def setupCbbSach(self, comboBox_2, invoice_data):
        try:
            if self.db_cursor:
                hdb_id = invoice_data[0]  # Lấy hdb_id từ invoice_data

                query = """
                SELECT sach.s_id, sach.s_tensach 
                FROM sach 
                JOIN chitiethoadon ON sach.s_id = chitiethoadon.cthd_s_id 
                WHERE chitiethoadon.cthd_hdb_id = %s
                """
                self.db_cursor.execute(query, (hdb_id,))
                sach_list = self.db_cursor.fetchall()
                for s_id, s_tensach in sach_list:
                    comboBox_2.addItem(f"{s_tensach}", s_id)
            else:
                print("Đối tượng con trỏ cơ sở dữ liệu chưa được khởi tạo.")
        except mysql.connector.Error as e:
            print(f"Lỗi truy vấn danh sách sách từ cơ sở dữ liệu: {e}")

    def addToTableEdit(self):
        try:
            if self.db_cursor:
                txtID_value = self.txtID.text()
                dateTime_value = self.dateTimeTraHang.dateTime().toString("yyyy-MM-dd HH:mm:ss")
                cbbNhanVien_value = self.cbbNhanVien.currentData()
                comboBox_2_value = self.cbbSanPham.currentData()
                txtSoLuong_value = self.txtSoLuong.text()

                # Truy vấn giá của sách từ cơ sở dữ liệu
                query = "SELECT s_gia FROM sach WHERE s_id = %s"
                self.db_cursor.execute(query, (comboBox_2_value,))
                sach_gia = self.db_cursor.fetchone()[0]

                # Tính tổng tiền hoàn trả
                tong_tien = int(txtSoLuong_value) * sach_gia

                # Thêm dữ liệu vào mô hình
                self.model.appendRow([
                    QStandardItem(txtID_value),
                    QStandardItem(dateTime_value),
                    QStandardItem(str(cbbNhanVien_value)),
                    QStandardItem(str(comboBox_2_value)),
                    QStandardItem(txtSoLuong_value),
                    QStandardItem(str(tong_tien))
                ])

                # Gọi phương thức traHang với cthd_id tương ứng
                cthd_id_to_return = comboBox_2_value  # Lấy cthd_id từ comboBox_2_value
                self.traHang(cthd_id_to_return)

            else:
                print("Đối tượng con trỏ cơ sở dữ liệu chưa được khởi tạo.")
        except Exception as e:
            print(f"Lỗi khi thêm vào bảng: {e}")

    def traHang(self, cthd_id):
        try:
            if self.db_cursor:
                if cthd_id in self.so_lan_doi_tra:
                    if self.so_lan_doi_tra[cthd_id] > 0:
                        self.so_lan_doi_tra[cthd_id] -= 1
                        print(f"Đã đổi trả sách có ID {cthd_id}, còn lại {self.so_lan_doi_tra[cthd_id]} lần đổi trả.")
                    else:
                        print(f"Sách có ID {cthd_id} đã hết lượt đổi trả.")
                else:
                    print(f"Không tìm thấy sách có ID {cthd_id} trong hóa đơn.")
            else:
                print("Đối tượng con trỏ cơ sở dữ liệu chưa được khởi tạo.")
        except Exception as e:
            print(f"Lỗi khi thực hiện đổi trả sách: {e}")
    def removeSelectedRow(self):
        try:
            selected_index = self.tableView.selectedIndexes()
            if selected_index:
                row_index = selected_index[0].row()
                self.model.removeRow(row_index)
            else:
                print("Không có dòng nào được chọn.")
        except Exception as e:
            print(f"Lỗi khi xóa dòng: {e}")
    def luuDuLieu(self, invoice_data):
        if not self.db_cursor:
            print("Đối tượng con trỏ cơ sở dữ liệu chưa được khởi tạo.")
            return
        hdb_id = self.hdb_id

        try:
            for row in range(self.model.rowCount()):
                hdth_id = str(self.model.item(row, 0).text())
                ngay_trahang_str = self.model.item(row, 1).text()
                nv_id = self.model.item(row, 2).text()
                sp_id = self.model.item(row, 3).text()
                so_luong = int(self.model.item(row, 4).text())
                tong_tien_str = self.model.item(row, 5).text()
                tong_tien = decimal.Decimal(tong_tien_str).quantize(decimal.Decimal('0.01'))

                # Chuyển đổi chuỗi ngày giờ thành datetime
                ngay_trahang = datetime.strptime(ngay_trahang_str, '%Y-%m-%d %H:%M:%S')

                insert_query = "INSERT INTO hoadontrahang (hdth_id, hdth_hdb_id, hdth_nv_id, hdth_ngaytrahang, hdth_tongtienhoantra) " \
                               "VALUES (%s, %s, %s, %s, %s)"
                self.db_cursor.execute(insert_query, (hdth_id, hdb_id, nv_id, ngay_trahang, tong_tien))
            self.updateSachSoLuong()
            self.db_connection.commit()
            self.closeDatabaseConnection()
            QMessageBox.information(self, "Thông báo", "Thêm dữ liệu thành công vào bảng!")
        except Exception as e:
            print(f"Lỗi khi lưu dữ liệu vào cơ sở dữ liệu: {e}")
    def updateSachSoLuong(self):
        try:
            for row in range(self.model.rowCount()):
                sp_id = self.model.item(row, 3).text()
                so_luong = int(self.model.item(row, 4).text())

                # Truy vấn số lượng hiện tại của sách từ bảng sach
                query_select_soluong = "SELECT s_soluong FROM sach WHERE s_id = %s"
                self.db_cursor.execute(query_select_soluong, (sp_id,))
                current_so_luong = self.db_cursor.fetchone()[0]

                # Cập nhật số lượng mới của sách
                new_so_luong = int(current_so_luong + so_luong)

                # Update vào bảng sach
                query_update_soluong = "UPDATE sach SET s_soluong = %s WHERE s_id = %s"
                self.db_cursor.execute(query_update_soluong, (new_so_luong, sp_id))

            self.db_connection.commit()
            print("Đã cập nhật số lượng sách thành công trong bảng sach.")
        except Exception as e:
            print(f"Lỗi khi cập nhật số lượng sách: {e}")
    def customizeTableHeader(self):
        header = self.tableView.horizontalHeader()
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
    def closeDatabaseConnection(self):
        try:
            if self.db_cursor:
                self.db_cursor.close()
            if self.db_connection:
                self.db_connection.close()
            print("Đóng kết nối cơ sở dữ liệu.")
        except Exception as e:
            print(f"Lỗi khi đóng kết nối cơ sở dữ liệu: {e}")

