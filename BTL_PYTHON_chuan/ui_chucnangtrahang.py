# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chucnangtrahang.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_chucnangtrahang(object):
    def setupUi(self, chucnangtrahang):
        if not chucnangtrahang.objectName():
            chucnangtrahang.setObjectName(u"chucnangtrahang")
        chucnangtrahang.resize(913, 567)
        chucnangtrahang.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.layoutWidget = QWidget(chucnangtrahang)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(2, 2, 911, 561))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.layoutWidget)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 4, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnLuu = QPushButton(self.layoutWidget)
        self.btnLuu.setObjectName(u"btnLuu")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(10)
        self.btnLuu.setFont(font)
        self.btnLuu.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius:5px;\n"
"background-color: rgb(0, 170, 0);")

        self.horizontalLayout_3.addWidget(self.btnLuu)

        self.btnInHoaDon = QPushButton(self.layoutWidget)
        self.btnInHoaDon.setObjectName(u"btnInHoaDon")
        self.btnInHoaDon.setFont(font)
        self.btnInHoaDon.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius:5px;\n"
"background-color: rgb(255, 180, 3);")

        self.horizontalLayout_3.addWidget(self.btnInHoaDon)


        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnThem = QPushButton(self.layoutWidget)
        self.btnThem.setObjectName(u"btnThem")
        self.btnThem.setFont(font)
        self.btnThem.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border: 1px solid gray;\n"
"border-radius:5px;")

        self.horizontalLayout_4.addWidget(self.btnThem)

        self.btnXoa = QPushButton(self.layoutWidget)
        self.btnXoa.setObjectName(u"btnXoa")
        self.btnXoa.setFont(font)
        self.btnXoa.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border: 1px solid gray;\n"
"border-radius:5px;\n"
"")

        self.horizontalLayout_4.addWidget(self.btnXoa)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 15, -1, -1)
        self.horizontalSpacer = QSpacerItem(148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(13)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(21, -1, -1, 8)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_3.addWidget(self.label_6)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_6.addWidget(self.label_9)

        self.txtID = QLineEdit(self.layoutWidget)
        self.txtID.setObjectName(u"txtID")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(18)
        sizePolicy.setHeightForWidth(self.txtID.sizePolicy().hasHeightForWidth())
        self.txtID.setSizePolicy(sizePolicy)
        self.txtID.setStyleSheet(u"border: 1px solid gray")

        self.verticalLayout_6.addWidget(self.txtID)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.dateTimeTraHang = QDateTimeEdit(self.layoutWidget)
        self.dateTimeTraHang.setObjectName(u"dateTimeTraHang")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dateTimeTraHang.sizePolicy().hasHeightForWidth())
        self.dateTimeTraHang.setSizePolicy(sizePolicy2)
        self.dateTimeTraHang.setFont(font)
        self.dateTimeTraHang.setStyleSheet(u"border: 1px solid gray")

        self.verticalLayout.addWidget(self.dateTimeTraHang)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.cbbNhanVien = QComboBox(self.layoutWidget)
        self.cbbNhanVien.setObjectName(u"cbbNhanVien")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cbbNhanVien.sizePolicy().hasHeightForWidth())
        self.cbbNhanVien.setSizePolicy(sizePolicy4)
        self.cbbNhanVien.setFont(font)
        self.cbbNhanVien.setStyleSheet(u"border: 1px solid gray")

        self.verticalLayout_2.addWidget(self.cbbNhanVien)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font)

        self.verticalLayout_4.addWidget(self.label_7)

        self.cbbSanPham = QComboBox(self.layoutWidget)
        self.cbbSanPham.setObjectName(u"cbbSanPham")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(20)
        sizePolicy5.setHeightForWidth(self.cbbSanPham.sizePolicy().hasHeightForWidth())
        self.cbbSanPham.setSizePolicy(sizePolicy5)
        self.cbbSanPham.setFont(font)
        self.cbbSanPham.setStyleSheet(u"border: 1px solid gray")

        self.verticalLayout_4.addWidget(self.cbbSanPham)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)

        self.txtSoLuong = QLineEdit(self.layoutWidget)
        self.txtSoLuong.setObjectName(u"txtSoLuong")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.txtSoLuong.sizePolicy().hasHeightForWidth())
        self.txtSoLuong.setSizePolicy(sizePolicy6)
        self.txtSoLuong.setMinimumSize(QSize(0, 20))
        self.txtSoLuong.setStyleSheet(u"border: 1px solid gray")

        self.verticalLayout_7.addWidget(self.txtSoLuong)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)


        self.retranslateUi(chucnangtrahang)

        QMetaObject.connectSlotsByName(chucnangtrahang)
    # setupUi

    def retranslateUi(self, chucnangtrahang):
        chucnangtrahang.setWindowTitle(QCoreApplication.translate("chucnangtrahang", u"Dialog", None))
        self.btnLuu.setText(QCoreApplication.translate("chucnangtrahang", u"X\u00e1c nh\u1eadn tr\u1ea3 h\u00e0ng", None))
        self.btnInHoaDon.setText(QCoreApplication.translate("chucnangtrahang", u"In h\u00f3a \u0111\u01a1n", None))
        self.btnThem.setText(QCoreApplication.translate("chucnangtrahang", u"Th\u00eam", None))
        self.btnXoa.setText(QCoreApplication.translate("chucnangtrahang", u"X\u00f3a", None))
        self.label.setText(QCoreApplication.translate("chucnangtrahang", u"H\u00f3a \u0111\u01a1n tr\u1ea3 h\u00e0ng ", None))
        self.label_2.setText(QCoreApplication.translate("chucnangtrahang", u"ID H\u00f3a \u0111\u01a1n:", None))
        self.label_5.setText(QCoreApplication.translate("chucnangtrahang", u"Kh\u00e1ch h\u00e0ng", None))
        self.label_6.setText(QCoreApplication.translate("chucnangtrahang", u"Nh\u00e2n vi\u00ean b\u00e1n", None))
        self.label_9.setText(QCoreApplication.translate("chucnangtrahang", u"ID H\u00f3a \u0111\u01a1n tr\u1ea3 h\u00e0ng", None))
        self.label_3.setText(QCoreApplication.translate("chucnangtrahang", u"Ng\u00e0y tr\u1ea3 h\u00e0ng", None))
        self.label_4.setText(QCoreApplication.translate("chucnangtrahang", u"Nh\u00e2n vi\u00ean tr\u1ea3 h\u00e0ng", None))
        self.label_7.setText(QCoreApplication.translate("chucnangtrahang", u"S\u00e1ch", None))
        self.label_10.setText(QCoreApplication.translate("chucnangtrahang", u"S\u1ed1 l\u01b0\u1ee3ng", None))
    # retranslateUi

