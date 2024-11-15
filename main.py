
import sys
import os
import platform
import threading
import yaml

from modules import *
from widgets import *
from modules.custom.imports import *
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
        
        # thread pool
        self.threadpool = QThreadPool.globalInstance()
        self.threadpool.maxThreadCount = 20



        # diagnostics submenu 1
        widgets.diagnosticsSubmenu1.setAlignment(Qt.AlignTop)
        widgets.btn_experiment_select.clicked.connect(self.mess2_experiment_select)
        widgets.btn_experiment_load.clicked.connect(self.mess2_experiment_load)
        widgets.btn_experiment_abort.clicked.connect(self.mess2_experiment_abort)

        self.experiment_file_extensions: str = ".yaml (*.yaml)"
        self.experiment_file_path: str = None
        self.experiment_file_content = None
        
        self.experiment_name = None
        self.is_experiment_loaded = False

        # diagnostics sensors
        widgets.diagnosticsSensorsLayout.setAlignment(Qt.AlignTop)
        self.diagnostics_grid_sensors = Obj_gridDiagnosticsLayout(2)
        self.diagnostics_sensors = []

        # diagnostics ugvs
        widgets.diagnosticsUGVsLayout.setAlignment(Qt.AlignTop)
        self.diagnsotics_grid_ugvs = Obj_gridDiagnosticsLayout(2)
        self.diagnostics_actors_ugvs = []

        # diagnostics uavs
        widgets.diagnosticsUAVsLayout.setAlignment(Qt.AlignTop)
        self.diagnsotics_grid_uavs = Obj_gridDiagnosticsLayout(2)
        self.diagnostics_actors_uavs = []

        # diagnostics update network connection icons worker
        self.diagnostics_timer_device_network_connections = QTimer()
        self.diagnostics_timer_device_network_connections.timeout.connect(self.mess2_check_network_and_ssh_connections)
        self.diagnostics_timer_device_network_connections.start(5000)



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

            if self.experiment_name is None and experiment_name != "":
                self.experiment_name = experiment_name
                self.mess2_load_sensors()
                self.mess2_load_actors()
                self.is_experiment_loaded = True
                UIFunctions.mess2_log_to_diagnostics(self, f"loaded experiment {self.experiment_name}")

            elif self.experiment_name is not None and experiment_name != "" and experiment_name != self.experiment_name:
                self.experiment_name = experiment_name
                self.mess2_remove_sensors()
                self.mess2_remove_actors()
                self.mess2_load_sensors()
                self.mess2_load_actors()
                self.is_experiment_loaded = True
                UIFunctions.mess2_log_to_diagnostics(self, f"loaded experiment {self.experiment_name}")

            elif experiment_name == "":
                UIFunctions.mess2_log_to_diagnostics(self, f"experiment file {self.experiment_file_path} is invalid")

            elif experiment_name == self.experiment_name:
                UIFunctions.mess2_log_to_diagnostics(self, f"experiment file {self.experiment_file_path} was already loaded")


    def mess2_add_sensor(self, type: str = "sensor", name: str = "", ip: str = "", username: str = "ubuntu", password: str = "1234", port: int = -1):
        """
        
        """
        index_row = self.diagnostics_grid_sensors.get_index_row()
        index_col = self.diagnostics_grid_sensors.get_index_col()
        if name == "":
            name = f"blankSensor_{index_row}_{index_col}"
        sensor = Device(
            type=type, name=name, ip=ip, username=username, password=password, port=port
        )
        if type != "":
            self.diagnostics_sensors.append(sensor)
            widgets.diagnosticsSensorsLayout.addWidget(sensor.widget, index_row, index_col)
    

    def mess2_remove_sensor(self, sensor: Device):
        """
        
        """
        widgets.diagnosticsSensorsLayout.removeWidget(sensor.widget)
        sensor.widget.deleteLater()


    def mess2_remove_sensors(self):
        """
        
        """
        for sensor in self.diagnostics_sensors:
            self.mess2_remove_sensor(sensor)
        self.diagnostics_sensors.clear()
        self.diagnostics_grid_sensors.__reset__()
    

    def mess2_load_sensors(self):
        """
        This method loads the sensor diagnostics gui elements from a preconfigured experiment .yaml file.
        """
        if "sensors" in self.experiment_file_content:
            for sensor in self.experiment_file_content["sensors"]:
                type = sensor.get("type", "")
                name = sensor.get("name", "")
                ip = sensor.get("ip", "")
                assert(type != "" and type != None)
                assert(name != "" and name != None)

                username = sensor.get("username", "ubuntu")
                password = sensor.get("password", "1234")
                port = sensor.get("port")
                assert(username != "")

                self.mess2_add_sensor(
                    type=type, name=name, ip=ip, username=username, password=password, port=port
                )
                if type == "vicon":
                    self.mess2_add_sensor(type="")  # add empty tile next to vicon ;) so it has its own row


    def mess2_add_actor_ugv(self, type: str = "ugv", name: str = "", ip: str = "", username: str = "ubuntu", password: str = "1234", port: int = -1):
        """
        
        """
        index_row = self.diagnsotics_grid_ugvs.get_index_row()
        index_col = self.diagnsotics_grid_ugvs.get_index_col()
        actor = Device(
            type=type, name=name, ip=ip, username=username, password=password, port=port
        )
        self.diagnostics_actors_ugvs.append(actor)
        widgets.diagnosticsUGVsLayout.addWidget(actor.widget, index_row, index_col)
    

    def mess2_remove_actor_ugv(self, actor: Device):
        """

        """
        widgets.diagnosticsUGVsLayout.removeWidget(actor.widget)
        actor.widget.deleteLater()


    def mess2_add_actor_uav(self, type: str = "ugv", name: str = "", ip: str = "", username: str = "ubuntu", password: str = "1234", port: int = -1):
        """
        
        """
        index_row = self.diagnsotics_grid_uavs.get_index_row()
        index_col = self.diagnsotics_grid_uavs.get_index_col()
        actor = Device(
            type=type, name=name, ip=ip, username=username, password=password, port=port
        )
        self.diagnostics_actors_uavs.append(actor)
        widgets.diagnosticsUAVsLayout.addWidget(actor.widget, index_row, index_col)
    

    def mess2_remove_actor_uav(self, actor: Device):
        """

        """
        widgets.diagnosticsUAVsLayout.removeWidget(actor.widget)
        actor.widget.deleteLater()

    
    def mess2_remove_actors(self):
        """
        
        """
        for actor in self.diagnostics_actors_ugvs:
            self.mess2_remove_actor_ugv(actor)
        self.diagnostics_actors_ugvs.clear()
        self.diagnsotics_grid_ugvs.__reset__()
        for actor in self.diagnostics_actors_uavs:
            self.mess2_remove_actor_uav(actor)
        self.diagnostics_actors_uavs.clear()
        self.diagnsotics_grid_uavs.__reset__()


    def mess2_load_actors(self):
        """
        Loads the ugv and uav actor diagnostics gui elements from a preconfigured experiment .yaml file.
        """
        if "actors" in self.experiment_file_content:
            for actor in self.experiment_file_content["actors"]:
                type = actor.get("type", "")
                name = actor.get("name", "")
                ip = actor.get("ip", "")
                assert(type != "" and type != None)
                assert(name != "" and name != None)

                username = actor.get("username", "ubuntu")
                password = actor.get("password", "1234")
                port = actor.get("port")
                assert(username != "")

                if type == "ugv":
                    self.mess2_add_actor_ugv(
                        type=type, name=name, ip=ip, username=username, password=password, port=port
                    )
                elif type == "uav":
                    self.mess2_add_actor_uav(
                        type=type, name=name, ip=ip, username=username, password=password, port=port
                    )


    def mess2_check_network_and_ssh_connections(self):
        """
        Checks network connections for sensors, ugvs, and uavs.
        """
        worker = WorkerDeviceUI(
            self.diagnostics_sensors,
            self.diagnostics_actors_ugvs + self.diagnostics_actors_uavs
        )
        self.threadpool.start(worker)


    def mess2_experiment_abort(self):
        """
        """
        if self.is_experiment_running == True:
            UIFunctions.mess2_log_to_diagnostics(self, f"aborting experiment {self.experiment_name}")
            UIFunctions.mess2_log_to_diagnostics(self, f"aborted experiment {self.experiment_name}")




def main():
    """
    This function runs the application.
    """
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
