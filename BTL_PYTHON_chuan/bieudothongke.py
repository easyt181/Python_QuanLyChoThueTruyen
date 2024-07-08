import sys
from PySide6.QtWidgets import *
from PySide6.QtCharts import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import mysql.connector

class BieuDo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Biểu đồ doanh thu theo tháng")
        self.setGeometry(100, 100, 1000, 600)

        # Tạo layout chứa biểu đồ và các thành phần điều khiển
        layout = QVBoxLayout()

        # Tạo view cho biểu đồ QtCharts
        self.chart_view = QChartView()
        layout.addWidget(self.chart_view)

        # Tạo các label để hiển thị thông tin doanh thu
        self.lblTotaldoanhthu = QLabel("Tổng doanh thu:")
        self.lblTotaldoanhthu.setFont(QFont("Arial", 10, QFont.Bold))
        layout.addWidget(self.lblTotaldoanhthu)

        self.lblbanhang = QLabel("Doanh thu bán hàng:")
        self.lblbanhang.setFont(QFont("Arial", 10, QFont.Bold))
        layout.addWidget(self.lblbanhang)

        self.lblthue = QLabel("Doanh thu cho thuê:")
        self.lblthue.setFont(QFont("Arial", 10, QFont.Bold))
        layout.addWidget(self.lblthue)

        self.lblHoantien = QLabel("Tổng tiền hoàn trả:")
        self.lblHoantien.setFont(QFont("Arial", 10, QFont.Bold))
        layout.addWidget(self.lblHoantien)

        # Tạo date edit để chọn tháng
        self.dateEdit = QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setFixedSize(150, 40)
        layout.addWidget(self.dateEdit)

        # Tạo nút Refresh
        self.btnRefresh = QPushButton('Refresh')
        self.btnRefresh.setFixedSize(150, 40)
        layout.addWidget(self.btnRefresh)

        # Thiết lập layout cho cửa sổ chính
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Kết nối sự kiện clicked của nút Refresh với hàm refresh_chart
        self.btnRefresh.clicked.connect(self.refresh_chart)

        # Kết nối sự kiện dateChanged của dateEdit với hàm display_monthly_revenue
        self.dateEdit.dateChanged.connect(self.display_monthly_revenue)

        # Hiển thị biểu đồ ban đầu
        self.refresh_chart()

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

    def calculate_monthly_revenue(self):
        try:
            # Kết nối đến cơ sở dữ liệu
            self.setupDatabaseConnection()

            # Truy vấn tính tổng doanh thu bán hàng theo từng tháng từ các hóa đơn bán hàng
            query_sales = """
                SELECT DATE_FORMAT(HDB_NgayXuat, '%Y-%m') AS month, SUM(HDB_TongTien) AS total_sales_revenue
                FROM hoadonban
                GROUP BY month
            """
            self.db_cursor.execute(query_sales)
            sales_data = self.db_cursor.fetchall()

            # Truy vấn tính tổng doanh thu cho thuê theo từng tháng từ các hóa đơn cho thuê
            query_rentals = """
                SELECT DATE_FORMAT(hdct_ngaythue, '%Y-%m') AS month, SUM(hdct_tongtien) AS total_rental_revenue
                FROM hoadonchothue
                GROUP BY month
            """
            self.db_cursor.execute(query_rentals)
            rental_data = self.db_cursor.fetchall()

            # Truy vấn tính tổng tiền hoàn trả theo từng tháng từ các hóa đơn trả hàng
            query_refunds = """
                SELECT DATE_FORMAT(hdth_ngaytrahang, '%Y-%m') AS month, SUM(hdth_tongtienhoantra) AS total_refund_revenue
                FROM hoadontrahang
                GROUP BY month
            """
            self.db_cursor.execute(query_refunds)
            refund_data = self.db_cursor.fetchall()

            # Đóng kết nối cơ sở dữ liệu
            self.db_cursor.close()
            self.db_connection.close()

            # Chuyển dữ liệu thành từ điển để dễ dàng xử lý
            sales_dict = {row[0]: row[1] for row in sales_data}
            rental_dict = {row[0]: row[1] for row in rental_data}
            refund_dict = {row[0]: row[1] for row in refund_data}

            # Tạo danh sách các tháng có trong dữ liệu
            all_months = set(sales_dict.keys()).union(set(rental_dict.keys())).union(set(refund_dict.keys()))

            # Sắp xếp các tháng theo thứ tự từ trước đến sau
            sorted_months = sorted(all_months)

            # Chuẩn bị dữ liệu cho biểu đồ
            monthly_revenue = []
            for month in sorted_months:
                sales_revenue = sales_dict.get(month, 0)
                rental_revenue = rental_dict.get(month, 0)
                refund_revenue = refund_dict.get(month, 0)
                total_revenue = sales_revenue + rental_revenue - refund_revenue
                monthly_revenue.append((month, sales_revenue, rental_revenue, refund_revenue, total_revenue))

            return monthly_revenue

        except mysql.connector.Error as e:
            print(f"Error calculating revenue: {e}")
            return []

    def display_monthly_revenue(self):
        # Hiển thị thông tin doanh thu cho tháng được chọn từ dateEdit
        selected_date = self.dateEdit.date()
        selected_month = selected_date.toString("yyyy-MM")

        monthly_revenue = self.calculate_monthly_revenue()

        for month, sales_revenue, rental_revenue, refund_revenue, total_revenue in monthly_revenue:
            if month == selected_month:
                self.lblbanhang.setText(f"Doanh thu bán hàng: {sales_revenue}")
                self.lblthue.setText(f"Doanh thu cho thuê: {rental_revenue}")
                self.lblHoantien.setText(f"Tổng tiền hoàn trả: {refund_revenue}")
                self.lblTotaldoanhthu.setText(f"Tổng doanh thu: {total_revenue}")
                return

        # Nếu không tìm thấy tháng được chọn trong dữ liệu
        self.lblbanhang.setText("Doanh thu bán hàng:")
        self.lblthue.setText("Doanh thu cho thuê:")
        self.lblHoantien.setText("Tổng tiền hoàn trả:")
        self.lblTotaldoanhthu.setText("Tổng doanh thu:")

    def refresh_chart(self):
        # Xóa biểu đồ cũ trước khi vẽ biểu đồ mới
        chart = QChart()
        chart.setTitle("Thống kê doanh thu theo tháng")

        # Tính toán và hiển thị biểu đồ
        self.display_monthly_revenue()

        monthly_revenue = self.calculate_monthly_revenue()

        categories = [month for month, _, _, _, _ in monthly_revenue]
        sales_revenue = [sales for _, sales, _, _, _ in monthly_revenue]
        rental_revenue = [rentals for _, _, rentals, _, _ in monthly_revenue]
        refund_revenue = [refunds for _, _, _, refunds, _ in monthly_revenue]
        total_revenue = [total for _, _, _, _, total in monthly_revenue]

        set_sales = QBarSet("Doanh thu bán hàng")
        set_rentals = QBarSet("Doanh thu cho thuê")
        set_refunds = QBarSet("Tổng tiền hoàn trả")

        set_sales.append(sales_revenue)
        set_rentals.append(rental_revenue)
        set_refunds.append(refund_revenue)

        series = QBarSeries()
        series.append(set_sales)
        series.append(set_rentals)
        series.append(set_refunds)

        chart.addSeries(series)

        # Thêm trục X với các tháng
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        # Tìm giá trị lớn nhất của tổng doanh thu để đặt giới hạn cho trục Y
        max_total_revenue = max(total_revenue) if total_revenue else 0

        axisY = QValueAxis()
        axisY.setLabelFormat("%i")
        axisY.setRange(0, float(max_total_revenue) * 4)  # Đặt giới hạn tối đa cho trục Y
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        line_series = QLineSeries()
        line_series.setName("Tổng doanh thu")
        for i, total in enumerate(total_revenue):
            line_series.append(i, total)
        pen = QPen(QColor("red"))
        pen.setWidth(2)
        line_series.setPen(pen)
        chart.addSeries(line_series)
        line_series.attachAxis(axisX)
        line_series.attachAxis(axisY)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.chart_view.setChart(chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
