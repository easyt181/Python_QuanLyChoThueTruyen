# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QLHDB.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QWidget)
import new_resource_rc

class Ui_Quanlyhodon(object):
    def setupUi(self, Quanlyhodon):
        if not Quanlyhodon.objectName():
            Quanlyhodon.setObjectName(u"Quanlyhodon")
        Quanlyhodon.resize(1154, 801)
        Quanlyhodon.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(Quanlyhodon)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"padding-bottom: 50px;\n"
"padding-top:20px")
        self.label.setWordWrap(True)
        self.label.setMargin(0)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineSearch = QLineEdit(self.centralwidget)
        self.lineSearch.setObjectName(u"lineSearch")
        self.lineSearch.setMaximumSize(QSize(16777215, 40))
        self.lineSearch.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.lineSearch)

        self.spacer = QSpacerItem(18, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.spacer)

        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setMinimumSize(QSize(100, 30))
        self.dateTimeEdit.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(10)
        self.dateTimeEdit.setFont(font1)
        self.dateTimeEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray;")

        self.horizontalLayout.addWidget(self.dateTimeEdit)

        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(100, 30))
        self.comboBox.setMaximumSize(QSize(150, 30))
        self.comboBox.setFont(font1)
        self.comboBox.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 1px solid gray")

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalSpacer_3 = QSpacerItem(298, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btnLamMoi = QPushButton(self.centralwidget)
        self.btnLamMoi.setObjectName(u"btnLamMoi")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnLamMoi.sizePolicy().hasHeightForWidth())
        self.btnLamMoi.setSizePolicy(sizePolicy1)
        self.btnLamMoi.setMinimumSize(QSize(70, 40))
        self.btnLamMoi.setFont(font1)
        self.btnLamMoi.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border: none;\n"
"border-radius: 10px;")

        self.horizontalLayout.addWidget(self.btnLamMoi)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(12)
        self.tableWidget.setFont(font2)
        self.tableWidget.setStyleSheet(u"background-color: rgb(245, 245, 245);")

        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)

        Quanlyhodon.setCentralWidget(self.centralwidget)

        self.retranslateUi(Quanlyhodon)

        QMetaObject.connectSlotsByName(Quanlyhodon)
    # setupUi

    def retranslateUi(self, Quanlyhodon):
        Quanlyhodon.setWindowTitle(QCoreApplication.translate("Quanlyhodon", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Quanlyhodon", u"H\u00d3A \u0110\u01a0N B\u00c1N H\u00c0NG", None))
        self.lineSearch.setText("")
        self.lineSearch.setPlaceholderText(QCoreApplication.translate("Quanlyhodon", u"Search here...", None))
        self.btnLamMoi.setText(QCoreApplication.translate("Quanlyhodon", u"L\u00e0m m\u1edbi", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Quanlyhodon", u"ID H\u00f3a \u0111\u01a1n", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Quanlyhodon", u"Nh\u00e2n Vi\u00ean", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Quanlyhodon", u"Kh\u00e1ch H\u00e0ng", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Quanlyhodon", u"Ng\u00e0y Xu\u1ea5t", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Quanlyhodon", u"T\u1ed5ng Ti\u1ec1n", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Quanlyhodon", u"Tr\u1ea1ng Th\u00e1i", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Quanlyhodon", u"Chi Ti\u1ebft", None));
    # retranslateUi

