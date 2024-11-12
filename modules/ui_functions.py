# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *
from datetime import datetime
from modules.custom.sensor_object import Obj_tileSensorTemplate

# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class UIFunctions(MainWindow):
    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # TOGGLE LEFT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleLeftBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraLeftBox.width()
            widthRightBox = self.ui.extraRightBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            color = Settings.BTN_LEFT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.toggleLeftBox.setStyleSheet(style + color)
                if widthRightBox != 0:
                    style = self.ui.settingsTopBtn.styleSheet()
                    self.ui.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))
                
        UIFunctions.start_box_animation(self, width, widthRightBox, "left")

    # TOGGLE RIGHT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleRightBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraRightBox.width()
            widthLeftBox = self.ui.extraLeftBox.width()
            maxExtend = Settings.RIGHT_BOX_WIDTH
            color = Settings.BTN_RIGHT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.settingsTopBtn.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.settingsTopBtn.setStyleSheet(style + color)
                if widthLeftBox != 0:
                    style = self.ui.toggleLeftBox.styleSheet()
                    self.ui.toggleLeftBox.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

            UIFunctions.start_box_animation(self, widthLeftBox, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0 

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0       

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # /////////////////////////////////////////////////////////////////////////////////

    #     def selectMenu(getStyle):
    #     select = getStyle + Settings.MENU_SELECTED_STYLESHEET
    #     return select

    # # DESELECT
    # def deselectMenu(getStyle):
    #     deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
    #     return deselect

    # # START SELECTION
    # def selectStandardMenu(self, widget):
    #     for w in self.ui.topMenu.findChildren(QPushButton):
    #         if w.objectName() == widget:
    #             w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # # RESET SELECTION
    # def resetStyle(self, widget):
    #     for w in self.ui.topMenu.findChildren(QPushButton):
    #         if w.objectName() != widget:
    #             w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))



    
    def selectStyleDiagnosticsSubMenu2(getStyle):
        """
        
        """
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET_DIAGNOSTICS2
        return select
        # # select = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, Settings.DIAGNOSTICS_SUBMENU2_STYLESHEET_SELECTED)
        # # print(select)
        # return select


    def deselectStyleDiagnosticsSubMenu2(getStyle):
        """
        
        """
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET_DIAGNOSTICS2, "")
        return deselect

    
    def resetStyleDiagnosticsSubMenu2(self, btnName: str):
        """
        
        """
        ignore = ["btn_diagnostics_refresh"]
        for w in self.ui.diagnosticsSubMenu2.findChildren(QPushButton):
            is_same: bool = (w.objectName() == btnName)
            is_ignore: bool = (w.objectName() in ignore)
            if not is_same and not is_ignore:
                w.setStyleSheet(UIFunctions.deselectStyleDiagnosticsSubMenu2(w.styleSheet()))
    




    def toggleStyleConnected(self, frameName, frameBool: bool):
        """
        """
        frame = eval(f"self.ui.{frameName}")
        style = frame.styleSheet()
        if frameBool:
            style = style.replace("disconnected", "connected")
        else:
            style = style.replace("connected", "disconnected")
        frame.setStyleSheet(style)
    

    def toggleStyleOnline(self, frameName: str, frameBool: bool):
        """
        """
        frame = eval(f"self.ui.{frameName}")
        style = frame.styleSheet()
        if frameBool:
            style = style.replace("offline", "online")
        else:
            style = style.replace("online", "offline")
        frame.setStyleSheet(style)




    # def selectMenu(getStyle):
    #     select = getStyle + Settings.MENU_SELECTED_STYLESHEET
    #     return select

    # # DESELECT
    # def deselectMenu(getStyle):
    #     deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
    #     return deselect



    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS

    def mess2_log_to_diagnostics(self, msg: str = ""):
        """
        This method logs strings to the diagnostics terminal with an HH:MM:SS timestamp.
        """
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        message = f"{timestamp} : {msg}"
        self.ui.diagnosticsTerminal.appendPlainText(message)


    def mess2_toggle_connected_icon(self, widget_name: str, sensor: Obj_tileSensorTemplate):
        """
        This method toggles the is_connected ui element of a widget.
        """
        if not sensor.show_connected:
            widget = eval(f"self.ui.{widget_name}")
            style = widget.styleSheet()
            style = style.replace(sensor.style_is_disconnected, "")
            style = style.replace(sensor.style_is_connected, "")
            widget.setStyleSheet(style)


    def mess2_update_connected_icon(self, widget_name: str, sensor: Obj_tileSensorTemplate):
        """
        This method updates the is_connected ui element of a widget.
        """
        widget = eval(f"self.ui.{widget_name}")
        style = widget.styleSheet()
        if sensor.is_connected:
            style.replace(sensor.style_is_disconnected, sensor.style_is_connected)
        else:
            style.replace(sensor.style_is_connected, sensor.style_is_disconnected)
        widget.setStyleSheet(style)


    def mess2_toggle_online_icon(self, widget_name: str, sensor: Obj_tileSensorTemplate):
        """
        This method toggles the is_online ui element of a widget.
        """
        if not sensor.show_online:
            widget = eval(f"self.ui.{widget_name}")
            style = widget.styleSheet()
            style = style.replace(sensor.style_is_offline, "")
            style = style.replace(sensor.style_is_online, "")
            widget.setStyleSheet(style)


    def mess2_update_online_icon(self, widget_name: str, sensor: Obj_tileSensorTemplate):
        """
        This method updates the is_online ui element of a widget.
        """
        widget = eval(f"self.ui.{widget_name}")
        style = widget.styleSheet()
        if sensor.is_online:
            style.replace(sensor.style_is_offline, sensor.style_is_online)
        else:
            style.replace(sensor.style_is_online, sensor.style_is_offline)
        widget.setStyleSheet(style) 