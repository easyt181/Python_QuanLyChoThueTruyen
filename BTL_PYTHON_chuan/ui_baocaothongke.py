# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BaoCaoThongKe.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import new_resource_rc

class Ui_ThongKe(object):
    def setupUi(self, ThongKe):
        if not ThongKe.objectName():
            ThongKe.setObjectName(u"ThongKe")
        ThongKe.resize(1154, 864)
        self.centralwidget = QWidget(ThongKe)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"padding-top: 10px;")

        self.verticalLayout.addWidget(self.label_4)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(0, 35))
        self.widget_2.setMaximumSize(QSize(16777215, 100))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	background-color: rgb(255, 170, 127);\n"
"}\n"
"QWidget{\n"
"background-color: rgb(255, 170, 127);\n"
"}\n"
"")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_5 = QPushButton(self.widget_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(12)
        self.pushButton_5.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/books.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_11.addWidget(self.pushButton_5)

        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(14)
        self.label_9.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_9)


        self.horizontalLayout_10.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	background-color: rgb(255, 170, 127);\n"
"}\n"
"QWidget{\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_6 = QPushButton(self.widget_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/bill (3).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.horizontalLayout_12.addWidget(self.pushButton_6)

        self.label_10 = QLabel(self.widget_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_10)


        self.horizontalLayout_10.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_2)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	\n"
"}\n"
"QWidget{\n"
"background-color: rgb(255, 234, 110);\n"
"}\n"
"")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_7 = QPushButton(self.widget_10)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/invoice.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QSize(30, 30))

        self.horizontalLayout_13.addWidget(self.pushButton_7)

        self.label_11 = QLabel(self.widget_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.horizontalLayout_13.addWidget(self.label_11)


        self.horizontalLayout_10.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_2)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	\n"
"}\n"
"QWidget{\n"
"background-color: rgb(43, 190, 17);\n"
"}\n"
"")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_8 = QPushButton(self.widget_11)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/reading-book.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(30, 30))

        self.horizontalLayout_14.addWidget(self.pushButton_8)

        self.label_12 = QLabel(self.widget_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.horizontalLayout_14.addWidget(self.label_12)


        self.horizontalLayout_10.addWidget(self.widget_11)


        self.verticalLayout.addWidget(self.widget_2)

        self.dothi_2 = QWidget(self.centralwidget)
        self.dothi_2.setObjectName(u"dothi_2")
        self.dothi_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.verticalLayout_12 = QVBoxLayout(self.dothi_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")

        self.verticalLayout_12.addLayout(self.verticalLayout_13)


        self.verticalLayout.addWidget(self.dothi_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        ThongKe.setCentralWidget(self.centralwidget)

        self.retranslateUi(ThongKe)

        QMetaObject.connectSlotsByName(ThongKe)
    # setupUi

    def retranslateUi(self, ThongKe):
        ThongKe.setWindowTitle(QCoreApplication.translate("ThongKe", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("ThongKe", u"TH\u1ed0NG K\u00ca H\u00d4M NAY", None))
        self.pushButton_5.setText(QCoreApplication.translate("ThongKe", u"Truy\u1ec7n", None))
        self.label_9.setText(QCoreApplication.translate("ThongKe", u"TextLabel", None))
        self.pushButton_6.setText(QCoreApplication.translate("ThongKe", u"H\u00f3a \u0111\u01a1n b\u00e1n ", None))
        self.label_10.setText(QCoreApplication.translate("ThongKe", u"TextLabel", None))
        self.pushButton_7.setText(QCoreApplication.translate("ThongKe", u"H\u00f3a \u0111\u01a1n nh\u1eadp", None))
        self.label_11.setText(QCoreApplication.translate("ThongKe", u"TextLabel", None))
        self.pushButton_8.setText(QCoreApplication.translate("ThongKe", u"Thu\u00ea truy\u1ec7n", None))
        self.label_12.setText(QCoreApplication.translate("ThongKe", u"TextLabel", None))
    # retranslateUi

