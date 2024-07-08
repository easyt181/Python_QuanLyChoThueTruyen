from PySide6.QtWidgets import QDialog
from ui_chitiethoadonban import Ui_Dialog

class DetailDialog(QDialog, Ui_Dialog):
    def __init__(self, invoice_data):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Chi tiết hóa đơn")
        self.loadData(invoice_data)

    def loadData(self, invoice_data):
        self.label_2.setText(f"ID Hóa đơn: {invoice_data['hdb_id']}")
        self.label_5.setText(f"Ngày xuất: {invoice_data['hdb_ngayxuat']}")
        self.label_3.setText(f"Nhân viên: {invoice_data['nv_ten']}")
        self.label_6.setText(f"Tổng tiền: {invoice_data['hdb_tongtien']}")
        self.label_4.setText(f"Khách hàng: {invoice_data['hdb_kh_sdt_id']}")
        self.label_7.setText(f"Trạng thái: {'Đã thanh toán' if invoice_data['hdb_trangthai'] == 1 else 'Chưa thanh toán'}")



