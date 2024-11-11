
import sys
import os
import platform
import threading

from modules import *
from widgets import *
from modules.diagnostics import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

widgets = None


class MainWindow(QMainWindow):
    """
    """
    def __init__(self):
        """
        """
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        title = "mess2"
        description = "Modular Experiment Software System 2"
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, False))
        UIFunctions.uiDefinitions(self)
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_diagnostics.clicked.connect(self.buttonClick)
        widgets.btn_planner.clicked.connect(self.buttonClick)
        widgets.btn_settings.clicked.connect(self.buttonClick)

        # DIAGNOSTICS TAB
        # ///////////////////////////////////////////////////////////////

        # DIAGNOSTICS MENU
        widgets.btn_experiment_select.clicked.connect(self.buttonClick)
        widgets.btn_experiment_load.clicked.connect(self.buttonClick)
        widgets.btn_actors_connect.clicked.connect(self.buttonClick)
        widgets.btn_actors_disconnect.clicked.connect(self.buttonClick)

        self.enable_click_logging_while_experiment_running = False
        self.is_experiment_running: bool = False
        self.experiment_file_extensions: str = "test1 (*.yaml *.png);; test2 (*.png *.csv)"
        self.experiment_file_path: str = None

        # DIAGNOSTICS SUBMENU 2
        widgets.btn_diagnostics_sensors.clicked.connect(self.buttonClick)
        widgets.btn_diagnostics_ugvs.clicked.connect(self.buttonClick)
        widgets.btn_diagnostics_uavs.clicked.connect(self.buttonClick)
        widgets.btn_diagnostics_refresh.clicked.connect(self.buttonClick)

        # VICON CONNECTIVITY
        # self.sensor_vicon = SensorVICON(name="VICON Valkyrie Motion Capture System", btnName=widgets.btnVICON_11.objectName())
        # self.sensors_flir = []
        # widgets.btnVICON_11.clicked.connect(self.buttonClick)

        # ///////////////////////////////////////////////////////////////
        self.threadpool = QThreadPool()
        self.threadpool.maxThreadCount = 4






        # diagnostics sensors
        widgets.diagnosticsSensorsLayout.setAlignment(Qt.AlignTop)
        self.grid_diagnostics_sensors = Obj_gridWidget(2)
        self.mess2_initialize_vicon()

        
        widgets.diagnosticsUGVsLayout.setAlignment(Qt.AlignTop)
        widgets.diagnosticsUAVsLayout.setAlignment(Qt.AlignTop)
        




        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        UIFunctions.mess2_log_to_diagnostics(self, "launched mess2")

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes/py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        widgets.btn_diagnostics_sensors.setStyleSheet(UIFunctions.selectStyleDiagnosticsSubMenu2(widgets.btn_diagnostics_sensors.styleSheet()))
        widgets.diagnosticsStackedWidget.setCurrentWidget(widgets.diagnosticsSensors)


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # LOG CLICK IN LINUX TERMINAL
        print(f"buttonClick : pressed {btnName}")


        # SHOW HOME PAGE
        if btnName == "btn_home":
            if self.is_experiment_running:
                self.logExperimentRunningEvent(self, btnName)
            else:
                widgets.stackedWidget.setCurrentWidget(widgets.home)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))



        # DIAGNOSTICS
        # ///////////////////////////////////////////////////////////////////////////


        # SHOW DIAGNOSTICS PAGE
        if btnName == "btn_diagnostics":
            if self.is_experiment_running:
                self.logExperimentRunningEvent(self, btnName)
            else:
                widgets.stackedWidget.setCurrentWidget(widgets.diagnostics)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
                widgets.diagnosticsTerminal.verticalScrollBar().setValue(widgets.diagnosticsTerminal.verticalScrollBar().maximum())


        # DIAGNOSTICS SUBMENU1
        if btnName == "btn_experiment_select":
            if self.is_experiment_running:
                self.logExperimentRunningEvent(self, btnName)
            else:
                self.selectExperimentEvent()



        # DIAGNOSTICS SENSORS TAB
        if btnName == "btn_diagnostics_sensors":
            widgets.diagnosticsStackedWidget.setCurrentWidget(widgets.diagnosticsSensors)
            UIFunctions.resetStyleDiagnosticsSubMenu2(self, btnName)
            btn.setStyleSheet(UIFunctions.selectStyleDiagnosticsSubMenu2(btn.styleSheet()))


        # DIAGNOSTICS UGVS TAB
        if btnName == "btn_diagnostics_ugvs":
            widgets.diagnosticsStackedWidget.setCurrentWidget(widgets.diagnosticsUGVs)
            UIFunctions.resetStyleDiagnosticsSubMenu2(self, btnName)
            btn.setStyleSheet(UIFunctions.selectStyleDiagnosticsSubMenu2(btn.styleSheet()))


        # DIAGNOSTICS UAVS TAB
        if btnName == "btn_diagnostics_uavs":
            widgets.diagnosticsStackedWidget.setCurrentWidget(widgets.diagnosticsUAVs)
            UIFunctions.resetStyleDiagnosticsSubMenu2(self, btnName)
            btn.setStyleSheet(UIFunctions.selectStyleDiagnosticsSubMenu2(btn.styleSheet()))
        






        if btnName == "btn_actors_connect":
            new_button = QPushButton("Dynamically Added")
            new_button.setObjectName("dynamic_button")
            new_button.setStyleSheet("background-color: lightblue;")
            self.ui.diagnosticsCol2Layout.addWidget(new_button)
            new_button.clicked.connect(lambda: print("Dynamically added button clicked!"))

        
        print(f"clicked {btnName}")


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('mouseClick : left click')
        if event.buttons() == Qt.RightButton:
            print('mouseClick : right click')

    
    # BUTTON EVENTS
    # ///////////////////////////////////////////////////////////////
    def logExperimentRunningEvent(self, btnName: str):
        """
        """
        if self.enable_click_logging_while_experiment_running:
                    UIFunctions.mess2_log_to_diagnostics(f"buttonClick : cannot press {btnName} while experiment is running")


    def selectExperimentEvent(self):
        """
        """
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select a file",
            dir=os.getcwd(),
            filter=self.experiment_file_extensions
        )
        experiment_file_path, _ = response
        if experiment_file_path:
            self.experiment_file_path = experiment_file_path
            UIFunctions.mess2_log_to_diagnostics(self, f"selected experiment file {self.experiment_file_path}")
    

    def createSensorVICONEvent(self):
        """
        """
        if self.sensor_vicon:
            pass


    def toggleSensorVICONEvent(self):
        """
        """
        if not self.sensor_vicon.is_connected:
            UIFunctions.toggleStyleConnected(self, self.sensor_vicon.frameNameConnected, True)
            UIFunctions.toggleStyleOnline(self, self.sensor_vicon.frameNameOnline, True)
            self.sensor_vicon.is_connected = True
        # if not self.sensor_vicon.is_running









    # CUSTOM CODE
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # def mess2_create_grid(self, n_cols: int = 2, n_rows: int = None):
    #     """
    #     This method initializes 
    #     """



    # def mess2_create_sensor(self):
    def mess2_add_sensor(self, widget: QWidget, widget_name: str, index_row: int, index_col: int):
        """
        This method adds a sensor template widget to the diagnostics sensors grid layout at the specified row and column index.
        """
        widgets.diagnosticsSensorsLayout.addWidget(widget, index_row, index_col)
        if widget_name == None:
            widget_name = f"diagnosticsSensorsLayoutGrid_{index_row}_{index_col}"
        widgets.__setattr__(widget_name, widget)


    def mess2_create_sensor(self, sensor: Obj_tileSensorTemplate):
        """
        This method creates a sensor template widget and updates its attributes using a sensor object.
        """
        widget = QWidget()
        widget.setObjectName(sensor.widget_name)
        ui = Ui_tileSensorTemplate()
        ui.setupUi(widget)

        ui.sensorName.setText(sensor.sensor_name)


        return widget
    

    def mess2_initialize_vicon(self):
        """
        
        """
        vicon_sensor = Obj_tileSensorTemplate("VICON Valkyrie Motion Capture System", "192.168.0.145", "sensorVICON", False, True)
        print(vicon_sensor.show_online)
        vicon_widget = self.mess2_create_sensor(vicon_sensor)

        self.mess2_add_sensor(vicon_widget, vicon_widget.objectName(), self.grid_diagnostics_sensors.get_index_row(), self.grid_diagnostics_sensors.get_index_col())
        self.mess2_add_sensor(QWidget(), None, self.grid_diagnostics_sensors.get_index_row(), self.grid_diagnostics_sensors.get_index_col())

        UIFunctions.mess2_toggle_connected(self, vicon_widget.objectName(), vicon_sensor)
        UIFunctions.mess2_toggle_online(self, vicon_widget.objectName(), vicon_sensor)
        UIFunctions.mess2_log_to_diagnostics(self, "added vicon diagnostics to sensors")



#######################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
