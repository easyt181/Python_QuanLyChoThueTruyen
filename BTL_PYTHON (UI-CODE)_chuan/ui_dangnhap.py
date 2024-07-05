# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DangNhap.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
import new_resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(707, 406)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QTextEdit{\n"
"border: 1px solid gray\n"
"}")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 301, 411))
        self.widget.setStyleSheet(u"background-color: rgb(255, 170, 127);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 40, 261, 311))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u":/newPrefix/icons/1.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setMargin(0)
        self.label_2.setIndent(0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(300, 0, 411, 411))
        self.txtTaiKhoan = QTextEdit(self.widget_2)
        self.txtTaiKhoan.setObjectName(u"txtTaiKhoan")
        self.txtTaiKhoan.setGeometry(QRect(110, 130, 281, 31))
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 50, 221, 61))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 120, 40, 40))
        self.label_3.setPixmap(QPixmap(u":/newPrefix/icons/user.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 190, 40, 40))
        self.label_4.setPixmap(QPixmap(u":/newPrefix/icons/padlock.png"))
        self.label_4.setScaledContents(True)
        self.txtMatKhau = QTextEdit(self.widget_2)
        self.txtMatKhau.setObjectName(u"txtMatKhau")
        self.txtMatKhau.setGeometry(QRect(110, 200, 281, 31))
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 110, 81, 16))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 180, 61, 16))
        self.btnDangNhap = QPushButton(self.widget_2)
        self.btnDangNhap.setObjectName(u"btnDangNhap")
        self.btnDangNhap.setGeometry(QRect(300, 260, 91, 51))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.btnDangNhap.setFont(font2)
        self.btnDangNhap.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border: none;\n"
"border-radius: 10px;")
        self.btnThoat = QPushButton(self.widget_2)
        self.btnThoat.setObjectName(u"btnThoat")
        self.btnThoat.setGeometry(QRect(110, 260, 91, 51))
        self.btnThoat.setFont(font2)
        self.btnThoat.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 10px;\n"
"border: none;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0102NG NH\u1eacP", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"T\u00e0i kho\u1ea3n ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"M\u1eadt kh\u1ea9u", None))
        self.btnDangNhap.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng nh\u1eadp", None))
        self.btnThoat.setText(QCoreApplication.translate("MainWindow", u"Tho\u00e1t", None))
    # retranslateUi

