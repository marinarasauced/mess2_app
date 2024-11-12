
import sys
import os
import platform
import threading
import yaml

from modules import *
from widgets import *
from modules.ui_diagnostics import *
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
        # widgets.btn_experiment_select.clicked.connect(self.buttonClick)
        # widgets.btn_experiment_load.clicked.connect(self.buttonClick)
        # widgets.btn_actors_connect.clicked.connect(self.buttonClick)
        # widgets.btn_actors_disconnect.clicked.connect(self.buttonClick)

        self.enable_click_logging_while_experiment_running = False
        self.is_experiment_running: bool = False
        

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



        # diagnostics submenu 1
        widgets.btn_experiment_select.clicked.connect(self.mess2_experiment_select)
        widgets.btn_experiment_load.clicked.connect(self.mess2_experiment_load)

        self.experiment_file_extensions: str = ".yaml (*.yaml)"
        self.experiment_file_path: str = None
        self.experiment_file_content = None
        
        self.experiment_name = None
        self.is_experiment_loaded = False

        self.experiment_widgets_sensors = []

        # diagnostics sensors
        widgets.diagnosticsSensorsLayout.setAlignment(Qt.AlignTop)
        self.grid_diagnostics_sensors = Obj_gridWidget(2)
        # self.mess2_initialize_vicon()

        
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
    def mess2_experiment_select(self):
        """
        This method creates a 
        """
        if not self.is_experiment_running:
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


    def mess2_experiment_load(self):
        """
        This method loads the gui elements of a preconfigured experiment .yaml file and creates backend object instances needed to run an experiment.
        """
        if self.is_experiment_running:
            UIFunctions.mess2_log_to_diagnostics(self, "unable to load experiment file while experiment is running")
        elif self.experiment_file_path is None:
            UIFunctions.mess2_log_to_diagnostics(self, "unable to load exeperiment file while no experiment is selected")
        else:
            with open(self.experiment_file_path, "r") as file:
                self.experiment_file_content = yaml.safe_load(file)
            experiment_name = self.experiment_file_content.get("experiment_name", "")
            print(experiment_name)
            if self.experiment_name is None and experiment_name != "":
                self.experiment_name = experiment_name
                self.mess2_experiment_load_sensors_gui()
            elif self.experiment_name is not None and experiment_name != "" and experiment_name != self.experiment_name:
                self.experiment_name = experiment_name
                self.mess2_experiment_clear_sensors_gui()
                self.mess2_experiment_load_sensors_gui()
            elif experiment_name == "":
                UIFunctions.mess2_log_to_diagnostics(self, f"experiment file {self.experiment_file_path} is invalid")
            elif experiment_name == self.experiment_name:
                UIFunctions.mess2_log_to_diagnostics(self, f"experiment file {self.experiment_file_path} was already loaded")

    
    def mess2_experiment_clear_sensors_gui(self):
        """
        
        """
        is_empty = False
        if self.experiment_widgets_sensors == []:
            is_empty = True
        for widget in self.experiment_widgets_sensors:
            widgets.diagnosticsSensorsLayout.removeWidget(widget)
            print(widget.objectName())
            widgets.__delattr__(widget.objectName())
            widget.deleteLater()
        self.experiment_widgets_sensors.clear()
        if not is_empty:
            UIFunctions.mess2_log_to_diagnostics(self, "removed gui elements for experiment sensors from previous experiment")


    def mess2_experiment_load_sensors_gui(self):
        """
        This method loads the sensor diagnostics gui elements from a preconfigured experiment .yaml file.
        """
        if "sensors" in self.experiment_file_content:
            # UIFunctions.mess2_log_to_diagnostics(self, "creating gui elements for experiment sensors")
            for sensor in self.experiment_file_content["sensors"]:
                # if type == "vicon":
                #     self.mess2_initialize_vicon()
                name = sensor.get("name", "")
                assert(name != "")

                ip = sensor.get("ip", "")
                show_connected = sensor.get("show_connected", False)
                show_online = sensor.get("show_online", False)

                sensor_object = self.mess2_create_sensor_gui_object(name, ip, show_connected, show_online)
                sensor_widget = self.mess2_create_sensor_gui_widget(sensor_object)

                index_row = self.grid_diagnostics_sensors.get_index_row()
                index_col = self.grid_diagnostics_sensors.get_index_col()
                self.mess2_add_sensor_gui_widget(sensor_widget, index_row, index_col)
                # UIFunctions.mess2_log_to_diagnostics(self, f"created gui element for experiment sensor {sensor_object.widget_name}")
                type = sensor.get("type", "")
                if type == "vicon":
                    index_row = self.grid_diagnostics_sensors.get_index_row()
                    index_col = self.grid_diagnostics_sensors.get_index_col()
                    empty_widget = self.mess2_create_sensor_gui_widget_empty(index_row, index_col)
                    self.mess2_add_sensor_gui_widget(empty_widget, index_row, index_col)
            UIFunctions.mess2_log_to_diagnostics(self, "created gui elements for experiment sensors")


    
    def mess2_create_sensor_gui_object(self, name: str, ip: str = "", show_connected: bool = False, show_online: bool = False):
        """
        
        """
        assert(name != "")
        sensor_name = name.replace(" ", "_")
        sensor_object = Obj_tileSensorTemplate(name, ip, f"sensor{sensor_name}", show_connected, show_online)
        return sensor_object


    def mess2_create_sensor_gui_widget(self, sensor_object: Obj_tileSensorTemplate):
        """
        
        """
        assert(sensor_object.sensor_name != "" and sensor_object.widget_name != "sensor")

        sensor_widget = QWidget()
        sensor_widget.setObjectName(sensor_object.widget_name)
        ui = Ui_tileSensorTemplate()
        ui.setupUi(sensor_widget)
        ui.sensorName.setText(sensor_object.sensor_name)
        ui.sensorIP.setText(sensor_object.sensor_ip)
        print(sensor_object.widget_name)
        widgets.__setattr__(sensor_object.widget_name, sensor_widget)
        UIFunctions.mess2_toggle_connected_icon(self, sensor_object.widget_name, sensor_object)
        UIFunctions.mess2_toggle_online_icon(self, sensor_object.widget_name, sensor_object)
        # UIFunctions.mess2_log_to_diagnostics(self, f"added {sensor_object.widget_name} as attribute")
        return sensor_widget


    def mess2_create_sensor_gui_widget_empty(self, index_row: int, index_col: int):
        """
        
        """
        name = f"sensorEmpty_{index_row}_{index_col}"
        empty_widget = QWidget()
        empty_widget.setObjectName(name)
        widgets.__setattr__(name, empty_widget)
        return empty_widget

    
    def mess2_add_sensor_gui_widget(self, widget: QWidget, index_row: int, index_col: int):
        """
        
        """
        widgets.diagnosticsSensorsLayout.addWidget(eval(f"self.ui.{widget.objectName()}"), index_row, index_col)
        self.experiment_widgets_sensors.append(widget)
        

            



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
        ui.sensorIP.setText(sensor.sensor_ip)
        return widget
    

    def mess2_initialize_vicon(self):
        """
        
        """
        vicon_sensor = Obj_tileSensorTemplate("VICON Valkyrie Motion Capture System", "192.168.0.145", "sensorVICON", False, True)
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
