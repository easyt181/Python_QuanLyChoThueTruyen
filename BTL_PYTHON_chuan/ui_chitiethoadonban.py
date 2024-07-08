# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chitiethoadonban.ui'
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
                           QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QStandardItem)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(684, 462)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 671, 461))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(20)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(21)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Chi ti\u1ebft h\u00f3a \u0111\u01a1n", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"ID H\u00f3a \u0111\u01a1n:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Ng\u00e0y xu\u1ea5t:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Nh\u00e2n vi\u00ean:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"T\u1ed5ng ti\u1ec1n:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Kh\u00e1ch h\u00e0ng:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Tr\u1ea1ng th\u00e1i:", None))
    # retranslateUi
    def setInvoiceDetails(self, details):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["ID", "Sản phẩm", "Đơn giá", "Số lượng", "Thành tiền"])

        for row, detail in enumerate(details):
            for column, item in enumerate(detail):
                model.setItem(row, column, QStandardItem(str(item)))

        self.tableView.setModel(model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
