# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tileDiagnosticsUGVOIxBhc.ui'
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
    QLabel, QLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_tileDiagnosticsUGV(object):
    def setupUi(self, tileDiagnosticsUGV):
        if not tileDiagnosticsUGV.objectName():
            tileDiagnosticsUGV.setObjectName(u"tileDiagnosticsUGV")
        tileDiagnosticsUGV.resize(350, 128)
        tileDiagnosticsUGV.setMinimumSize(QSize(350, 128))
        tileDiagnosticsUGV.setMaximumSize(QSize(350, 128))
        tileDiagnosticsUGV.setStyleSheet(u"QWidget QFrame {\n"
"background-color: rgb(21, 23, 27);\n"
"border-radius: 5px;\n"
"color: rgb(221, 221, 221);\n"
"}\n"
"#ssh_icon {\n"
"background-image: url(:/icons/images/icons2/ssh_na.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}\n"
"\n"
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
"}\n"
"#battery_icon {\n"
"background-image: url(:/icons/images/icons2/battery_na.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"#battery_text {\n"
"color: rgb(92, 95, 102) !important;\n"
"font-size: 10px !important;\n"
"}")
        self.verticalLayout = QVBoxLayout(tileDiagnosticsUGV)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(tileDiagnosticsUGV)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 9, 12, 12)
        self.horizontalFrame = QFrame(self.frame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 24))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(1, 0, 1, 0)
        self.name_text = QLabel(self.horizontalFrame)
        self.name_text.setObjectName(u"name_text")
        self.name_text.setMinimumSize(QSize(0, 0))
        self.name_text.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout.addWidget(self.name_text, 0, Qt.AlignTop)

        self.battery_text = QLabel(self.horizontalFrame)
        self.battery_text.setObjectName(u"battery_text")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battery_text.sizePolicy().hasHeightForWidth())
        self.battery_text.setSizePolicy(sizePolicy)
        self.battery_text.setMinimumSize(QSize(38, 0))
        self.battery_text.setMaximumSize(QSize(38, 16777215))

        self.horizontalLayout.addWidget(self.battery_text, 0, Qt.AlignRight|Qt.AlignTop)

        self.battery_icon = QFrame(self.horizontalFrame)
        self.battery_icon.setObjectName(u"battery_icon")
        self.battery_icon.setMinimumSize(QSize(24, 16))
        self.battery_icon.setMaximumSize(QSize(24, 24))
        self.battery_icon.setFrameShape(QFrame.StyledPanel)
        self.battery_icon.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.battery_icon, 0, Qt.AlignTop)

        self.ssh_icon = QPushButton(self.horizontalFrame)
        self.ssh_icon.setObjectName(u"ssh_icon")
        self.ssh_icon.setMinimumSize(QSize(16, 16))
        self.ssh_icon.setMaximumSize(QSize(16, 16))
        self.ssh_icon.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.ssh_icon, 0, Qt.AlignTop)

        self.network_icon = QFrame(self.horizontalFrame)
        self.network_icon.setObjectName(u"network_icon")
        self.network_icon.setMinimumSize(QSize(0, 16))
        self.network_icon.setMaximumSize(QSize(16, 24))
        self.network_icon.setFrameShape(QFrame.StyledPanel)
        self.network_icon.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.network_icon, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.horizontalFrame)

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
        self.frame_2 = QFrame(self.verticalFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ip_text = QLabel(self.frame_2)
        self.ip_text.setObjectName(u"ip_text")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ip_text.sizePolicy().hasHeightForWidth())
        self.ip_text.setSizePolicy(sizePolicy2)
        self.ip_text.setMinimumSize(QSize(0, 0))
        font = QFont()
        self.ip_text.setFont(font)

        self.horizontalLayout_2.addWidget(self.ip_text, 0, Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.nodes = QFrame(self.verticalFrame)
        self.nodes.setObjectName(u"nodes")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.nodes.sizePolicy().hasHeightForWidth())
        self.nodes.setSizePolicy(sizePolicy3)
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


        self.retranslateUi(tileDiagnosticsUGV)

        QMetaObject.connectSlotsByName(tileDiagnosticsUGV)
    # setupUi

    def retranslateUi(self, tileDiagnosticsUGV):
        tileDiagnosticsUGV.setWindowTitle(QCoreApplication.translate("tileDiagnosticsUGV", u"Form", None))
        self.name_text.setText(QCoreApplication.translate("tileDiagnosticsUGV", u"name", None))
        self.battery_text.setText(QCoreApplication.translate("tileDiagnosticsUGV", u"80%", None))
        self.ssh_icon.setText("")
        self.ip_text.setText(QCoreApplication.translate("tileDiagnosticsUGV", u"ip", None))
    # retranslateUi
