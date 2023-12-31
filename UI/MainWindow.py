# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMaximumSize(QSize(600, 700))
        MainWindow.setStyleSheet(u"background-color: rgb(124, 174, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(204, 213, 211);\n"
"font: 700 24pt \"Segoe Print\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.frame_16 = QFrame(self.frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_16)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(250, 0, -1, 0)
        self.bt_clear = QPushButton(self.frame_16)
        self.bt_clear.setObjectName(u"bt_clear")
        self.bt_clear.setMinimumSize(QSize(100, 0))
        self.bt_clear.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        self.bt_clear.setFont(font1)
        self.bt_clear.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
"font: 700 10pt \"Segoe Print\";\n"
"background-color: rgb(206, 209, 221);\n"
"border: 2px solid rgb(130, 136, 255);\n"
"color: rgb(130, 136, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-radius: 6px;\n"
"font: 700 10pt \"Segoe Print\";\n"
"background-color: rgb(209, 209, 209);\n"
"border: 2px solid rgb(130, 136, 255);\n"
"color: rgb(130, 136, 255);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.bt_clear)


        self.verticalLayout_3.addWidget(self.frame_16)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(105, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(390, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(130, 136, 255);")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(130, 130))
        self.frame_7.setMaximumSize(QSize(130, 130))
        self.frame_7.setStyleSheet(u"border: none;")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_7)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.l1 = QLineEdit(self.frame_7)
        self.l1.setObjectName(u"l1")
        self.l1.setMinimumSize(QSize(41, 41))
        self.l1.setMaximumSize(QSize(41, 41))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.l1.setFont(font2)
        self.l1.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);\n"
"")
        self.l1.setMaxLength(1)
        self.l1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l1, 0, 0, 1, 1)

        self.l2 = QLineEdit(self.frame_7)
        self.l2.setObjectName(u"l2")
        self.l2.setMinimumSize(QSize(41, 41))
        self.l2.setMaximumSize(QSize(41, 41))
        self.l2.setFont(font2)
        self.l2.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);\n"
"")
        self.l2.setMaxLength(1)
        self.l2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l2, 0, 1, 1, 1)

        self.l3 = QLineEdit(self.frame_7)
        self.l3.setObjectName(u"l3")
        self.l3.setMinimumSize(QSize(41, 41))
        self.l3.setMaximumSize(QSize(41, 41))
        self.l3.setFont(font2)
        self.l3.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);\n"
"")
        self.l3.setMaxLength(1)
        self.l3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l3, 0, 2, 1, 1)

        self.l10 = QLineEdit(self.frame_7)
        self.l10.setObjectName(u"l10")
        self.l10.setMinimumSize(QSize(41, 41))
        self.l10.setMaximumSize(QSize(41, 41))
        self.l10.setFont(font2)
        self.l10.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);\n"
"")
        self.l10.setMaxLength(1)
        self.l10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l10, 1, 0, 1, 1)

        self.l11 = QLineEdit(self.frame_7)
        self.l11.setObjectName(u"l11")
        self.l11.setMinimumSize(QSize(41, 41))
        self.l11.setMaximumSize(QSize(41, 41))
        self.l11.setFont(font2)
        self.l11.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);\n"
"")
        self.l11.setMaxLength(1)
        self.l11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l11, 1, 1, 1, 1)

        self.l12 = QLineEdit(self.frame_7)
        self.l12.setObjectName(u"l12")
        self.l12.setMinimumSize(QSize(41, 41))
        self.l12.setMaximumSize(QSize(41, 41))
        self.l12.setFont(font2)
        self.l12.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);\n"
"")
        self.l12.setMaxLength(1)
        self.l12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l12, 1, 2, 1, 1)

        self.l19 = QLineEdit(self.frame_7)
        self.l19.setObjectName(u"l19")
        self.l19.setMinimumSize(QSize(41, 41))
        self.l19.setMaximumSize(QSize(41, 41))
        self.l19.setFont(font2)
        self.l19.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);\n"
"")
        self.l19.setMaxLength(1)
        self.l19.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l19, 2, 0, 1, 1)

        self.l20 = QLineEdit(self.frame_7)
        self.l20.setObjectName(u"l20")
        self.l20.setMinimumSize(QSize(41, 41))
        self.l20.setMaximumSize(QSize(41, 41))
        self.l20.setFont(font2)
        self.l20.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);\n"
"")
        self.l20.setMaxLength(1)
        self.l20.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l20, 2, 1, 1, 1)

        self.l21 = QLineEdit(self.frame_7)
        self.l21.setObjectName(u"l21")
        self.l21.setMinimumSize(QSize(41, 41))
        self.l21.setMaximumSize(QSize(41, 41))
        self.l21.setFont(font2)
        self.l21.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);\n"
"")
        self.l21.setMaxLength(1)
        self.l21.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l21, 2, 2, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(130, 130))
        self.frame_8.setMaximumSize(QSize(130, 130))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_8)
        self.gridLayout_9.setSpacing(1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.l4 = QLineEdit(self.frame_8)
        self.l4.setObjectName(u"l4")
        self.l4.setMinimumSize(QSize(41, 41))
        self.l4.setMaximumSize(QSize(41, 41))
        self.l4.setFont(font2)
        self.l4.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l4.setMaxLength(1)
        self.l4.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.l4, 0, 0, 1, 1)

        self.l5 = QLineEdit(self.frame_8)
        self.l5.setObjectName(u"l5")
        self.l5.setMinimumSize(QSize(41, 41))
        self.l5.setMaximumSize(QSize(41, 41))
        self.l5.setFont(font2)
        self.l5.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l5.setMaxLength(1)
        self.l5.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.l5, 0, 1, 1, 1)

        self.l6 = QLineEdit(self.frame_8)
        self.l6.setObjectName(u"l6")
        self.l6.setMinimumSize(QSize(41, 41))
        self.l6.setMaximumSize(QSize(41, 41))
        self.l6.setFont(font2)
        self.l6.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l6.setMaxLength(1)
        self.l6.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.l6, 0, 2, 1, 1)

        self.l13 = QLineEdit(self.frame_8)
        self.l13.setObjectName(u"l13")
        self.l13.setMinimumSize(QSize(41, 41))
        self.l13.setMaximumSize(QSize(41, 41))
        self.l13.setFont(font2)
        self.l13.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l13.setMaxLength(1)
        self.l13.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.l13, 1, 0, 1, 1)

        self.l14 = QLineEdit(self.frame_8)
        self.l14.setObjectName(u"l14")
        self.l14.setMinimumSize(QSize(41, 41))
        self.l14.setMaximumSize(QSize(41, 41))
        self.l14.setFont(font2)
        self.l14.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l14.setMaxLength(1)
        self.l14.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.l14, 1, 1, 1, 1)

        self.l15 = QLineEdit(self.frame_8)
        self.l15.setObjectName(u"l15")
        self.l15.setMinimumSize(QSize(41, 41))
        self.l15.setMaximumSize(QSize(41, 41))
        self.l15.setFont(font2)
        self.l15.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l15.setMaxLength(1)
        self.l15.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.l15, 1, 2, 1, 1)

        self.l22 = QLineEdit(self.frame_8)
        self.l22.setObjectName(u"l22")
        self.l22.setMinimumSize(QSize(41, 41))
        self.l22.setMaximumSize(QSize(41, 41))
        self.l22.setFont(font2)
        self.l22.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l22.setMaxLength(1)
        self.l22.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.l22, 2, 0, 1, 1)

        self.l23 = QLineEdit(self.frame_8)
        self.l23.setObjectName(u"l23")
        self.l23.setMinimumSize(QSize(41, 41))
        self.l23.setMaximumSize(QSize(41, 41))
        self.l23.setFont(font2)
        self.l23.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l23.setMaxLength(1)
        self.l23.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.l23, 2, 1, 1, 1)

        self.l24 = QLineEdit(self.frame_8)
        self.l24.setObjectName(u"l24")
        self.l24.setMinimumSize(QSize(41, 41))
        self.l24.setMaximumSize(QSize(41, 41))
        self.l24.setFont(font2)
        self.l24.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l24.setMaxLength(1)
        self.l24.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.l24, 2, 2, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(130, 130))
        self.frame_9.setMaximumSize(QSize(130, 130))
        self.frame_9.setStyleSheet(u"border: none;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_9)
        self.gridLayout_4.setSpacing(1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.l7 = QLineEdit(self.frame_9)
        self.l7.setObjectName(u"l7")
        self.l7.setMinimumSize(QSize(41, 41))
        self.l7.setMaximumSize(QSize(41, 41))
        self.l7.setFont(font2)
        self.l7.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l7.setMaxLength(1)
        self.l7.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l7, 0, 0, 1, 1)

        self.l8 = QLineEdit(self.frame_9)
        self.l8.setObjectName(u"l8")
        self.l8.setMinimumSize(QSize(41, 41))
        self.l8.setMaximumSize(QSize(41, 41))
        self.l8.setFont(font2)
        self.l8.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l8.setMaxLength(1)
        self.l8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l8, 0, 1, 1, 1)

        self.l9 = QLineEdit(self.frame_9)
        self.l9.setObjectName(u"l9")
        self.l9.setMinimumSize(QSize(41, 41))
        self.l9.setMaximumSize(QSize(41, 41))
        self.l9.setFont(font2)
        self.l9.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l9.setMaxLength(1)
        self.l9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l9, 0, 2, 1, 1)

        self.l16 = QLineEdit(self.frame_9)
        self.l16.setObjectName(u"l16")
        self.l16.setMinimumSize(QSize(41, 41))
        self.l16.setMaximumSize(QSize(41, 41))
        self.l16.setFont(font2)
        self.l16.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l16.setMaxLength(1)
        self.l16.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l16, 1, 0, 1, 1)

        self.l17 = QLineEdit(self.frame_9)
        self.l17.setObjectName(u"l17")
        self.l17.setMinimumSize(QSize(41, 41))
        self.l17.setMaximumSize(QSize(41, 41))
        self.l17.setFont(font2)
        self.l17.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l17.setMaxLength(1)
        self.l17.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l17, 1, 1, 1, 1)

        self.l18 = QLineEdit(self.frame_9)
        self.l18.setObjectName(u"l18")
        self.l18.setMinimumSize(QSize(41, 41))
        self.l18.setMaximumSize(QSize(41, 41))
        self.l18.setFont(font2)
        self.l18.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l18.setMaxLength(1)
        self.l18.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l18, 1, 2, 1, 1)

        self.l25 = QLineEdit(self.frame_9)
        self.l25.setObjectName(u"l25")
        self.l25.setMinimumSize(QSize(41, 41))
        self.l25.setMaximumSize(QSize(41, 41))
        self.l25.setFont(font2)
        self.l25.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l25.setMaxLength(1)
        self.l25.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l25, 2, 0, 1, 1)

        self.l26 = QLineEdit(self.frame_9)
        self.l26.setObjectName(u"l26")
        self.l26.setMinimumSize(QSize(41, 41))
        self.l26.setMaximumSize(QSize(41, 41))
        self.l26.setFont(font2)
        self.l26.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l26.setMaxLength(1)
        self.l26.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l26, 2, 1, 1, 1)

        self.l27 = QLineEdit(self.frame_9)
        self.l27.setObjectName(u"l27")
        self.l27.setMinimumSize(QSize(41, 41))
        self.l27.setMaximumSize(QSize(41, 41))
        self.l27.setFont(font2)
        self.l27.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l27.setMaxLength(1)
        self.l27.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l27, 2, 2, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(390, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(130, 136, 255);")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(130, 130))
        self.frame_10.setMaximumSize(QSize(130, 130))
        self.frame_10.setStyleSheet(u"border: none;")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_10)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.l28 = QLineEdit(self.frame_10)
        self.l28.setObjectName(u"l28")
        self.l28.setMinimumSize(QSize(41, 41))
        self.l28.setMaximumSize(QSize(41, 41))
        self.l28.setFont(font2)
        self.l28.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l28.setMaxLength(1)
        self.l28.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.l28, 0, 0, 1, 1)

        self.l29 = QLineEdit(self.frame_10)
        self.l29.setObjectName(u"l29")
        self.l29.setMinimumSize(QSize(41, 41))
        self.l29.setMaximumSize(QSize(41, 41))
        self.l29.setFont(font2)
        self.l29.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l29.setMaxLength(1)
        self.l29.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.l29, 0, 1, 1, 1)

        self.l30 = QLineEdit(self.frame_10)
        self.l30.setObjectName(u"l30")
        self.l30.setMinimumSize(QSize(41, 41))
        self.l30.setMaximumSize(QSize(41, 41))
        self.l30.setFont(font2)
        self.l30.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l30.setMaxLength(1)
        self.l30.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.l30, 0, 2, 1, 1)

        self.l37 = QLineEdit(self.frame_10)
        self.l37.setObjectName(u"l37")
        self.l37.setMinimumSize(QSize(41, 41))
        self.l37.setMaximumSize(QSize(41, 41))
        self.l37.setFont(font2)
        self.l37.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l37.setMaxLength(1)
        self.l37.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.l37, 1, 0, 1, 1)

        self.l38 = QLineEdit(self.frame_10)
        self.l38.setObjectName(u"l38")
        self.l38.setMinimumSize(QSize(41, 41))
        self.l38.setMaximumSize(QSize(41, 41))
        self.l38.setFont(font2)
        self.l38.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l38.setMaxLength(1)
        self.l38.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.l38, 1, 1, 1, 1)

        self.l39 = QLineEdit(self.frame_10)
        self.l39.setObjectName(u"l39")
        self.l39.setMinimumSize(QSize(41, 41))
        self.l39.setMaximumSize(QSize(41, 41))
        self.l39.setFont(font2)
        self.l39.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l39.setMaxLength(1)
        self.l39.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.l39, 1, 2, 1, 1)

        self.l46 = QLineEdit(self.frame_10)
        self.l46.setObjectName(u"l46")
        self.l46.setMinimumSize(QSize(41, 41))
        self.l46.setMaximumSize(QSize(41, 41))
        self.l46.setFont(font2)
        self.l46.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l46.setMaxLength(1)
        self.l46.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.l46, 2, 0, 1, 1)

        self.l47 = QLineEdit(self.frame_10)
        self.l47.setObjectName(u"l47")
        self.l47.setMinimumSize(QSize(41, 41))
        self.l47.setMaximumSize(QSize(41, 41))
        self.l47.setFont(font2)
        self.l47.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l47.setMaxLength(1)
        self.l47.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.l47, 2, 1, 1, 1)

        self.l48 = QLineEdit(self.frame_10)
        self.l48.setObjectName(u"l48")
        self.l48.setMinimumSize(QSize(41, 41))
        self.l48.setMaximumSize(QSize(41, 41))
        self.l48.setFont(font2)
        self.l48.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l48.setMaxLength(1)
        self.l48.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.l48, 2, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(130, 130))
        self.frame_11.setMaximumSize(QSize(130, 130))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_11)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.l33 = QLineEdit(self.frame_11)
        self.l33.setObjectName(u"l33")
        self.l33.setMinimumSize(QSize(41, 41))
        self.l33.setMaximumSize(QSize(41, 41))
        self.l33.setFont(font2)
        self.l33.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l33.setMaxLength(1)
        self.l33.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l33, 0, 2, 1, 1)

        self.l32 = QLineEdit(self.frame_11)
        self.l32.setObjectName(u"l32")
        self.l32.setMinimumSize(QSize(41, 41))
        self.l32.setMaximumSize(QSize(41, 41))
        self.l32.setFont(font2)
        self.l32.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l32.setMaxLength(1)
        self.l32.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l32, 0, 1, 1, 1)

        self.l50 = QLineEdit(self.frame_11)
        self.l50.setObjectName(u"l50")
        self.l50.setMinimumSize(QSize(41, 41))
        self.l50.setMaximumSize(QSize(41, 41))
        self.l50.setFont(font2)
        self.l50.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l50.setMaxLength(1)
        self.l50.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l50, 2, 1, 1, 1)

        self.l42 = QLineEdit(self.frame_11)
        self.l42.setObjectName(u"l42")
        self.l42.setMinimumSize(QSize(41, 41))
        self.l42.setMaximumSize(QSize(41, 41))
        self.l42.setFont(font2)
        self.l42.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l42.setMaxLength(1)
        self.l42.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l42, 1, 2, 1, 1)

        self.l40 = QLineEdit(self.frame_11)
        self.l40.setObjectName(u"l40")
        self.l40.setMinimumSize(QSize(41, 41))
        self.l40.setMaximumSize(QSize(41, 41))
        self.l40.setFont(font2)
        self.l40.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l40.setMaxLength(1)
        self.l40.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l40, 1, 0, 1, 1)

        self.l49 = QLineEdit(self.frame_11)
        self.l49.setObjectName(u"l49")
        self.l49.setMinimumSize(QSize(41, 41))
        self.l49.setMaximumSize(QSize(41, 41))
        self.l49.setFont(font2)
        self.l49.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l49.setMaxLength(1)
        self.l49.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l49, 2, 0, 1, 1)

        self.l41 = QLineEdit(self.frame_11)
        self.l41.setObjectName(u"l41")
        self.l41.setMinimumSize(QSize(41, 41))
        self.l41.setMaximumSize(QSize(41, 41))
        self.l41.setFont(font2)
        self.l41.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l41.setMaxLength(1)
        self.l41.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l41, 1, 1, 1, 1)

        self.l31 = QLineEdit(self.frame_11)
        self.l31.setObjectName(u"l31")
        self.l31.setMinimumSize(QSize(41, 41))
        self.l31.setMaximumSize(QSize(41, 41))
        self.l31.setFont(font2)
        self.l31.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l31.setMaxLength(1)
        self.l31.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l31, 0, 0, 1, 1)

        self.l51 = QLineEdit(self.frame_11)
        self.l51.setObjectName(u"l51")
        self.l51.setMinimumSize(QSize(41, 41))
        self.l51.setMaximumSize(QSize(41, 41))
        self.l51.setFont(font2)
        self.l51.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l51.setMaxLength(1)
        self.l51.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l51, 2, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(130, 130))
        self.frame_12.setMaximumSize(QSize(130, 130))
        self.frame_12.setStyleSheet(u"border: none;")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_12)
        self.gridLayout_6.setSpacing(1)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.l34 = QLineEdit(self.frame_12)
        self.l34.setObjectName(u"l34")
        self.l34.setMinimumSize(QSize(41, 41))
        self.l34.setMaximumSize(QSize(41, 41))
        self.l34.setFont(font2)
        self.l34.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l34.setMaxLength(1)
        self.l34.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.l34, 0, 0, 1, 1)

        self.l35 = QLineEdit(self.frame_12)
        self.l35.setObjectName(u"l35")
        self.l35.setMinimumSize(QSize(41, 41))
        self.l35.setMaximumSize(QSize(41, 41))
        self.l35.setFont(font2)
        self.l35.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l35.setMaxLength(1)
        self.l35.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.l35, 0, 1, 1, 1)

        self.l36 = QLineEdit(self.frame_12)
        self.l36.setObjectName(u"l36")
        self.l36.setMinimumSize(QSize(41, 41))
        self.l36.setMaximumSize(QSize(41, 41))
        self.l36.setFont(font2)
        self.l36.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l36.setMaxLength(1)
        self.l36.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.l36, 0, 2, 1, 1)

        self.l43 = QLineEdit(self.frame_12)
        self.l43.setObjectName(u"l43")
        self.l43.setMinimumSize(QSize(41, 41))
        self.l43.setMaximumSize(QSize(41, 41))
        self.l43.setFont(font2)
        self.l43.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l43.setMaxLength(1)
        self.l43.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.l43, 1, 0, 1, 1)

        self.l44 = QLineEdit(self.frame_12)
        self.l44.setObjectName(u"l44")
        self.l44.setMinimumSize(QSize(41, 41))
        self.l44.setMaximumSize(QSize(41, 41))
        self.l44.setFont(font2)
        self.l44.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l44.setMaxLength(1)
        self.l44.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.l44, 1, 1, 1, 1)

        self.l45 = QLineEdit(self.frame_12)
        self.l45.setObjectName(u"l45")
        self.l45.setMinimumSize(QSize(41, 41))
        self.l45.setMaximumSize(QSize(41, 41))
        self.l45.setFont(font2)
        self.l45.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l45.setMaxLength(1)
        self.l45.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.l45, 1, 2, 1, 1)

        self.l52 = QLineEdit(self.frame_12)
        self.l52.setObjectName(u"l52")
        self.l52.setMinimumSize(QSize(41, 41))
        self.l52.setMaximumSize(QSize(41, 41))
        self.l52.setFont(font2)
        self.l52.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l52.setMaxLength(1)
        self.l52.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.l52, 2, 0, 1, 1)

        self.l53 = QLineEdit(self.frame_12)
        self.l53.setObjectName(u"l53")
        self.l53.setMinimumSize(QSize(41, 41))
        self.l53.setMaximumSize(QSize(41, 41))
        self.l53.setFont(font2)
        self.l53.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l53.setMaxLength(1)
        self.l53.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.l53, 2, 1, 1, 1)

        self.l54 = QLineEdit(self.frame_12)
        self.l54.setObjectName(u"l54")
        self.l54.setMinimumSize(QSize(41, 41))
        self.l54.setMaximumSize(QSize(41, 41))
        self.l54.setFont(font2)
        self.l54.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l54.setMaxLength(1)
        self.l54.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.l54, 2, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_12)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(390, 16777215))
        self.frame_6.setStyleSheet(u"background-color: rgb(130, 136, 255);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(130, 130))
        self.frame_13.setMaximumSize(QSize(130, 130))
        self.frame_13.setStyleSheet(u"border: none;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_13)
        self.gridLayout_8.setSpacing(1)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.l55 = QLineEdit(self.frame_13)
        self.l55.setObjectName(u"l55")
        self.l55.setMinimumSize(QSize(41, 41))
        self.l55.setMaximumSize(QSize(41, 41))
        self.l55.setFont(font2)
        self.l55.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l55.setMaxLength(1)
        self.l55.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l55, 0, 0, 1, 1)

        self.l56 = QLineEdit(self.frame_13)
        self.l56.setObjectName(u"l56")
        self.l56.setMinimumSize(QSize(41, 41))
        self.l56.setMaximumSize(QSize(41, 41))
        self.l56.setFont(font2)
        self.l56.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l56.setMaxLength(1)
        self.l56.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l56, 0, 1, 1, 1)

        self.l57 = QLineEdit(self.frame_13)
        self.l57.setObjectName(u"l57")
        self.l57.setMinimumSize(QSize(41, 41))
        self.l57.setMaximumSize(QSize(41, 41))
        self.l57.setFont(font2)
        self.l57.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l57.setMaxLength(1)
        self.l57.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l57, 0, 2, 1, 1)

        self.l64 = QLineEdit(self.frame_13)
        self.l64.setObjectName(u"l64")
        self.l64.setMinimumSize(QSize(41, 41))
        self.l64.setMaximumSize(QSize(41, 41))
        self.l64.setFont(font2)
        self.l64.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l64.setMaxLength(1)
        self.l64.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l64, 1, 0, 1, 1)

        self.l65 = QLineEdit(self.frame_13)
        self.l65.setObjectName(u"l65")
        self.l65.setMinimumSize(QSize(41, 41))
        self.l65.setMaximumSize(QSize(41, 41))
        self.l65.setFont(font2)
        self.l65.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l65.setMaxLength(1)
        self.l65.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l65, 1, 1, 1, 1)

        self.l66 = QLineEdit(self.frame_13)
        self.l66.setObjectName(u"l66")
        self.l66.setMinimumSize(QSize(41, 41))
        self.l66.setMaximumSize(QSize(41, 41))
        self.l66.setFont(font2)
        self.l66.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l66.setMaxLength(1)
        self.l66.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l66, 1, 2, 1, 1)

        self.l73 = QLineEdit(self.frame_13)
        self.l73.setObjectName(u"l73")
        self.l73.setMinimumSize(QSize(41, 41))
        self.l73.setMaximumSize(QSize(41, 41))
        self.l73.setFont(font2)
        self.l73.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l73.setMaxLength(1)
        self.l73.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l73, 2, 0, 1, 1)

        self.l74 = QLineEdit(self.frame_13)
        self.l74.setObjectName(u"l74")
        self.l74.setMinimumSize(QSize(41, 41))
        self.l74.setMaximumSize(QSize(41, 41))
        self.l74.setFont(font2)
        self.l74.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l74.setMaxLength(1)
        self.l74.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l74, 2, 1, 1, 1)

        self.l75 = QLineEdit(self.frame_13)
        self.l75.setObjectName(u"l75")
        self.l75.setMinimumSize(QSize(41, 41))
        self.l75.setMaximumSize(QSize(41, 41))
        self.l75.setFont(font2)
        self.l75.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l75.setMaxLength(1)
        self.l75.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.l75, 2, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(130, 130))
        self.frame_14.setMaximumSize(QSize(130, 130))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_14)
        self.gridLayout_7.setSpacing(1)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.l58 = QLineEdit(self.frame_14)
        self.l58.setObjectName(u"l58")
        self.l58.setMinimumSize(QSize(41, 41))
        self.l58.setMaximumSize(QSize(41, 41))
        self.l58.setFont(font2)
        self.l58.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l58.setMaxLength(1)
        self.l58.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.l58, 0, 0, 1, 1)

        self.l59 = QLineEdit(self.frame_14)
        self.l59.setObjectName(u"l59")
        self.l59.setMinimumSize(QSize(41, 41))
        self.l59.setMaximumSize(QSize(41, 41))
        self.l59.setFont(font2)
        self.l59.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l59.setMaxLength(1)
        self.l59.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.l59, 0, 1, 1, 1)

        self.l60 = QLineEdit(self.frame_14)
        self.l60.setObjectName(u"l60")
        self.l60.setMinimumSize(QSize(41, 41))
        self.l60.setMaximumSize(QSize(41, 41))
        self.l60.setFont(font2)
        self.l60.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l60.setMaxLength(1)
        self.l60.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.l60, 0, 2, 1, 1)

        self.l67 = QLineEdit(self.frame_14)
        self.l67.setObjectName(u"l67")
        self.l67.setMinimumSize(QSize(41, 41))
        self.l67.setMaximumSize(QSize(41, 41))
        self.l67.setFont(font2)
        self.l67.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l67.setMaxLength(1)
        self.l67.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.l67, 1, 0, 1, 1)

        self.l68 = QLineEdit(self.frame_14)
        self.l68.setObjectName(u"l68")
        self.l68.setMinimumSize(QSize(41, 41))
        self.l68.setMaximumSize(QSize(41, 41))
        self.l68.setFont(font2)
        self.l68.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l68.setMaxLength(1)
        self.l68.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.l68, 1, 1, 1, 1)

        self.l69 = QLineEdit(self.frame_14)
        self.l69.setObjectName(u"l69")
        self.l69.setMinimumSize(QSize(41, 41))
        self.l69.setMaximumSize(QSize(41, 41))
        self.l69.setFont(font2)
        self.l69.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l69.setMaxLength(1)
        self.l69.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.l69, 1, 2, 1, 1)

        self.l76 = QLineEdit(self.frame_14)
        self.l76.setObjectName(u"l76")
        self.l76.setMinimumSize(QSize(41, 41))
        self.l76.setMaximumSize(QSize(41, 41))
        self.l76.setFont(font2)
        self.l76.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l76.setMaxLength(1)
        self.l76.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.l76, 2, 0, 1, 1)

        self.l77 = QLineEdit(self.frame_14)
        self.l77.setObjectName(u"l77")
        self.l77.setMinimumSize(QSize(41, 41))
        self.l77.setMaximumSize(QSize(41, 41))
        self.l77.setFont(font2)
        self.l77.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l77.setMaxLength(1)
        self.l77.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.l77, 2, 1, 1, 1)

        self.l78 = QLineEdit(self.frame_14)
        self.l78.setObjectName(u"l78")
        self.l78.setMinimumSize(QSize(41, 41))
        self.l78.setMaximumSize(QSize(41, 41))
        self.l78.setFont(font2)
        self.l78.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l78.setMaxLength(1)
        self.l78.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.l78, 2, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(130, 130))
        self.frame_15.setMaximumSize(QSize(130, 130))
        self.frame_15.setStyleSheet(u"border: none;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_15)
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.l61 = QLineEdit(self.frame_15)
        self.l61.setObjectName(u"l61")
        self.l61.setMinimumSize(QSize(41, 41))
        self.l61.setMaximumSize(QSize(41, 41))
        self.l61.setFont(font2)
        self.l61.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l61.setMaxLength(1)
        self.l61.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.l61, 0, 0, 1, 1)

        self.l62 = QLineEdit(self.frame_15)
        self.l62.setObjectName(u"l62")
        self.l62.setMinimumSize(QSize(41, 41))
        self.l62.setMaximumSize(QSize(41, 41))
        self.l62.setFont(font2)
        self.l62.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l62.setMaxLength(1)
        self.l62.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.l62, 0, 1, 1, 1)

        self.l63 = QLineEdit(self.frame_15)
        self.l63.setObjectName(u"l63")
        self.l63.setMinimumSize(QSize(41, 41))
        self.l63.setMaximumSize(QSize(41, 41))
        self.l63.setFont(font2)
        self.l63.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l63.setMaxLength(1)
        self.l63.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.l63, 0, 2, 1, 1)

        self.l70 = QLineEdit(self.frame_15)
        self.l70.setObjectName(u"l70")
        self.l70.setMinimumSize(QSize(41, 41))
        self.l70.setMaximumSize(QSize(41, 41))
        self.l70.setFont(font2)
        self.l70.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l70.setMaxLength(1)
        self.l70.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.l70, 1, 0, 1, 1)

        self.l71 = QLineEdit(self.frame_15)
        self.l71.setObjectName(u"l71")
        self.l71.setMinimumSize(QSize(41, 41))
        self.l71.setMaximumSize(QSize(41, 41))
        self.l71.setFont(font2)
        self.l71.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l71.setMaxLength(1)
        self.l71.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.l71, 1, 1, 1, 1)

        self.l72 = QLineEdit(self.frame_15)
        self.l72.setObjectName(u"l72")
        self.l72.setMinimumSize(QSize(41, 41))
        self.l72.setMaximumSize(QSize(41, 41))
        self.l72.setFont(font2)
        self.l72.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l72.setMaxLength(1)
        self.l72.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.l72, 1, 2, 1, 1)

        self.l79 = QLineEdit(self.frame_15)
        self.l79.setObjectName(u"l79")
        self.l79.setMinimumSize(QSize(41, 41))
        self.l79.setMaximumSize(QSize(41, 41))
        self.l79.setFont(font2)
        self.l79.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l79.setMaxLength(1)
        self.l79.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.l79, 2, 0, 1, 1)

        self.l80 = QLineEdit(self.frame_15)
        self.l80.setObjectName(u"l80")
        self.l80.setMinimumSize(QSize(41, 41))
        self.l80.setMaximumSize(QSize(41, 41))
        self.l80.setFont(font2)
        self.l80.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l80.setMaxLength(1)
        self.l80.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.l80, 2, 1, 1, 1)

        self.l81 = QLineEdit(self.frame_15)
        self.l81.setObjectName(u"l81")
        self.l81.setMinimumSize(QSize(41, 41))
        self.l81.setMaximumSize(QSize(41, 41))
        self.l81.setFont(font2)
        self.l81.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"color: rgb(114, 156, 255);")
        self.l81.setMaxLength(1)
        self.l81.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.l81, 2, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_15)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bt_solve = QPushButton(self.frame_3)
        self.bt_solve.setObjectName(u"bt_solve")
        self.bt_solve.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Segoe Print"])
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setItalic(False)
        self.bt_solve.setFont(font3)
        self.bt_solve.setStyleSheet(u"QPushButton {\n"
"border-radius: 8px;\n"
"font: 700 16pt \"Segoe Print\";\n"
"background-color: rgb(206, 209, 221);\n"
"border:2px solid rgb(130, 136, 255);\n"
"color: rgb(130, 136, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-radius: 10px;\n"
"font: 700 16pt \"Segoe Print\";\n"
"background-color: rgb(209, 209, 209);\n"
"border: 2px solid rgb(130, 136, 255);\n"
"color: rgb(130, 136, 255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.bt_solve)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.l1, self.l2)
        QWidget.setTabOrder(self.l2, self.l3)
        QWidget.setTabOrder(self.l3, self.l4)
        QWidget.setTabOrder(self.l4, self.l5)
        QWidget.setTabOrder(self.l5, self.l6)
        QWidget.setTabOrder(self.l6, self.l7)
        QWidget.setTabOrder(self.l7, self.l8)
        QWidget.setTabOrder(self.l8, self.l9)
        QWidget.setTabOrder(self.l9, self.l10)
        QWidget.setTabOrder(self.l10, self.l11)
        QWidget.setTabOrder(self.l11, self.l12)
        QWidget.setTabOrder(self.l12, self.l13)
        QWidget.setTabOrder(self.l13, self.l14)
        QWidget.setTabOrder(self.l14, self.l15)
        QWidget.setTabOrder(self.l15, self.l16)
        QWidget.setTabOrder(self.l16, self.l17)
        QWidget.setTabOrder(self.l17, self.l18)
        QWidget.setTabOrder(self.l18, self.l19)
        QWidget.setTabOrder(self.l19, self.l20)
        QWidget.setTabOrder(self.l20, self.l21)
        QWidget.setTabOrder(self.l21, self.l22)
        QWidget.setTabOrder(self.l22, self.l23)
        QWidget.setTabOrder(self.l23, self.l24)
        QWidget.setTabOrder(self.l24, self.l25)
        QWidget.setTabOrder(self.l25, self.l26)
        QWidget.setTabOrder(self.l26, self.l27)
        QWidget.setTabOrder(self.l27, self.l28)
        QWidget.setTabOrder(self.l28, self.l29)
        QWidget.setTabOrder(self.l29, self.l30)
        QWidget.setTabOrder(self.l30, self.l31)
        QWidget.setTabOrder(self.l31, self.l32)
        QWidget.setTabOrder(self.l32, self.l33)
        QWidget.setTabOrder(self.l33, self.l34)
        QWidget.setTabOrder(self.l34, self.l35)
        QWidget.setTabOrder(self.l35, self.l36)
        QWidget.setTabOrder(self.l36, self.l37)
        QWidget.setTabOrder(self.l37, self.l38)
        QWidget.setTabOrder(self.l38, self.l39)
        QWidget.setTabOrder(self.l39, self.l40)
        QWidget.setTabOrder(self.l40, self.l41)
        QWidget.setTabOrder(self.l41, self.l42)
        QWidget.setTabOrder(self.l42, self.l43)
        QWidget.setTabOrder(self.l43, self.l44)
        QWidget.setTabOrder(self.l44, self.l45)
        QWidget.setTabOrder(self.l45, self.l46)
        QWidget.setTabOrder(self.l46, self.l47)
        QWidget.setTabOrder(self.l47, self.l48)
        QWidget.setTabOrder(self.l48, self.l49)
        QWidget.setTabOrder(self.l49, self.l50)
        QWidget.setTabOrder(self.l50, self.l51)
        QWidget.setTabOrder(self.l51, self.l52)
        QWidget.setTabOrder(self.l52, self.l53)
        QWidget.setTabOrder(self.l53, self.l54)
        QWidget.setTabOrder(self.l54, self.l55)
        QWidget.setTabOrder(self.l55, self.l56)
        QWidget.setTabOrder(self.l56, self.l57)
        QWidget.setTabOrder(self.l57, self.l58)
        QWidget.setTabOrder(self.l58, self.l59)
        QWidget.setTabOrder(self.l59, self.l60)
        QWidget.setTabOrder(self.l60, self.l61)
        QWidget.setTabOrder(self.l61, self.l62)
        QWidget.setTabOrder(self.l62, self.l63)
        QWidget.setTabOrder(self.l63, self.l64)
        QWidget.setTabOrder(self.l64, self.l65)
        QWidget.setTabOrder(self.l65, self.l66)
        QWidget.setTabOrder(self.l66, self.l67)
        QWidget.setTabOrder(self.l67, self.l68)
        QWidget.setTabOrder(self.l68, self.l69)
        QWidget.setTabOrder(self.l69, self.l70)
        QWidget.setTabOrder(self.l70, self.l71)
        QWidget.setTabOrder(self.l71, self.l72)
        QWidget.setTabOrder(self.l72, self.l73)
        QWidget.setTabOrder(self.l73, self.l74)
        QWidget.setTabOrder(self.l74, self.l75)
        QWidget.setTabOrder(self.l75, self.l76)
        QWidget.setTabOrder(self.l76, self.l77)
        QWidget.setTabOrder(self.l77, self.l78)
        QWidget.setTabOrder(self.l78, self.l79)
        QWidget.setTabOrder(self.l79, self.l80)
        QWidget.setTabOrder(self.l80, self.l81)
        QWidget.setTabOrder(self.l81, self.bt_solve)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SUDOKU SOLVER", None))
        self.bt_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.l1.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.l2.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.l10.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.l20.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.l21.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.frame_8.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: none;", None))
        self.l14.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.l15.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.l22.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.l8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.l9.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.l30.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.l46.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.l48.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.frame_11.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: none;", None))
        self.l33.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.l34.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.l43.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.l53.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.l56.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.l64.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.frame_14.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: none;", None))
        self.l59.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.l67.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.l68.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.l69.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.l77.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.l63.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.l79.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.l80.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.l81.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.bt_solve.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
    # retranslateUi

