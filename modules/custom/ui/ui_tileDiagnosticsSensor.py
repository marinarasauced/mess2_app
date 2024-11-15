# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tileDiagnosticsSensorkCtdqC.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
    QLabel, QLayout, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_tileDiagnosticsSensor(object):
    def setupUi(self, tileDiagnosticsSensor):
        if not tileDiagnosticsSensor.objectName():
            tileDiagnosticsSensor.setObjectName(u"tileDiagnosticsSensor")
        tileDiagnosticsSensor.resize(350, 128)
        tileDiagnosticsSensor.setMinimumSize(QSize(350, 128))
        tileDiagnosticsSensor.setMaximumSize(QSize(350, 128))
        tileDiagnosticsSensor.setStyleSheet(u"QWidget QFrame {\n"
"background-color: rgb(21, 23, 27);\n"
"border-radius: 5px;\n"
"color: rgb(221, 221, 221);\n"
"}\n"
"#network_icon {\n"
"background-image: url(:/icons/images/icons2/network_na.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"#ip_text {\n"
"color: rgb(191, 191, 191) !important;\n"
"font-size: 10px !important;\n"
"}\n"
"#nodes {\n"
"background-color: rgb(30, 33, 39);\n"
"}\n"
"#nodes QFrame {\n"
"background-color: transparent;\n"
"font-size: 10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(tileDiagnosticsSensor)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(tileDiagnosticsSensor)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 9, 12, 12)
        self.horizontalWidget = QWidget(self.frame)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(0, 24))
        self.horizontalWidget.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(1, 0, 1, 0)
        self.name_text = QLabel(self.horizontalWidget)
        self.name_text.setObjectName(u"name_text")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.name_text.sizePolicy().hasHeightForWidth())
        self.name_text.setSizePolicy(sizePolicy)
        self.name_text.setMinimumSize(QSize(0, 16))
        self.name_text.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.name_text, 0, Qt.AlignTop)

        self.network_icon = QFrame(self.horizontalWidget)
        self.network_icon.setObjectName(u"network_icon")
        self.network_icon.setMinimumSize(QSize(16, 16))
        self.network_icon.setMaximumSize(QSize(16, 16))
        self.network_icon.setFrameShape(QFrame.StyledPanel)
        self.network_icon.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.network_icon, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.horizontalWidget, 0, Qt.AlignTop)

        self.verticalFrame = QFrame(self.frame)
        self.verticalFrame.setObjectName(u"verticalFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ip_text = QLabel(self.verticalFrame)
        self.ip_text.setObjectName(u"ip_text")
        font = QFont()
        self.ip_text.setFont(font)

        self.verticalLayout_3.addWidget(self.ip_text, 0, Qt.AlignTop)

        self.nodes = QFrame(self.verticalFrame)
        self.nodes.setObjectName(u"nodes")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.nodes.sizePolicy().hasHeightForWidth())
        self.nodes.setSizePolicy(sizePolicy2)
        self.nodes.setStyleSheet(u"")
        self.nodes.setFrameShape(QFrame.StyledPanel)
        self.nodes.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.nodes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.nodesLayout = QGridLayout()
        self.nodesLayout.setObjectName(u"nodesLayout")

        self.gridLayout.addLayout(self.nodesLayout, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.nodes)


        self.verticalLayout_2.addWidget(self.verticalFrame)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(tileDiagnosticsSensor)

        QMetaObject.connectSlotsByName(tileDiagnosticsSensor)
    # setupUi

    def retranslateUi(self, tileDiagnosticsSensor):
        tileDiagnosticsSensor.setWindowTitle(QCoreApplication.translate("tileDiagnosticsSensor", u"Form", None))
        self.name_text.setText(QCoreApplication.translate("tileDiagnosticsSensor", u"name", None))
        self.ip_text.setText(QCoreApplication.translate("tileDiagnosticsSensor", u"ip", None))
    # retranslateUi

