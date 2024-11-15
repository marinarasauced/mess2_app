# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWNFBYv.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import modules.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setMinimumSize(QSize(1600, 900))
        MainWindow.setMaximumSize(QSize(1600, 900))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"color: rgb(221, 221, 221);\n"
"font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"color: #ffffff;\n"
"background-color: rgba(33, 37, 43, 180);\n"
"border: 1px solid rgb(44, 49, 58);\n"
"background-image: none;\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 2px solid rgb(0, 204, 255);\n"
"text-align: left;\n"
"padding-left: 8px;\n"
"margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp { \n"
"background-color: rgb(37, 39,"
                        " 43);\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg { \n"
"background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"background-color: rgb(33, 37, 43);\n"
"background-image: url(:/images/images/images/mess2_beta.png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(0, 204, 255 ); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton { \n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 22px solid transparent;\n"
"background-color: transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"background-color: rgb(37, 39, 43);\n"
"}\n"
"#topMenu .QPushButton:pressed { \n"
"background-color: rgb(98, 114, 164 );\n"
"color: rgb(255, 255"
                        ", 255);\n"
"}\n"
"#bottomMenu .QPushButton { \n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"background-color:transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"background-color: rgb(37, 39, 43);\n"
"}\n"
"#bottomMenu .QPushButton:pressed { \n"
"background-color: rgb(98, 114, 164 );\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"#diagnosticsSubMenu2 .QPushButton { \n"
"background-color: transparent;\n"
"text-align: center;\n"
"padding: 0 18px 0 18px;\n"
"border: None;\n"
"border-radius: 0;\n"
"}\n"
"#diagnosticsSubMenu2 .QPushButton:hover {\n"
"background-color: rgb(37, 39, 43);\n"
"border: None;\n"
"border-radius: 0;\n"
"}\n"
"#diagnosticsSubMenu2 .QPushButton:pressed { \n"
"background-color: rgb(98, 114, 164 );\n"
"color: rgb(255, 255, 255);\n"
"border: None;\n"
"border-radius: 0;\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"background-position: left center;\n"
""
                        "background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"background-color: rgb(37, 41, 48);\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"color: rgb(138, 139, 141);\n"
"}\n"
"#toggleButton:hover {\n"
"background-color: rgb(37, 39, 43);\n"
"}\n"
"#toggleButton:pressed {\n"
"background-color: rgb(98, 114, 164 );\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox { \n"
"background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{ \n"
"background-color: rgb(98, 114, 164 )\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255,"
                        " 0); border: none; border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(98, 114, 164 ); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(98, 114, 164 ); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"border-top: 3px solid rgb(37, 39, 43);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 22px solid transparent;\n"
"background-color:transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"background-color: rgb(37, 39, 43);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed { \n"
"background-color: rgb(98, 114, 164 );\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{ \n"
"background-color: "
                        "rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"border-top: 3px solid rgb(0, 204, 255);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none; border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(0, 204, 255 ); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(255, 0, 0); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton { \n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 2"
                        "2px solid transparent;\n"
"background-color:transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"background-color: rgb(37, 39, 43);\n"
"}\n"
"#contentSettings .QPushButton:pressed { \n"
"background-color: rgb(98, 114, 164 );\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget { \n"
"background-color: transparent;\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"gridline-color: rgb(44, 49, 58);\n"
"border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"border-color: rgb(44, 49, 60);\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"background-color: rgb(98, 114, 164 );\n"
"}\n"
"QHeaderView::section{\n"
"background-color: rgb(33, 37, 43);\n"
"max-width: 30px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"border-style: none;\n"
"borde"
                        "r-bottom: 1px solid rgb(44, 49, 60);\n"
"border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader { \n"
"background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"border: 1px solid rgb(33, 37, 43);\n"
"background-color: rgb(33, 37, 43);\n"
"padding: 3px;\n"
"border-top-left-radius: 7px;\n"
"border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(33, 37, 43);\n"
"padding-left: 10px;\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 204, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////"
                        "////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"background-color: rgb(27, 29, 35);\n"
"border-radius: 0px;\n"
"padding: 6px;\n"
"selection-color: rgb(231, 231, 231);\n"
"selection-background-color: rgb(0, 114, 143);\n"
"}\n"
"QPlainTextEdit QScrollBar:vertical {\n"
"width: 8px;\n"
"}\n"
"QPlainTextEdit QScrollBar:horizontal {\n"
"height: 8px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"border: none;\n"
"background: rgb(52, 59, 72);\n"
"height: 8px;\n"
"margin: 0px 21px 0 21px;\n"
"border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"background: rgb(98, 114, 164 );\n"
"min-width: 25px;\n"
"border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"border: none;\n"
"background: "
                        "rgb(55, 63, 77);\n"
"width: 20px;\n"
"border-top-right-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"subcontrol-position: right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"border: none;\n"
"background: rgb(55, 63, 77);\n"
"width: 20px;\n"
"border-top-left-radius: 4px;\n"
"border-bottom-left-radius: 4px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"border: none;\n"
"background: rgb(52, 59, 72);\n"
"width: 8px;\n"
"margin: 0 0 0 0;\n"
"border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical { \n"
"background: rgb(40, 44, 52);\n"
"min-height: 25px;\n"
"border-radius: 4px\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"background: rgb(60, 64, 72);\n"
"}\n"
"QScrollBar::handle:vertical:pressed { \n"
"background:"
                        " rgb(60, 64, 72); \n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"border: none;\n"
"background: rgb(55, 63, 77);\n"
"height: 0px;\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"border: none;\n"
"background: rgb(55, 63, 77);\n"
"height: 0px;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"border: 3px solid rgb(52, 59, 72);\n"
"width: 15px;\n"
"height: 15px;\n"
"border-radius: 10px;\n"
"background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:ho"
                        "ver {\n"
"border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background: 3px solid rgb(52, 59, 72);\n"
"border: 3px solid rgb(52, 59, 72); \n"
"background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"border: 3px solid rgb(52, 59, 72);\n"
"width: 15px;\n"
"height: 15px;\n"
"border-radius: 10px;\n"
"background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"background: 3px solid rgb(94, 106, 130);\n"
"border: 3px solid rgb(52, 59, 72); \n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"background-color: rgb(27, 29, 35);\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(33, 37, 43);\n"
"padding: 5px;\n"
"padding-lef"
                        "t: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 25px; \n"
"border-left-width: 3px;\n"
"border-left-color: rgba(39, 44, 54, 150);\n"
"border-left-style: solid;\n"
"border-top-right-radius: 3px;\n"
"border-bottom-right-radius: 3px; \n"
"background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"background-position: center;\n"
"background-repeat: no-reperat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"color: rgb(0, 204, 255); \n"
"background-color: rgb(33, 37, 43);\n"
"padding: 10px;\n"
"selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"border-radius: 5px;\n"
"height: 10px;\n"
"margin: 0px;\n"
"background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"background-color: rgb(55, 62,"
                        " 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"background-color: rgb(98, 114, 164 );\n"
"border: none;\n"
"height: 10px;\n"
"width: 10px;\n"
"margin: 0px;\n"
"border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"background-color: rgb(0, 204, 255);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"border-radius: 5px;\n"
"width: 10px;\n"
"margin: 0px;\n"
"background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"background-color: rgb(98, 114, 164 );\n"
"border: none;\n"
"height: 10px;\n"
"width: 10px;\n"
"margin: 0px;\n"
"border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"background-color: rgb(0, 204, 255);\n"
"}\n"
"\n"
"/* ////////////////////////////////////////////////////////////////////////////////////////"
                        "/////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton { \n"
"color: rgb(0, 204, 255);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover { \n"
"color: rgb(255, 170, 255);\n"
"background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed { \n"
"color: rgb(98, 114, 164 );\n"
"background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 5px; \n"
"background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"background-color: rgb(57, 65, 80);\n"
"border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed { \n"
"background-color: rgb(35, 40, 49);\n"
"border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"#diagnosticsRow11 QPushButton {\n"
"background-color: rbg(255, 0, 0);\n"
"}\n"
"#diagnosticsRow11 QPushButton:presse"
                        "d {\n"
"background-color: rbg(0, 204, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setStyleSheet(u"background-color: rgb(13, 16, 21);")
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setStyleSheet(u"background-color: rgb(13, 16, 21);")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        palette = QPalette()
        brush = QBrush(QColor(138, 139, 141, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(21, 23, 27, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(138, 139, 141, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.toggleButton.setPalette(palette)
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);\n"
"background-color: rgb(21, 23, 27);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_diagnostics = QPushButton(self.topMenu)
        self.btn_diagnostics.setObjectName(u"btn_diagnostics")
        sizePolicy.setHeightForWidth(self.btn_diagnostics.sizePolicy().hasHeightForWidth())
        self.btn_diagnostics.setSizePolicy(sizePolicy)
        self.btn_diagnostics.setMinimumSize(QSize(0, 45))
        self.btn_diagnostics.setFont(font)
        self.btn_diagnostics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_diagnostics.setLayoutDirection(Qt.LeftToRight)
        self.btn_diagnostics.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-rss.png);")

        self.verticalLayout_8.addWidget(self.btn_diagnostics)

        self.btn_planner = QPushButton(self.topMenu)
        self.btn_planner.setObjectName(u"btn_planner")
        self.btn_planner.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_planner.sizePolicy().hasHeightForWidth())
        self.btn_planner.setSizePolicy(sizePolicy)
        self.btn_planner.setMinimumSize(QSize(0, 45))
        self.btn_planner.setFont(font)
        self.btn_planner.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_planner)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.bottomMenu)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QSize(0, 45))
        self.btn_settings.setFont(font)
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.btn_settings)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"background-color: rgb(13, 16, 21);")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setStyleSheet(u"background-color: rgb(13, 16, 21);")
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setStyleSheet(u"background-color: rgb(13, 16, 21);")
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setAutoFillBackground(False)
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        palette1 = QPalette()
        brush3 = QBrush(QColor(221, 221, 221, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(30, 33, 39, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush4)
        brush5 = QBrush(QColor(66, 74, 87, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush5)
        brush6 = QBrush(QColor(55, 61, 72, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        brush7 = QBrush(QColor(22, 25, 29, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush7)
        brush8 = QBrush(QColor(29, 33, 39, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush3)
        brush9 = QBrush(QColor(255, 255, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        brush11 = QBrush(QColor(22, 24, 29, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush11)
        brush12 = QBrush(QColor(255, 255, 220, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush12)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
        brush13 = QBrush(QColor(221, 221, 221, 128))
        brush13.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        brush14 = QBrush(QColor(75, 75, 75, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush14)
        brush15 = QBrush(QColor(42, 42, 42, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush15)
        brush16 = QBrush(QColor(33, 33, 33, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush16)
        brush17 = QBrush(QColor(38, 38, 38, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush17)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        brush18 = QBrush(QColor(25, 25, 25, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush18)
        brush19 = QBrush(QColor(43, 43, 43, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        brush20 = QBrush(QColor(37, 37, 37, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush20)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush19)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.stackedWidget.setPalette(palette1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(30, 33, 39);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"/*\n"
"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"*/")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon4)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.tableWidget.setPalette(palette2)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.diagnostics = QWidget()
        self.diagnostics.setObjectName(u"diagnostics")
        sizePolicy2.setHeightForWidth(self.diagnostics.sizePolicy().hasHeightForWidth())
        self.diagnostics.setSizePolicy(sizePolicy2)
        self.horizontalLayout_7 = QHBoxLayout(self.diagnostics)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.diagnosticsCol1 = QFrame(self.diagnostics)
        self.diagnosticsCol1.setObjectName(u"diagnosticsCol1")
        self.diagnosticsCol1.setMinimumSize(QSize(250, 60))
        self.diagnosticsCol1.setMaximumSize(QSize(250, 16777215))
        self.diagnosticsCol1.setStyleSheet(u"/*border-left: 6px solid rgb(21, 23, 27); */\n"
"background-color: rgb(21, 23, 27);")
        self.diagnosticsCol1.setFrameShape(QFrame.NoFrame)
        self.diagnosticsCol1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.diagnosticsCol1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.diagnosticsRow11 = QFrame(self.diagnosticsCol1)
        self.diagnosticsRow11.setObjectName(u"diagnosticsRow11")
        self.diagnosticsRow11.setMinimumSize(QSize(0, 500))
        self.diagnosticsRow11.setStyleSheet(u"QFrame {\n"
"	background: transparent;\n"
"	border: None;\n"
"}\n"
"QFrame QPushButton {\n"
"	border: 2px solid rgb(0, 204, 255);\n"
"	border-radius: 20px;\n"
"	background-color: transparent;\n"
"}\n"
"QFrame QPushButton:hover {\n"
"	background-color: rgb(0, 49, 61);\n"
"}\n"
"QFrame QPushButton:pressed {\n"
"	background-color: rgb(0, 49, 61);\n"
"}")
        self.btn_experiment_load = QPushButton(self.diagnosticsRow11)
        self.btn_experiment_load.setObjectName(u"btn_experiment_load")
        self.btn_experiment_load.setGeometry(QRect(10, 60, 211, 41))
        self.btn_experiment_load.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        iconThemeName = u"system-help"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.btn_experiment_load.setIcon(icon5)
        self.btn_actors_connect = QPushButton(self.diagnosticsRow11)
        self.btn_actors_connect.setObjectName(u"btn_actors_connect")
        self.btn_actors_connect.setGeometry(QRect(20, 200, 181, 26))
        self.pushButton_5 = QPushButton(self.diagnosticsRow11)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 300, 181, 26))
        self.pushButton_6 = QPushButton(self.diagnosticsRow11)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 220, 181, 26))
        self.pushButton_7 = QPushButton(self.diagnosticsRow11)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(20, 240, 181, 26))
        self.pushButton_8 = QPushButton(self.diagnosticsRow11)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 260, 181, 26))
        self.btn_actors_disconnect = QPushButton(self.diagnosticsRow11)
        self.btn_actors_disconnect.setObjectName(u"btn_actors_disconnect")
        self.btn_actors_disconnect.setGeometry(QRect(20, 280, 181, 26))
        self.btn_experiment_select = QPushButton(self.diagnosticsRow11)
        self.btn_experiment_select.setObjectName(u"btn_experiment_select")
        self.btn_experiment_select.setGeometry(QRect(10, 10, 211, 41))
        self.btn_experiment_select.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_experiment_select.setStyleSheet(u"")
        icon6 = QIcon()
        iconThemeName = u"folder-open"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.btn_experiment_select.setIcon(icon6)
        self.btn_vicon_driver = QPushButton(self.diagnosticsRow11)
        self.btn_vicon_driver.setObjectName(u"btn_vicon_driver")
        self.btn_vicon_driver.setGeometry(QRect(10, 110, 211, 41))

        self.verticalLayout_7.addWidget(self.diagnosticsRow11)

        self.diagnosticsRow12 = QFrame(self.diagnosticsCol1)
        self.diagnosticsRow12.setObjectName(u"diagnosticsRow12")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.diagnosticsRow12.sizePolicy().hasHeightForWidth())
        self.diagnosticsRow12.setSizePolicy(sizePolicy4)
        self.diagnosticsRow12.setStyleSheet(u"background: transparent;\n"
"border: None;")
        self.diagnosticsRow12.setFrameShape(QFrame.StyledPanel)
        self.diagnosticsRow12.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.diagnosticsRow12)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(40, 50, 151, 26))

        self.verticalLayout_7.addWidget(self.diagnosticsRow12)


        self.horizontalLayout_7.addWidget(self.diagnosticsCol1)

        self.diagnosticsCol2 = QFrame(self.diagnostics)
        self.diagnosticsCol2.setObjectName(u"diagnosticsCol2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.diagnosticsCol2.sizePolicy().hasHeightForWidth())
        self.diagnosticsCol2.setSizePolicy(sizePolicy5)
        self.diagnosticsCol2.setMinimumSize(QSize(400, 60))
        self.diagnosticsCol2.setStyleSheet(u"background: transparent;\n"
"")
        self.diagnosticsCol2.setFrameShape(QFrame.NoFrame)
        self.diagnosticsCol2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.diagnosticsCol2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.diagnosticsSubMenu2 = QFrame(self.diagnosticsCol2)
        self.diagnosticsSubMenu2.setObjectName(u"diagnosticsSubMenu2")
        self.diagnosticsSubMenu2.setMinimumSize(QSize(0, 45))
        self.diagnosticsSubMenu2.setStyleSheet(u"background-color: rgb(21, 23, 27);")
        self.btn_diagnostics_ugvs = QPushButton(self.diagnosticsSubMenu2)
        self.btn_diagnostics_ugvs.setObjectName(u"btn_diagnostics_ugvs")
        self.btn_diagnostics_ugvs.setGeometry(QRect(90, 0, 73, 45))
        self.btn_diagnostics_ugvs.setMinimumSize(QSize(0, 45))
        self.btn_diagnostics_ugvs.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_diagnostics_ugvs.setStyleSheet(u"")
        self.btn_diagnostics_uavs = QPushButton(self.diagnosticsSubMenu2)
        self.btn_diagnostics_uavs.setObjectName(u"btn_diagnostics_uavs")
        self.btn_diagnostics_uavs.setGeometry(QRect(163, 0, 72, 45))
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_diagnostics_uavs.sizePolicy().hasHeightForWidth())
        self.btn_diagnostics_uavs.setSizePolicy(sizePolicy6)
        self.btn_diagnostics_uavs.setMinimumSize(QSize(0, 45))
        self.btn_diagnostics_uavs.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_diagnostics_uavs.setStyleSheet(u"")
        self.btn_diagnostics_sensors = QPushButton(self.diagnosticsSubMenu2)
        self.btn_diagnostics_sensors.setObjectName(u"btn_diagnostics_sensors")
        self.btn_diagnostics_sensors.setGeometry(QRect(-1, 0, 91, 45))
        self.btn_diagnostics_sensors.setMinimumSize(QSize(0, 45))
        self.btn_diagnostics_sensors.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_diagnostics_sensors.setStyleSheet(u"")
        self.btn_diagnostics_refresh = QPushButton(self.diagnosticsSubMenu2)
        self.btn_diagnostics_refresh.setObjectName(u"btn_diagnostics_refresh")
        self.btn_diagnostics_refresh.setGeometry(QRect(680, 0, 87, 45))
        self.btn_diagnostics_refresh.setMinimumSize(QSize(0, 45))
        self.btn_diagnostics_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_diagnostics_refresh.setStyleSheet(u"")
        self.btn_diagnostics_refresh.setCheckable(False)
        self.btn_diagnostics_refresh.setAutoDefault(False)

        self.verticalLayout_21.addWidget(self.diagnosticsSubMenu2)

        self.verticalFrame_2 = QFrame(self.diagnosticsCol2)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalLayout_22 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.diagnosticsStackedWidget = QStackedWidget(self.verticalFrame_2)
        self.diagnosticsStackedWidget.setObjectName(u"diagnosticsStackedWidget")
        sizePolicy3.setHeightForWidth(self.diagnosticsStackedWidget.sizePolicy().hasHeightForWidth())
        self.diagnosticsStackedWidget.setSizePolicy(sizePolicy3)
        self.diagnosticsSensors = QWidget()
        self.diagnosticsSensors.setObjectName(u"diagnosticsSensors")
        sizePolicy3.setHeightForWidth(self.diagnosticsSensors.sizePolicy().hasHeightForWidth())
        self.diagnosticsSensors.setSizePolicy(sizePolicy3)
        self.diagnosticsSensors.setMinimumSize(QSize(748, 732))
        self.verticalLayout_23 = QVBoxLayout(self.diagnosticsSensors)
        self.verticalLayout_23.setSpacing(6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(18, 9, 9, 9)
        self.diagnosticsSensorsScrollArea = QScrollArea(self.diagnosticsSensors)
        self.diagnosticsSensorsScrollArea.setObjectName(u"diagnosticsSensorsScrollArea")
        self.diagnosticsSensorsScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.diagnosticsSensorsScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.diagnosticsSensorsScrollArea.setWidgetResizable(True)
        self.diagnosticsSensorsScrollAreaContent = QWidget()
        self.diagnosticsSensorsScrollAreaContent.setObjectName(u"diagnosticsSensorsScrollAreaContent")
        self.diagnosticsSensorsScrollAreaContent.setGeometry(QRect(0, 0, 711, 712))
        self.verticalLayout_28 = QVBoxLayout(self.diagnosticsSensorsScrollAreaContent)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 18, 18, 18)
        self.diagnosticsSensorsLayout = QGridLayout()
        self.diagnosticsSensorsLayout.setSpacing(9)
        self.diagnosticsSensorsLayout.setObjectName(u"diagnosticsSensorsLayout")
        self.diagnosticsSensorsLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_28.addLayout(self.diagnosticsSensorsLayout)

        self.diagnosticsSensorsScrollArea.setWidget(self.diagnosticsSensorsScrollAreaContent)

        self.verticalLayout_23.addWidget(self.diagnosticsSensorsScrollArea)

        self.diagnosticsStackedWidget.addWidget(self.diagnosticsSensors)
        self.diagnosticsTEST = QWidget()
        self.diagnosticsTEST.setObjectName(u"diagnosticsTEST")
        self.gridLayout_6 = QGridLayout(self.diagnosticsTEST)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.diagnosticsStackedWidget.addWidget(self.diagnosticsTEST)
        self.diagnosticsUGVs = QWidget()
        self.diagnosticsUGVs.setObjectName(u"diagnosticsUGVs")
        sizePolicy3.setHeightForWidth(self.diagnosticsUGVs.sizePolicy().hasHeightForWidth())
        self.diagnosticsUGVs.setSizePolicy(sizePolicy3)
        self.diagnosticsUGVs.setMinimumSize(QSize(748, 732))
        self.verticalLayout_25 = QVBoxLayout(self.diagnosticsUGVs)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(18, 9, 9, 9)
        self.diagnosticsUGVsScrollArea = QScrollArea(self.diagnosticsUGVs)
        self.diagnosticsUGVsScrollArea.setObjectName(u"diagnosticsUGVsScrollArea")
        self.diagnosticsUGVsScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.diagnosticsUGVsScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.diagnosticsUGVsScrollArea.setWidgetResizable(True)
        self.diagnosticsUGVsScrollAreaContent = QWidget()
        self.diagnosticsUGVsScrollAreaContent.setObjectName(u"diagnosticsUGVsScrollAreaContent")
        self.diagnosticsUGVsScrollAreaContent.setGeometry(QRect(0, 0, 90, 38))
        self.verticalLayout_26 = QVBoxLayout(self.diagnosticsUGVsScrollAreaContent)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 18, 18, 18)
        self.diagnosticsUGVsLayout = QGridLayout()
        self.diagnosticsUGVsLayout.setSpacing(9)
        self.diagnosticsUGVsLayout.setObjectName(u"diagnosticsUGVsLayout")

        self.verticalLayout_26.addLayout(self.diagnosticsUGVsLayout)

        self.diagnosticsUGVsScrollArea.setWidget(self.diagnosticsUGVsScrollAreaContent)

        self.verticalLayout_25.addWidget(self.diagnosticsUGVsScrollArea)

        self.diagnosticsStackedWidget.addWidget(self.diagnosticsUGVs)
        self.diagnosticsUAVs = QWidget()
        self.diagnosticsUAVs.setObjectName(u"diagnosticsUAVs")
        sizePolicy3.setHeightForWidth(self.diagnosticsUAVs.sizePolicy().hasHeightForWidth())
        self.diagnosticsUAVs.setSizePolicy(sizePolicy3)
        self.diagnosticsUAVs.setMinimumSize(QSize(748, 732))
        self.verticalLayout_24 = QVBoxLayout(self.diagnosticsUAVs)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(18, 9, 9, 9)
        self.diagnosticsUAVsScrollArea = QScrollArea(self.diagnosticsUAVs)
        self.diagnosticsUAVsScrollArea.setObjectName(u"diagnosticsUAVsScrollArea")
        self.diagnosticsUAVsScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.diagnosticsUAVsScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.diagnosticsUAVsScrollArea.setWidgetResizable(True)
        self.diagnosticsUAVsScrollAreaContent = QWidget()
        self.diagnosticsUAVsScrollAreaContent.setObjectName(u"diagnosticsUAVsScrollAreaContent")
        self.diagnosticsUAVsScrollAreaContent.setGeometry(QRect(0, 0, 729, 736))
        self.verticalLayout_27 = QVBoxLayout(self.diagnosticsUAVsScrollAreaContent)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 18, 18, 18)
        self.diagnosticsUAVsLayout = QGridLayout()
        self.diagnosticsUAVsLayout.setSpacing(9)
        self.diagnosticsUAVsLayout.setObjectName(u"diagnosticsUAVsLayout")

        self.verticalLayout_27.addLayout(self.diagnosticsUAVsLayout)

        self.diagnosticsUAVsScrollArea.setWidget(self.diagnosticsUAVsScrollAreaContent)

        self.verticalLayout_24.addWidget(self.diagnosticsUAVsScrollArea)

        self.diagnosticsStackedWidget.addWidget(self.diagnosticsUAVs)

        self.verticalLayout_22.addWidget(self.diagnosticsStackedWidget)


        self.verticalLayout_21.addWidget(self.verticalFrame_2)


        self.verticalLayout_14.addLayout(self.verticalLayout_21)


        self.horizontalLayout_7.addWidget(self.diagnosticsCol2)

        self.diagnosticsCol3 = QFrame(self.diagnostics)
        self.diagnosticsCol3.setObjectName(u"diagnosticsCol3")
        self.diagnosticsCol3.setMinimumSize(QSize(500, 60))
        self.diagnosticsCol3.setMaximumSize(QSize(500, 16777215))
        self.diagnosticsCol3.setStyleSheet(u"background-color: rgb(13, 16, 21);\n"
"/*border-left: 6px solid rgb(21, 23, 27);*/")
        self.diagnosticsCol3.setFrameShape(QFrame.NoFrame)
        self.diagnosticsCol3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.diagnosticsCol3)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 5)
        self.diagnosticsTerminal = QPlainTextEdit(self.diagnosticsCol3)
        self.diagnosticsTerminal.setObjectName(u"diagnosticsTerminal")
        self.diagnosticsTerminal.setStyleSheet(u"border: None;\n"
"background: transparent;\n"
"")
        self.diagnosticsTerminal.setFrameShape(QFrame.NoFrame)
        self.diagnosticsTerminal.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.diagnosticsTerminal.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.diagnosticsTerminal.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.diagnosticsTerminal)


        self.horizontalLayout_7.addWidget(self.diagnosticsCol3)

        self.stackedWidget.addWidget(self.diagnostics)
        self.test = QWidget()
        self.test.setObjectName(u"test")
        self.test.setMinimumSize(QSize(1198, 623))
        self.test.setAutoFillBackground(False)
        self.verticalLayout_20 = QVBoxLayout(self.test)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.stackedWidget.addWidget(self.test)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(u"background-color: rgb(21, 23, 27);")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setStyleSheet(u"color: rgb(221, 221, 221)")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.diagnosticsStackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"mess2", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"ace lab @ wpi", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_diagnostics.setText(QCoreApplication.translate("MainWindow", u"Diagnostics", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8be9fd;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Modular Experiment Software System 2", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.btn_experiment_load.setText(QCoreApplication.translate("MainWindow", u"    Load Experiment File  ", None))
        self.btn_actors_connect.setText(QCoreApplication.translate("MainWindow", u"Connect to all Actors", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Start ROS2 Sensor Drivers", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Stop ROS2 Sensor Drivers", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Start ROS2 Actor Servers", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Stop ROS2 Actor Servers", None))
        self.btn_actors_disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect from all Actors", None))
        self.btn_experiment_select.setText(QCoreApplication.translate("MainWindow", u"    Select Experiment File", None))
        self.btn_vicon_driver.setText(QCoreApplication.translate("MainWindow", u"Start VICON Driver", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Abort Experiment", None))
        self.btn_diagnostics_ugvs.setText(QCoreApplication.translate("MainWindow", u"UGVs", None))
        self.btn_diagnostics_uavs.setText(QCoreApplication.translate("MainWindow", u"UAVs", None))
        self.btn_diagnostics_sensors.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.btn_diagnostics_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Marina J. Nelson", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.8", None))
    # retranslateUi

