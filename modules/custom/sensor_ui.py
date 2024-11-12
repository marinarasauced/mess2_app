# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tileSensorTemplatePwVPBR.ui'
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

class Ui_tileSensorTemplate(object):
    def setupUi(self, tileSensorTemplate):
        if not tileSensorTemplate.objectName():
            tileSensorTemplate.setObjectName(u"tileSensorTemplate")
        tileSensorTemplate.resize(350, 128)
        tileSensorTemplate.setMinimumSize(QSize(350, 128))
        tileSensorTemplate.setMaximumSize(QSize(350, 128))
        tileSensorTemplate.setStyleSheet(u"QWidget QFrame {\n"
"background-color: rgb(21, 23, 27);\n"
"border-radius: 5px;\n"
"color: rgb(221, 221, 221);\n"
"}\n"
"#sensorConnected {\n"
"background-image: url(:/icons/images/icons2/status_disconnected.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"#sensorOnline {\n"
"background-image: url(:/icons/images/icons2/status_offline.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"#sensorIP {\n"
"color: rgb(191, 191, 191) !important;\n"
"font-size: 10px !important;\n"
"}\n"
"#sensorNodes {\n"
"background-color: rgb(30, 33, 39);\n"
"}\n"
"#sensorNodes QFrame {\n"
"background-color: transparent;\n"
"font-size: 10px;\n"
"}\n"
"#nodeName1 {\n"
"color: rgb(191, 191, 191);\n"
"}\n"
"#nodeName2 {\n"
"color: rgb(191, 191, 191);\n"
"}\n"
"#nodeName3 {\n"
"color: rgb(191, 191, 191);\n"
"}\n"
"#nodeStatus1 {\n"
"color: rgb(92, 95, 102);\n"
"}\n"
"#nodeStatus2 {\n"
"color: rgb(92, 95, 102);\n"
"}\n"
"#nodeStatus3 {\n"
"color: rgb(92, 95, 102);\n"
"}")
        self.verticalLayout = QVBoxLayout(tileSensorTemplate)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(tileSensorTemplate)
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
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(1, 0, 1, 0)
        self.sensorName = QLabel(self.horizontalWidget)
        self.sensorName.setObjectName(u"sensorName")
        self.sensorName.setMinimumSize(QSize(0, 0))
        self.sensorName.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout.addWidget(self.sensorName, 0, Qt.AlignTop)

        self.sensorConnected = QFrame(self.horizontalWidget)
        self.sensorConnected.setObjectName(u"sensorConnected")
        self.sensorConnected.setMinimumSize(QSize(0, 16))
        self.sensorConnected.setMaximumSize(QSize(24, 24))
        self.sensorConnected.setFrameShape(QFrame.StyledPanel)
        self.sensorConnected.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.sensorConnected, 0, Qt.AlignTop)

        self.sensorOnline = QFrame(self.horizontalWidget)
        self.sensorOnline.setObjectName(u"sensorOnline")
        self.sensorOnline.setMinimumSize(QSize(0, 16))
        self.sensorOnline.setMaximumSize(QSize(24, 24))
        self.sensorOnline.setFrameShape(QFrame.StyledPanel)
        self.sensorOnline.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.sensorOnline, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.horizontalWidget, 0, Qt.AlignTop)

        self.verticalWidget = QWidget(self.frame)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sensorIP = QLabel(self.verticalWidget)
        self.sensorIP.setObjectName(u"sensorIP")
        font = QFont()
        self.sensorIP.setFont(font)

        self.verticalLayout_3.addWidget(self.sensorIP, 0, Qt.AlignTop)

        self.sensorNodes = QFrame(self.verticalWidget)
        self.sensorNodes.setObjectName(u"sensorNodes")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sensorNodes.sizePolicy().hasHeightForWidth())
        self.sensorNodes.setSizePolicy(sizePolicy1)
        self.sensorNodes.setStyleSheet(u"")
        self.sensorNodes.setFrameShape(QFrame.StyledPanel)
        self.sensorNodes.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.sensorNodes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(9, 3, 9, 3)
        self.nodeStatus3 = QLabel(self.sensorNodes)
        self.nodeStatus3.setObjectName(u"nodeStatus3")
        self.nodeStatus3.setMaximumSize(QSize(16777215, 16))

        self.gridLayout.addWidget(self.nodeStatus3, 2, 1, 1, 1)

        self.nodeName2 = QLabel(self.sensorNodes)
        self.nodeName2.setObjectName(u"nodeName2")
        self.nodeName2.setMinimumSize(QSize(245, 0))
        self.nodeName2.setMaximumSize(QSize(16777215, 16))

        self.gridLayout.addWidget(self.nodeName2, 1, 0, 1, 1)

        self.nodeStatus2 = QLabel(self.sensorNodes)
        self.nodeStatus2.setObjectName(u"nodeStatus2")
        self.nodeStatus2.setMaximumSize(QSize(16777215, 16))

        self.gridLayout.addWidget(self.nodeStatus2, 1, 1, 1, 1)

        self.nodeStatus1 = QLabel(self.sensorNodes)
        self.nodeStatus1.setObjectName(u"nodeStatus1")
        self.nodeStatus1.setMaximumSize(QSize(16777215, 16))

        self.gridLayout.addWidget(self.nodeStatus1, 0, 1, 1, 1)

        self.nodeName3 = QLabel(self.sensorNodes)
        self.nodeName3.setObjectName(u"nodeName3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.nodeName3.sizePolicy().hasHeightForWidth())
        self.nodeName3.setSizePolicy(sizePolicy2)
        self.nodeName3.setMinimumSize(QSize(245, 0))
        self.nodeName3.setMaximumSize(QSize(16777215, 16))

        self.gridLayout.addWidget(self.nodeName3, 2, 0, 1, 1)

        self.nodeName1 = QLabel(self.sensorNodes)
        self.nodeName1.setObjectName(u"nodeName1")
        self.nodeName1.setMinimumSize(QSize(245, 0))
        self.nodeName1.setMaximumSize(QSize(16777215, 16))

        self.gridLayout.addWidget(self.nodeName1, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.sensorNodes)


        self.verticalLayout_2.addWidget(self.verticalWidget)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(tileSensorTemplate)

        QMetaObject.connectSlotsByName(tileSensorTemplate)
    # setupUi

    def retranslateUi(self, tileSensorTemplate):
        tileSensorTemplate.setWindowTitle(QCoreApplication.translate("tileSensorTemplate", u"Form", None))
        self.sensorName.setText(QCoreApplication.translate("tileSensorTemplate", u"sensorName", None))
        self.sensorIP.setText(QCoreApplication.translate("tileSensorTemplate", u"sensorIP", None))
        self.nodeStatus3.setText(QCoreApplication.translate("tileSensorTemplate", u"running", None))
        self.nodeName2.setText(QCoreApplication.translate("tileSensorTemplate", u"/mess2/vicon/node2", None))
        self.nodeStatus2.setText(QCoreApplication.translate("tileSensorTemplate", u"not running", None))
        self.nodeStatus1.setText(QCoreApplication.translate("tileSensorTemplate", u"not running", None))
        self.nodeName3.setText(QCoreApplication.translate("tileSensorTemplate", u"/mess2/vicon/node3", None))
        self.nodeName1.setText(QCoreApplication.translate("tileSensorTemplate", u"/mess2/vicon/node1", None))
    # retranslateUi

