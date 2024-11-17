
import sys
import os
import platform
import threading
import yaml
from datetime import datetime

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

        #
        self.is_experiment_running: bool = False


        # PRIMARY MENU
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_diagnostics.clicked.connect(self.buttonClick)
        widgets.btn_planner.clicked.connect(self.buttonClick)
        widgets.btn_settings.clicked.connect(self.buttonClick)

        # DIAGNOSTICS SUBMENU1
        widgets.btn_experiment_select.clicked.connect(self.experiment_select)
        widgets.btn_experiment_load.clicked.connect(self.experiment_load)

        # DIAGNOSTICS SUBMENU2
        self.diagnostics_content = []
        self.devices_offline = []   # devices off the network (most likely the host machine) that must run ros2 software
        self.devices_remote = []    # devices with ros2 software that must be run on the remote device
        self.devices_local = []     # devices with ros2 software that must be run locally










        # LEFT MENUS
        

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
        # widgets.btn_diagnostics_sensors.clicked.connect(self.buttonClick)
        # widgets.btn_diagnostics_ugvs.clicked.connect(self.buttonClick)
        # widgets.btn_diagnostics_uavs.clicked.connect(self.buttonClick)
        # widgets.btn_diagnostics_refresh.clicked.connect(self.buttonClick)

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
        # widgets.btn_experiment_select.clicked.connect(self.mess2_experiment_select)
        # widgets.btn_experiment_load.clicked.connect(self.mess2_experiment_load)
        # widgets.btn_experiment_abort.clicked.connect(self.mess2_experiment_abort)

        self.experiment_file_extensions: str = ".yaml (*.yaml)"
        self.experiment_file_path: str = None
        self.experiment_file_content = None
        
        self.experiment_name = None
        self.is_experiment_loaded = False

        # widgets.btn_log_save_path_select.clicked.connect(self.mess2_logs_path_select)
        # self.experiment_dir_logs = os.path.abspath(os.path.join(os.getcwd(), "../logs"))
        # widgets.logSavePathText.setText(self.experiment_dir_logs)


        # self.are_actors_ssh_connected = False
        # widgets.btn_ssh_connect.clicked.connect(self.mess2_establish_or_close_ssh_connections)

        # self.are_sensor_nodes_running = False
        # widgets.btn_ros2_sensor_drivers.clicked.connect(self.mess2_start_or_stop_sensor_nodes)

        # self.are_actor_nodes_running = False
        # widgets.btn_ros2_actor_nodes.clicked.connect(self.mess2_start_or_stop_actor_nodes)


        # # diagnostics sensors
        # widgets.diagnosticsSensorsLayout.setAlignment(Qt.AlignTop)
        # self.diagnostics_grid_sensors = Obj_gridDiagnosticsLayout(2)
        # self.diagnostics_sensors = []

        # # diagnostics ugvs
        # widgets.diagnosticsUGVsLayout.setAlignment(Qt.AlignTop)
        # self.diagnsotics_grid_ugvs = Obj_gridDiagnosticsLayout(2)
        # self.diagnostics_actors_ugvs = []

        # # diagnostics uavs
        # widgets.diagnosticsUAVsLayout.setAlignment(Qt.AlignTop)
        # self.diagnsotics_grid_uavs = Obj_gridDiagnosticsLayout(2)
        # self.diagnostics_actors_uavs = []

        # # diagnostics update network connection icons worker
        # self.diagnostics_timer_device_network_connections = QTimer()
        # self.diagnostics_timer_device_network_connections.timeout.connect(self.mess2_check_network_and_ssh_connections)
        # self.diagnostics_timer_device_network_connections.start(5000)


        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        self.diagnostics_log("launched mess2 application")
        
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



    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_home":
            if self.is_experiment_running:
                # self.logExperimentRunningEvent(self, btnName)
                pass
            else:
                widgets.stackedWidget.setCurrentWidget(widgets.home)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_diagnostics":
            if self.is_experiment_running:
                # self.logExperimentRunningEvent(self, btnName)
                pass
            else:
                widgets.stackedWidget.setCurrentWidget(widgets.diagnostics)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
                widgets.diagnosticsTerminal.verticalScrollBar().setValue(widgets.diagnosticsTerminal.verticalScrollBar().maximum())

        # SHOW PLANNER PAGE
        if btnName == "btn_planner":
            if self.is_experiment_running:
                pass
            else:
                pass
        
        # SHOW SETTINGS PAGE
        if btnName == "btn_settings":
            if self.is_experiment_running:
                pass
            else:
                pass


        # # DIAGNOSTICS SENSORS TAB
        # if btnName == "btn_diagnostics_sensors":
        #     widgets.diagnosticsStackedWidget.setCurrentWidget(widgets.diagnosticsSensors)
        #     UIFunctions.resetStyleDiagnosticsSubMenu2(self, btnName)
        #     btn.setStyleSheet(UIFunctions.selectStyleDiagnosticsSubMenu2(btn.styleSheet()))


        # # DIAGNOSTICS UGVS TAB
        # if btnName == "btn_diagnostics_ugvs":
        #     widgets.diagnosticsStackedWidget.setCurrentWidget(widgets.diagnosticsUGVs)
        #     UIFunctions.resetStyleDiagnosticsSubMenu2(self, btnName)
        #     btn.setStyleSheet(UIFunctions.selectStyleDiagnosticsSubMenu2(btn.styleSheet()))


        # # DIAGNOSTICS UAVS TAB
        # if btnName == "btn_diagnostics_uavs":
        #     widgets.diagnosticsStackedWidget.setCurrentWidget(widgets.diagnosticsUAVs)
        #     UIFunctions.resetStyleDiagnosticsSubMenu2(self, btnName)
        #     btn.setStyleSheet(UIFunctions.selectStyleDiagnosticsSubMenu2(btn.styleSheet()))
        






        # if btnName == "btn_actors_connect":
        #     new_button = QPushButton("Dynamically Added")
        #     new_button.setObjectName("dynamic_button")
        #     new_button.setStyleSheet("background-color: lightblue;")
        #     self.ui.diagnosticsCol2Layout.addWidget(new_button)
        #     new_button.clicked.connect(lambda: print("Dynamically added button clicked!"))

        
        # print(f"clicked {btnName}")


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




    # LOG EVENT
    # ///////////////////////////////////////////////////////////////
    def diagnostics_log(self, value: str = ""):
        """
        Logs a string to the diagnostics console as a new line with a time stamp [HH:MM:SS].
        """
        time = datetime.now().strftime("[%H:%M:%S]")
        message = f"{time} : {value}"

        self.ui.diagnosticsTerminal.appendPlainText(message)
        self.ui.diagnosticsTerminal.verticalScrollBar().setValue(self.ui.diagnosticsTerminal.verticalScrollBar().maximum())


    # EXPERIMENT EVENTS
    # ///////////////////////////////////////////////////////////////
    def experiment_select(self):
        """
        Opens a dialogue to select an experiment file. 
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
                self.diagnostics_log(f"selected experiment file {self.experiment_file_path}")
                widgets.experimentFileNameText.setText(self.experiment_file_path)


    def experiment_load(self):
        """
        This method loads the gui elements of a preconfigured experiment .yaml file and creates backend object instances needed to run an experiment.
        """
        if self.is_experiment_running:
            self.diagnostics_log("unable to load experiment file while experiment is running")

        elif self.experiment_file_path is None:
            self.diagnostics_log("unable to load exeperiment file while no experiment is selected")

        else:
            with open(self.experiment_file_path, "r") as file:
                self.experiment_file_content = yaml.safe_load(file)
            
            self.diagnostics_experiment_load(self.experiment_file_content)


    def diagnostics_experiment_clear(self):
        """
        """
        for content in self.diagnostics_content:
        #     for widget in content.layout:
        #         content.layout.removeWidget(widget)
        #         widget.deleteLater()
            widgets.diagnosticsPages2.removeWidget(content.page)
            content.page.deleteLater()
            widgets.diagnosticsSubmenu2ButtonsLeftLayout.removeWidget(content.button)
            content.button.deleteLater()
        self.diagnostics_content.clear()
        self.devices_offline.clear()
        self.devices_local.clear()
        self.devices_remote.clear()


    def diagnostics_experiment_load(self, file):
        """
        """
        counter = 0

        experiment = file.get("experiment", "")
        if experiment == "":
            self.diagnostics_log(f"selected experiment file is invalid")
            return

        name = experiment.get("name", "")
        categories = experiment.get("categories", "")
        if name == "" or categories == "":
            self.diagnostics_log(f"selected experiment file is invalid")
            return
        
        if self.is_experiment_loaded == True and name == self.experiment_name:
            self.diagnostics_log(f"experiment file {self.experiment_file_path} was already loaded")
            return
        
        if self.is_experiment_loaded == True and name != self.experiment_name:
            self.diagnostics_log(f"clearing previously loaded experiment")
            self.diagnostics_experiment_clear()
        
        self.experiment_name = name

        for category in categories:
            content = file.get(category, "")
            if content == "" or content == None:
                self.diagnostics_log(f"selected experiment file is invalid")
                return
            self.__setattr__(f"grid_{category}", Obj_gridDiagnosticsLayout())


        class Content():
            """
            """
            def __init__(self, instance: MainWindow, category: str):
                """
                """
                super().__init__()
                self.instance = instance
                self.category = category

                self.grid = Obj_gridDiagnosticsLayout()

                self.button = QPushButton()
                self.button.setObjectName(f"btn_diagnostics2_{self.category}")
                self.button.setText(self.category)
                self.button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

                self.page = QWidget()
                self.ui = Ui_diagnosticsPage2()
                self.ui.setupUi(self.page)
                self.ui.diagnostics2ScrollAreaLayout.setAlignment(Qt.AlignTop)
                self.page.setObjectName(f"page_diagnostics2_{category}")

                self.button.clicked.connect(self.click)
                self.layout = self.ui.diagnostics2ScrollAreaLayout

                widgets.__setattr__(self.button.objectName(), self.button)
                widgets.__setattr__(self.page.objectName(), self.page)

                widgets.diagnosticsSubmenu2ButtonsLeftLayout.addWidget(self.button)
                widgets.diagnosticsPages2.addWidget(self.page)

                self.is_selected = False


            def select(self):
                """
                """
                style = self.button.styleSheet()
                style = style.replace("", Settings.DIAGNOSTICS_SUBMENU2_STYLE)
                self.button.setStyleSheet(style)

                page = self.instance.ui.diagnosticsPages2.findChild(QWidget, f"{self.page.objectName().replace('btn', 'page')}")
                self.instance.ui.diagnosticsPages2.setCurrentWidget(page)

                self.is_selected = True


            def deselect(self):
                """
                """
                style = self.button.styleSheet()
                style = style.replace(Settings.DIAGNOSTICS_SUBMENU2_STYLE, "")
                self.button.setStyleSheet(style)

                self.is_selected = False
            

            def click(self):
                """
                """
                if self.is_selected == False:
                    for content in self.instance.diagnostics_content:
                        if content.category == self.category:
                            self.select()
                        else:
                            content.deselect()
                

        for category in categories:
            
            # create content instance
            content = Content(self, category)            
            self.diagnostics_content.append(content)
            
            # create devices
            devices = file.get(category, "")
            for device in devices:
                device_type = device.get("type", "")
                device_name = device.get("name", "")
                device_ip = device.get("ip", "")
                device_username = device.get("username", "ubuntu")
                device_password = device.get("password", "1234")
                enable_network = device.get("enable_network", False)
                enable_ssh = device.get("enable_ssh", False)
                enable_battery = device.get("enable_battery", False)

                device_ = Device(
                    type=device_type,
                    name=device_name,
                    ip=device_ip,
                    username=device_username,
                    password=device_password,
                    logger=self.ui.diagnosticsTerminal,
                    threadpool=self.threadpool,
                    enable_network=enable_network,
                    enable_ssh=enable_ssh,
                    enable_battery=enable_battery
                )

                if enable_network == False:
                    self.devices_offline.append(device_)
                elif enable_ssh == False:
                    self.devices_local.append(device_)
                elif enable_ssh == True:
                    self.devices_remote.append(device_)

                index_row = content.grid.get_index_row()
                index_col = content.grid.get_index_col()
                content.layout.addWidget(device_.widget, index_row, index_col)
                
                # layout = eval(f"self.ui.grid_diagnostics2_{category}")
                # grid: Obj_gridDiagnosticsLayout = eval(f"self.grid_{category}")

                # index_row = grid.get_index_row()
                # index_col = grid.get_index_col()

                # layout.addWidget(device_.widget, index_row, index_col)



            # miscellaneous
            # if counter == 0:
            #     UIFunctions.diagnostics_submenu2_style(self, button.objectName())
            counter += 1
            if counter == 1:
                content.select()
        
        self.diagnostics_log(f"loaded experiment \"{self.experiment_name}\"")
        self.is_experiment_loaded = True


    def diagnostics_submenu2_click(self, button: QPushButton):
        """
        """
        button.clicked.disconnect()
        UIFunctions.diagnostics_submenu2_style(self, button.objectName())
        # button.clicked.connect(lambda self=self, button=button: UIFunctions.diagnostics_submenu2_click(self, button))


    


    # def diagnostics_submenu2_style_reset(self, name: str):
    #     """
    #     """
    #     for widget in widgets.diagnosticsSubmenu2ButtonsLeftLayout.findChildren(QPushButton):
    #         is_same: bool = (widget.objectName() == name)
    #         if is_same == False:
    #             style = widget.styleSheet()
    #             style = style.replace(Settings.DIAGNOSTICS_SUBMENU2_STYLE, "")
    #             widget.setStyleSheet(style)
    #         elif is_same == True:
    #             style = widget.styleSheet()
    #             style = style.replace("", Settings.DIAGNOSTICS_SUBMENU2_STYLE)
    #             widget.setStyleSheet(style)

    #             page = widgets.diagnosticsPages2.findChild(QWidget, f"{widget.objectName().replace('btn', 'page')}")
    #             widgets.diagnosticsPages2.setCurrentWidget(page)


            # experiment_name = self.experiment_file_content.get("experiment_name", "")

            # if self.experiment_name is None and experiment_name != "":
            #     self.experiment_name = experiment_name

            #     UIFunctions.diagnostics_add_submenu2_button(self, "test3")

            #     # self.mess2_load_sensors()
            #     # self.mess2_load_actors()
            #     self.is_experiment_loaded = True
            #     UIFunctions.diagnostics_log(self, f"loaded experiment {self.experiment_name}")
            #     widgets.experimentFileNameText.setText(self.experiment_file_path)

            # elif self.experiment_name is not None and experiment_name != "" and experiment_name != self.experiment_name:
            #     self.experiment_name = experiment_name
            #     # self.mess2_remove_sensors()
            #     # self.mess2_remove_actors()
            #     # self.mess2_load_sensors()
            #     # self.mess2_load_actors()
            #     self.is_experiment_loaded = True
            #     UIFunctions.diagnostics_log(self, f"loaded experiment {self.experiment_name}")
            #     widgets.experimentFileNameText.setText(self.experiment_file_path)


            # elif experiment_name == "":
            #     UIFunctions.diagnostics_log(self, f"experiment file {self.experiment_file_path} is invalid")

            # elif experiment_name == self.experiment_name:
            #     UIFunctions.diagnostics_log(self, f"experiment file {self.experiment_file_path} was already loaded")


    
    # BUTTON EVENTS
    # ///////////////////////////////////////////////////////////////
    # def logExperimentRunningEvent(self, btnName: str):
    #     """
    #     """
    #     if self.enable_click_logging_while_experiment_running:
    #                 UIFunctions.diagnostics_log(f"buttonClick : cannot press {btnName} while experiment is running")


    # def selectExperimentEvent(self):
    #     """
    #     """
        
    

    # def createSensorVICONEvent(self):
    #     """
    #     """
    #     if self.sensor_vicon:
    #         pass


    # def toggleSensorVICONEvent(self):
    #     """
    #     """
    #     if not self.sensor_vicon.is_connected:
    #         UIFunctions.toggleStyleConnected(self, self.sensor_vicon.frameNameConnected, True)
    #         UIFunctions.toggleStyleOnline(self, self.sensor_vicon.frameNameOnline, True)
    #         self.sensor_vicon.is_connected = True
    #     # if not self.sensor_vicon.is_running









    # CUSTOM CODE
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # def mess2_create_grid(self, n_cols: int = 2, n_rows: int = None):
    #     """
    #     This method initializes 
    #     """
    # def mess2_experiment_select(self):
    #     """
    #     This method creates a 
    #     """
    #     if not self.is_experiment_running:
    #         response = QFileDialog.getOpenFileName(
    #             parent=self,
    #             caption="Select a file",
    #             dir=os.getcwd(),
    #             filter=self.experiment_file_extensions
    #         )
    #         experiment_file_path, _ = response
    #         if experiment_file_path:
    #             self.experiment_file_path = experiment_file_path
    #             UIFunctions.diagnostics_log(self, f"selected experiment file {self.experiment_file_path}")


    # def mess2_experiment_load(self):
    #     """
    #     This method loads the gui elements of a preconfigured experiment .yaml file and creates backend object instances needed to run an experiment.
    #     """
    #     if self.is_experiment_running:
    #         UIFunctions.diagnostics_log(self, "unable to load experiment file while experiment is running")

    #     elif self.experiment_file_path is None:
    #         UIFunctions.diagnostics_log(self, "unable to load exeperiment file while no experiment is selected")

    #     else:
    #         with open(self.experiment_file_path, "r") as file:
    #             self.experiment_file_content = yaml.safe_load(file)
            
    #         experiment_name = self.experiment_file_content.get("experiment_name", "")

    #         if self.experiment_name is None and experiment_name != "":
    #             self.experiment_name = experiment_name
    #             self.mess2_load_sensors()
    #             self.mess2_load_actors()
    #             self.is_experiment_loaded = True
    #             UIFunctions.diagnostics_log(self, f"loaded experiment {self.experiment_name}")
    #             widgets.experimentFileNameText.setText(self.experiment_file_path)

    #         elif self.experiment_name is not None and experiment_name != "" and experiment_name != self.experiment_name:
    #             self.experiment_name = experiment_name
    #             self.mess2_remove_sensors()
    #             self.mess2_remove_actors()
    #             self.mess2_load_sensors()
    #             self.mess2_load_actors()
    #             self.is_experiment_loaded = True
    #             UIFunctions.diagnostics_log(self, f"loaded experiment {self.experiment_name}")
    #             widgets.experimentFileNameText.setText(self.experiment_file_path)


    #         elif experiment_name == "":
    #             UIFunctions.diagnostics_log(self, f"experiment file {self.experiment_file_path} is invalid")

    #         elif experiment_name == self.experiment_name:
    #             UIFunctions.diagnostics_log(self, f"experiment file {self.experiment_file_path} was already loaded")


    # def mess2_add_sensor(self, type: str = "sensor", name: str = "", ip: str = "", username: str = "ubuntu", password: str = "1234", port: int = -1):
    #     """
        
    #     """
    #     index_row = self.diagnostics_grid_sensors.get_index_row()
    #     index_col = self.diagnostics_grid_sensors.get_index_col()
    #     if name == "":
    #         name = f"blankSensor_{index_row}_{index_col}"
    #     sensor = Device(
    #         type=type, name=name, ip=ip, username=username, password=password, port=port, logger=widgets.diagnosticsTerminal, threadpool=self.threadpool
    #     )
    #     if type != "":
    #         self.diagnostics_sensors.append(sensor)
    #         widgets.diagnosticsSensorsLayout.addWidget(sensor.widget, index_row, index_col)
    

    # def mess2_remove_sensor(self, sensor: Device):
    #     """
        
    #     """
    #     widgets.diagnosticsSensorsLayout.removeWidget(sensor.widget)
    #     sensor.widget.deleteLater()


    # def mess2_remove_sensors(self):
    #     """
        
    #     """
    #     for sensor in self.diagnostics_sensors:
    #         self.mess2_remove_sensor(sensor)
    #     self.diagnostics_sensors.clear()
    #     self.diagnostics_grid_sensors.__reset__()
    

    # def mess2_load_sensors(self):
    #     """
    #     This method loads the sensor diagnostics gui elements from a preconfigured experiment .yaml file.
    #     """
    #     if "sensors" in self.experiment_file_content:
    #         for sensor in self.experiment_file_content["sensors"]:
    #             type = sensor.get("type", "")
    #             name = sensor.get("name", "")
    #             ip = sensor.get("ip", "")
    #             assert(type != "" and type != None)
    #             assert(name != "" and name != None)

    #             username = sensor.get("username", "ubuntu")
    #             password = sensor.get("password", "1234")
    #             port = sensor.get("port")
    #             assert(username != "")

    #             self.mess2_add_sensor(
    #                 type=type, name=name, ip=ip, username=username, password=password, port=port
    #             )
    #             if type == "vicon":
    #                 self.mess2_add_sensor(type="")  # add empty tile next to vicon ;) so it has its own row


    # def mess2_add_actor_ugv(self, type: str = "ugv", name: str = "", ip: str = "", username: str = "ubuntu", password: str = "1234", port: int = -1):
    #     """
        
    #     """
    #     index_row = self.diagnsotics_grid_ugvs.get_index_row()
    #     index_col = self.diagnsotics_grid_ugvs.get_index_col()
    #     actor = Device(
    #         type=type, name=name, ip=ip, username=username, password=password, port=port, logger=widgets.diagnosticsTerminal, threadpool=self.threadpool
    #     )
    #     self.diagnostics_actors_ugvs.append(actor)
    #     widgets.diagnosticsUGVsLayout.addWidget(actor.widget, index_row, index_col)
    

    # def mess2_remove_actor_ugv(self, actor: Device):
    #     """

    #     """
    #     widgets.diagnosticsUGVsLayout.removeWidget(actor.widget)
    #     actor.widget.deleteLater()


    # def mess2_add_actor_uav(self, type: str = "ugv", name: str = "", ip: str = "", username: str = "ubuntu", password: str = "1234", port: int = -1):
    #     """
        
    #     """
    #     index_row = self.diagnsotics_grid_uavs.get_index_row()
    #     index_col = self.diagnsotics_grid_uavs.get_index_col()
    #     actor = Device(
    #         type=type, name=name, ip=ip, username=username, password=password, port=port, logger=widgets.diagnosticsTerminal, threadpool=self.threadpool
    #     )
    #     self.diagnostics_actors_uavs.append(actor)
    #     widgets.diagnosticsUAVsLayout.addWidget(actor.widget, index_row, index_col)
    

    # def mess2_remove_actor_uav(self, actor: Device):
    #     """

    #     """
    #     widgets.diagnosticsUAVsLayout.removeWidget(actor.widget)
    #     actor.widget.deleteLater()

    
    # def mess2_remove_actors(self):
    #     """
        
    #     """
    #     for actor in self.diagnostics_actors_ugvs:
    #         self.mess2_remove_actor_ugv(actor)
    #     self.diagnostics_actors_ugvs.clear()
    #     self.diagnsotics_grid_ugvs.__reset__()
    #     for actor in self.diagnostics_actors_uavs:
    #         self.mess2_remove_actor_uav(actor)
    #     self.diagnostics_actors_uavs.clear()
    #     self.diagnsotics_grid_uavs.__reset__()


    # def mess2_load_actors(self):
    #     """
    #     Loads the ugv and uav actor diagnostics gui elements from a preconfigured experiment .yaml file.
    #     """
    #     if "actors" in self.experiment_file_content:
    #         for actor in self.experiment_file_content["actors"]:
    #             type = actor.get("type", "")
    #             name = actor.get("name", "")
    #             ip = actor.get("ip", "")
    #             assert(type != "" and type != None)
    #             assert(name != "" and name != None)

    #             username = actor.get("username", "ubuntu")
    #             password = actor.get("password", "1234")
    #             port = actor.get("port")
    #             assert(username != "")

    #             if type == "ugv":
    #                 self.mess2_add_actor_ugv(
    #                     type=type, name=name, ip=ip, username=username, password=password, port=port
    #                 )
    #             elif type == "uav":
    #                 self.mess2_add_actor_uav(
    #                     type=type, name=name, ip=ip, username=username, password=password, port=port
    #                 )


    # def mess2_check_network_and_ssh_connections(self):
    #     """
    #     Checks network connections for sensors, ugvs, and uavs.
    #     """
    #     worker = WorkerDeviceUI(
    #         self.diagnostics_sensors,
    #         self.diagnostics_actors_ugvs + self.diagnostics_actors_uavs
    #     )
    #     self.threadpool.start(worker)


    # def mess2_establish_or_close_ssh_connections(self):
    #     """
    #     """
    #     if self.are_actors_ssh_connected == False:
    #         widgets.btn_ssh_connect.setText("Disconnect from all Actors")
    #         self.are_actors_ssh_connected = True
    #     elif self.are_actors_ssh_connected == True:
    #         widgets.btn_ssh_connect.setText("Connect to all Actors")
    #         self.are_actors_ssh_connected = False


    # def mess2_start_or_stop_sensor_nodes(self):
    #     """
    #     """
    #     if self.are_sensor_nodes_running == False:
    #         widgets.btn_ros2_sensor_drivers.setText("Shutdown ROS2 Sensor Drivers")
    #         self.are_sensor_nodes_running = True
    #     elif self.are_sensor_nodes_running == True:
    #         widgets.btn_ros2_sensor_drivers.setText("Launch ROS2 Sensor Drivers")
    #         self.are_sensor_nodes_running = False


    # def mess2_start_or_stop_actor_nodes(self):
    #     """
    #     """
    #     if self.are_actor_nodes_running == False:
    #         widgets.btn_ros2_actor_nodes.setText("Shutdown ROS2 Actor Nodes")
    #         self.are_actor_nodes_running = True
    #     elif self.are_actor_nodes_running == True:
    #         widgets.btn_ros2_actor_nodes.setText("Launch ROS2 Actor Nodes")
    #         self.are_actor_nodes_running = False


    # def mess2_experiment_abort(self):
    #     """
    #     """
    #     if self.is_experiment_running == True:
    #         UIFunctions.diagnostics_log(self, f"aborting experiment {self.experiment_name}")
    #         UIFunctions.diagnostics_log(self, f"aborted experiment {self.experiment_name}")


    # def mess2_logs_path_select(self):
    #     """
    #     """
    #     if not self.is_experiment_running:
    #         response = QFileDialog.getExistingDirectory(
    #             parent=self,
    #             caption="Select a directory",
    #             dir=os.getcwd(),
    #         )
    #         self.experiment_dir_logs = response
    #         widgets.logSavePathText.setText(self.experiment_dir_logs)




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
