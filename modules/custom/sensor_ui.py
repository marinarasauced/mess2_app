# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tileSensorTemplatelufGhJ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QSizePolicy, QVBoxLayout, QWidget)

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
"color: rgb(201, 201, 201) !important;\n"
"font-size: 10px !important;\n"
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

        self.frame_2 = QFrame(self.verticalWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.verticalWidget)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(tileSensorTemplate)

        QMetaObject.connectSlotsByName(tileSensorTemplate)
    # setupUi

    def retranslateUi(self, tileSensorTemplate):
        tileSensorTemplate.setWindowTitle(QCoreApplication.translate("tileSensorTemplate", u"Form", None))
        self.sensorName.setText(QCoreApplication.translate("tileSensorTemplate", u"sensorName", None))
        self.sensorIP.setText(QCoreApplication.translate("tileSensorTemplate", u"sensorIP", None))
    # retranslateUi

