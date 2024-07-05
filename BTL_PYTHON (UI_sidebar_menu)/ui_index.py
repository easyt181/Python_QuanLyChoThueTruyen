# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main-ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import new_resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1467, 878)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_menu = QWidget(self.centralwidget)
        self.icon_only_menu.setObjectName(u"icon_only_menu")
        self.icon_only_menu.setEnabled(True)
        self.icon_only_menu.setMaximumSize(QSize(70, 16777215))
        self.icon_only_menu.setStyleSheet(u"QWidget{\n"
"	border:none;\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	box-shadow: 10px 0px 15px rgba(128, 128, 128, 0.5);\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 200, 160);\n"
"\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 200, 160);\n"
"\n"
"border-radius:8px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.icon_only_menu)
        self.verticalLayout_5.setSpacing(45)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 15, -1, 0)
        self.horizontalSpacer_4 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label = QLabel(self.icon_only_menu)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/newPrefix/icons/bookstore.png"))
        self.label.setScaledContents(True)
        self.label.setMargin(-5)
        self.label.setIndent(0)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.icon_only_menu)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/dashboard (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/newPrefix/icons/dashboard (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.icon_only_menu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/add-to-cart (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/newPrefix/icons/add-to-cart (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(30, 30))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.icon_only_menu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/borrow (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/newPrefix/icons/borrow (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(30, 30))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.icon_only_menu)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/open-book (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/newPrefix/icons/open-book (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(30, 30))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.icon_only_menu)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/warehouse (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/newPrefix/icons/warehouse (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(30, 30))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.icon_only_menu)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/bill (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/newPrefix/icons/bill (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(30, 30))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_13 = QPushButton(self.icon_only_menu)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/employee (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/newPrefix/icons/employee (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_13.setIcon(icon6)
        self.pushButton_13.setIconSize(QSize(30, 30))
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.icon_only_menu)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/target (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/newPrefix/icons/public-relation.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_14.setIcon(icon7)
        self.pushButton_14.setIconSize(QSize(30, 30))
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_14)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 255, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_17 = QPushButton(self.icon_only_menu)
        self.pushButton_17.setObjectName(u"pushButton_17")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/icons/setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/newPrefix/icons/setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_17.setIcon(icon8)
        self.pushButton_17.setIconSize(QSize(20, 20))
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.icon_only_menu)
        self.pushButton_18.setObjectName(u"pushButton_18")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/icons/logout (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/newPrefix/icons/logout (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_18.setIcon(icon9)
        self.pushButton_18.setIconSize(QSize(20, 20))
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_18)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.icon_only_menu, 0, 0, 2, 1)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.verticalLayout_7 = QVBoxLayout(self.main)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(220, 220, 220);")

        self.verticalLayout_7.addWidget(self.label_3)


        self.gridLayout.addWidget(self.main, 1, 2, 1, 1)

        self.sibarmenu = QWidget(self.centralwidget)
        self.sibarmenu.setObjectName(u"sibarmenu")
        self.sibarmenu.setMaximumSize(QSize(231, 16777215))
        self.sibarmenu.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	box-shadow: 10px 0px 15px rgba(128, 128, 128, 1);\n"
"}\n"
"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"text-align:left ;\n"
"border:none;\n"
"padding-left:10px;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 200, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 200, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.sibarmenu)
        self.verticalLayout_6.setSpacing(19)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 9, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_5 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.sibarmenu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/icons/bookstore.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(-31)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_6 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_7 = QPushButton(self.sibarmenu)
        self.pushButton_7.setObjectName(u"pushButton_7")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QSize(30, 30))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.sibarmenu)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QSize(30, 30))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.sibarmenu)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QSize(30, 30))
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.sibarmenu)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QSize(30, 30))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.sibarmenu)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font)
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QSize(30, 30))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.sibarmenu)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font)
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setIconSize(QSize(30, 30))
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_12)

        self.pushButton_15 = QPushButton(self.sibarmenu)
        self.pushButton_15.setObjectName(u"pushButton_15")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton_15.setFont(font1)
        self.pushButton_15.setIcon(icon6)
        self.pushButton_15.setIconSize(QSize(30, 30))
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.sibarmenu)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font)
        self.pushButton_16.setIcon(icon7)
        self.pushButton_16.setIconSize(QSize(30, 30))
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_16)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 255, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.pushButton_19 = QPushButton(self.sibarmenu)
        self.pushButton_19.setObjectName(u"pushButton_19")
        font2 = QFont()
        font2.setPointSize(9)
        self.pushButton_19.setFont(font2)
        self.pushButton_19.setIcon(icon8)
        self.pushButton_19.setIconSize(QSize(20, 20))
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.sibarmenu)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setFont(font2)
        self.pushButton_20.setIcon(icon9)
        self.pushButton_20.setIconSize(QSize(20, 20))
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_20)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.sibarmenu, 0, 1, 2, 1)

        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 70))
        self.header.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"}\n"
"QLineEdit{\n"
"padding-left:20px;\n"
"border:1px solid gray;\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_21 = QPushButton(self.header)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMaximumSize(QSize(30, 30))
        self.pushButton_21.setStyleSheet(u"border:none;")
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/icons/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_21.setIcon(icon10)
        self.pushButton_21.setIconSize(QSize(20, 20))
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setAutoExclusive(False)

        self.horizontalLayout_3.addWidget(self.pushButton_21)

        self.horizontalSpacer = QSpacerItem(295, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.header)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 30))
        self.lineEdit.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.pushButton_23 = QPushButton(self.header)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMaximumSize(QSize(50, 50))
        self.pushButton_23.setStyleSheet(u"border:none")
        icon11 = QIcon()
        icon11.addFile(u":/newPrefix/icons/research.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_23.setIcon(icon11)
        self.pushButton_23.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.pushButton_23)

        self.horizontalSpacer_2 = QSpacerItem(215, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_22 = QPushButton(self.header)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMaximumSize(QSize(80, 80))
        self.pushButton_22.setStyleSheet(u"border:none")
        icon12 = QIcon()
        icon12.addFile(u":/newPrefix/icons/profile (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_22.setIcon(icon12)
        self.pushButton_22.setIconSize(QSize(40, 40))
        self.pushButton_22.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton_22)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.header)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift"])
        font3.setPointSize(10)
        self.label_4.setFont(font3)
        self.label_4.setScaledContents(False)

        self.verticalLayout_8.addWidget(self.label_4)

        self.label_5 = QLabel(self.header)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_5.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.header, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_21.toggled.connect(self.icon_only_menu.setHidden)
        self.pushButton_21.toggled.connect(self.sibarmenu.setVisible)
        self.pushButton_14.toggled.connect(self.pushButton_16.setChecked)
        self.pushButton_13.toggled.connect(self.pushButton_15.setChecked)
        self.pushButton_6.toggled.connect(self.pushButton_12.setChecked)
        self.pushButton_5.toggled.connect(self.pushButton_11.setChecked)
        self.pushButton_4.toggled.connect(self.pushButton_10.setChecked)
        self.pushButton_3.toggled.connect(self.pushButton_9.setChecked)
        self.pushButton_2.toggled.connect(self.pushButton_8.setChecked)
        self.pushButton.toggled.connect(self.pushButton_7.setChecked)
        self.pushButton_7.toggled.connect(self.pushButton.setChecked)
        self.pushButton_8.toggled.connect(self.pushButton_2.setChecked)
        self.pushButton_9.toggled.connect(self.pushButton_3.setChecked)
        self.pushButton_10.toggled.connect(self.pushButton_4.setChecked)
        self.pushButton_11.toggled.connect(self.pushButton_5.setChecked)
        self.pushButton_12.toggled.connect(self.pushButton_6.setChecked)
        self.pushButton_15.toggled.connect(self.pushButton_13.setChecked)
        self.pushButton_16.toggled.connect(self.pushButton_14.setChecked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_13.setText("")
        self.pushButton_14.setText("")
        self.pushButton_17.setText("")
        self.pushButton_18.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"  Th\u1ed1ng k\u00ea ", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"  B\u00e1n h\u00e0ng", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"  Qu\u1ea3n l\u00fd thu\u00ea s\u00e1ch", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"  S\u1ea3n ph\u1ea9m", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"  Kho h\u00e0ng", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"  H\u00f3a \u0111\u01a1n", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"  Nh\u00e2n vi\u00ean", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"  Kh\u00e1ch h\u00e0ng", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton_21.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search here...", None))
        self.pushButton_23.setText("")
        self.pushButton_22.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Xin ch\u00e0o!", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ADMIN", None))
    # retranslateUi

