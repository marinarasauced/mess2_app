
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

        # GENERAL SETTINGS
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


        # THREADPOOL
        self.threadpool = QThreadPool.globalInstance()
        self.threadpool.maxThreadCount = 8


        # EXPERIMENT CHECKS
        self.are_all_devices_connected_to_network: bool = False
        self.are_all_remote_devices_connected_to_network: bool = False
        self.are_all_remote_devices_connected_via_ssh: bool = False
        self.are_all_local_nodes_running: bool = False
        self.are_all_remote_nodes_running: bool = False


        #
        self.experiment_name = None
        self.experiment_file_extensions: str = ".yaml (*.yaml)"
        self.experiment_file_path: str = None
        self.experiment_file_content = None
        self.is_experiment_loaded = False
        self.is_experiment_running: bool = False

        self.experiment_log_path: str = os.path.abspath(os.path.join(os.getcwd(), "../logs"))
        widgets.logSavePathText.setText(self.experiment_log_path)


        # PRIMARY MENU
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_diagnostics.clicked.connect(self.buttonClick)
        widgets.btn_planner.clicked.connect(self.buttonClick)
        widgets.btn_settings.clicked.connect(self.buttonClick)

        # DIAGNOSTICS
        # ///////////////////////////////////////////////////////////////

        # DIAGNOSTICS SUBMENU1
        widgets.btn_experiment_select.clicked.connect(self.experiment_select)
        widgets.btn_experiment_load.clicked.connect(self.experiment_load)
        widgets.btn_log_save_path_select.clicked.connect(self.save_path_select)
        widgets.btn_experiment_abort.clicked.connect(self.experiment_abort)
        widgets.btn_experiment_run.clicked.connect(self.experiment_run)

        widgets.diagnosticsSubmenu1.setAlignment(Qt.AlignTop)

        self.toggle_connect_to_remote_devices = 0
        widgets.btn_connect_to_remote_devices.clicked.connect(self.experiment_toggle_click_connect_to_remote_devices)
    
        self.toggle_start_local_ros2_nodes = 0
        widgets.btn_start_local_ros2_nodes.clicked.connect(self.experiment_toggle_click_start_local_ros2_nodes)

        self.toggle_start_remote_ros2_nodes = 0
        widgets.btn_start_remote_ros2_nodes.clicked.connect(self.experiment_toggle_click_start_remote_ros2_nodes)

        # DIAGNOSTICS SUBMENU2
        self.diagnostics_content = []
        self.devices_offline = []   # devices off the network (most likely the host machine) that must run ros2 software
        self.devices_remote = []    # devices with ros2 software that must be run on the remote device
        self.devices_local = []     # devices with ros2 software that must be run locally

        # DIAGNOSTICS ICONS WORKER
        self.diagnostics_timer_update_device_icons = QTimer()
        self.diagnostics_timer_update_device_icons.timeout.connect(self.diagnostics_update_icons)
        self.diagnostics_timer_update_device_icons.start(7000)









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
        if self.is_experiment_running == True:
            self.diagnostics_log("unable to select experiment file while experiment is running")
        elif self.is_experiment_running == False:
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
        if self.is_experiment_running == True:
            self.diagnostics_log("unable to load experiment file while experiment is running")

        elif self.experiment_file_path == None:
            self.diagnostics_log("unable to load exeperiment file while no experiment is selected")

        else:
            with open(self.experiment_file_path, "r") as file:
                self.experiment_file_content = yaml.safe_load(file)
            
            self.diagnostics_experiment_load(self.experiment_file_content)
        
        if self.devices_remote == None or self.devices_remote == []:
            self.toggle_connect_to_remote_devices = 2
            self.toggle_start_remote_ros2_nodes = 2
        else:
            self.toggle_connect_to_remote_devices = 0
            self.toggle_start_remote_ros2_nodes = 0


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
                commands1 = device.get("commands1", [])
                print(commands1)

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
                    enable_battery=enable_battery,
                    commands1=commands1
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

            counter += 1
            if counter == 1:
                content.select()
        
        self.diagnostics_log(f"loaded experiment \"{self.experiment_name}\"")
        self.is_experiment_loaded = True


    def diagnostics_update_icons(self):
        """
        """
        worker = WorkerDeviceUI(self.devices_local, self.devices_remote)
        self.threadpool.start(worker)


    def save_path_select(self):
        """
        """
        if self.is_experiment_running:
            self.diagnostics_log("unable to change log save path while experiment is running")
        else:
            response = QFileDialog.getExistingDirectory(
                parent=self,
                caption="Select a directory",
                dir=os.getcwd()
            )
            save_path_dir = response
            if save_path_dir:
                self.experiment_log_path = save_path_dir
                self.diagnostics_log(f"selected experiment log directory {self.experiment_log_path}")
                widgets.logSavePathText.setText(self.experiment_log_path)


    def experiment_run(self):
        """
        """
        self.diagnostics_log("experiment run not yet implemented")


    def experiment_abort(self):
        """
        """
        self.diagnostics_log("experiment abort not yet implemented")


    def experiment_check_remote_devices_connected_to_network(self):
        """
        """
        self.are_all_remote_devices_connected_to_network = True
        for device in self.devices_remote:
            if device.network.status_network == False or device.network.status_network == None:
                self.diagnostics_log(f"{device.name} is disconnected from the network")
                self.are_all_remote_devices_connected_to_network = False
        return self.are_all_remote_devices_connected_to_network


    def experiment_toggle_click_connect_to_remote_devices(self):
        """
        """
        if self.toggle_connect_to_remote_devices == 0:
            self.experiment_connect_to_remote_devices()
        elif self.toggle_connect_to_remote_devices == 1:
            self.experiment_disconnect_from_remote_devices()
        elif self.toggle_connect_to_remote_devices == 2:
            self.diagnostics_log("cannot connect to remote devices as no remote device are in the loaded experiment")


    def experiment_connect_to_remote_devices(self):
        """
        """
        if self.is_experiment_loaded == False:
            self.diagnostics_log(f"cannot connect to remote devices before experiment is selected")
            return

        if self.experiment_check_remote_devices_connected_to_network() == False:
            self.diagnostics_log(f"cannot connect to remote devices before all are connected to network")
            return
        
        worker = WorkerDevicesSSHConnect(self.devices_remote)
        self.threadpool.start(worker)

        widgets.btn_connect_to_remote_devices.setText("Disconnect from Remote Devices")
        self.toggle_connect_to_remote_devices = 1


    def experiment_disconnect_from_remote_devices(self):
        """
        """
        if self.is_experiment_loaded == False:
            self.diagnostics_log(f"cannot disconnect to remote devices before experiment is selected")
            return
        
        worker = WorkerDevicesSSHDisconnect(self.devices_remote)
        self.threadpool.start(worker)

        widgets.btn_connect_to_remote_devices.setText("Connect to Remote Devices")
        self.toggle_connect_to_remote_devices = 0


    def experiment_check_remote_devices_connected_via_ssh(self):
        """
        """
        self.are_all_remote_devices_connected_via_ssh = True
        for device in self.devices_remote:
            if device.network.status() == False:
                self.diagnostics_log(f"{device.name} is not connected via SSH")
                self.are_all_remote_devices_connected_via_ssh = False
        return self.are_all_remote_devices_connected_via_ssh


    def experiment_toggle_click_start_remote_ros2_nodes(self):
        """
        """
        if self.toggle_start_remote_ros2_nodes == 0:
            self.experiment_start_remote_ros2_nodes()
        elif self.toggle_start_remote_ros2_nodes == 1:
            self.experiment_stop_remote_ros2_nodes()
        elif self.toggle_start_remote_ros2_nodes == 2:
            self.diagnostics_log("cannot start remote ros2 nodes as there are no remote device in the loaded experiment")


    def experiment_start_remote_ros2_nodes(self):
        """
        """
        if self.is_experiment_loaded == False:
            self.diagnostics_log(f"cannot start remote ros2 nodes before experiment is selected")
            return
    
        if self.experiment_check_remote_devices_connected_to_network() == False:
            self.diagnostics_log(f"cannot start remote ros2 nodes unless all remote devices are connected to the network")
            return
        
        if self.experiment_check_remote_devices_connected_via_ssh() == False:
            self.diagnostics_log(f"cannot start remote ros2 nodes unless all remote devices are connected via ssh")
            return
        
        worker = WorkerDevicesROS2RemoteStart(self.devices_remote, 1)
        self.threadpool.start(worker)

        widgets.btn_start_remote_ros2_nodes.setText("Shutdown Remote ROS2 Nodes")
        self.toggle_start_remote_ros2_nodes = 1


    def experiment_stop_remote_ros2_nodes(self):
        """
        """
        if self.is_experiment_loaded == False:
            self.diagnostics_log(f"cannot stop remote ros2 nodes before experiment is selected")
            return

        devices_ = []
        for device in self.devices_remote:
            if device.network.status() == True:
                devices_.append(device)
        
        worker = WorkerDevicesROS2RemoteStop(devices_, 1)
        self.threadpool.start(worker)

        widgets.btn_start_remote_ros2_nodes.setText("Launch Remote ROS2 Nodes")
        self.toggle_start_remote_ros2_nodes = 0


    def experiment_toggle_click_start_local_ros2_nodes(self):
        """
        """
        if self.toggle_start_local_ros2_nodes == 0:
            self.experiment_start_local_ros2_nodes()
        elif self.toggle_start_local_ros2_nodes == 1:
            self.experiment_stop_local_ros2_nodes()


    def experiment_start_local_ros2_nodes(self):
        """
        """
        if self.is_experiment_loaded == False:
            self.diagnostics_log(f"cannot start local ros2 nodes before experiment is selected")
            return

        worker = WorkerDevicesROS2LocalStart(self.devices_local, 1)
        self.threadpool.start(worker)

        widgets.btn_start_local_ros2_nodes.setText("Shutdown Local ROS2 Nodes")
        self.toggle_start_local_ros2_nodes = 1


    def experiment_stop_local_ros2_nodes(self):
        """
        """
        if self.is_experiment_loaded == False:
            self.diagnostics_log(f"cannot stop local ros2 nodes before experiment is selected")
            return

        worker = WorkerDevicesROS2LocalStop(self.devices_local, 1)
        self.threadpool.start(worker)

        widgets.btn_start_local_ros2_nodes.setText("Launch Local ROS2 Nodes")
        self.toggle_start_local_ros2_nodes = 0



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
