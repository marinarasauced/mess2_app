
from PySide6.QtCore import Qt, QRunnable, QThreadPool
from PySide6.QtWidgets import QWidget, QPlainTextEdit

from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, Future
from modules.custom.diagnostics.logger import LoggerUI
from modules.custom.diagnostics.network import NetworkFunctions
from modules.custom.ui.ui_tileDiagnosticsSensor import Ui_tileDiagnosticsSensor
from modules.custom.ui.ui_tileDiagnosticsUGV import Ui_tileDiagnosticsUGV
from modules.custom.ui.ui_tileDiagnosticsUAV import Ui_tileDiagnosticsUAV
from typing import List, Union


class DeviceUI():
    """
    Manages the ui attributes and methods for a mess2 app diagnostics instance.
    """
    def __init__(self):
        """
        Initializes ui attributes.
        """
        # battery icons
        self.style_battery_percentage_0 = "background-image: url(:/icons/images/icons2/battery_0.png);"
        self.style_battery_percentage_25 = "background-image: url(:/icons/images/icons2/battery_25.png);"
        self.style_battery_percentage_50 = "background-image: url(:/icons/images/icons2/battery_50.png);"
        self.style_battery_percentage_75 = "background-image: url(:/icons/images/icons2/battery_75.png);"
        self.style_battery_percentage_100 = "background-image: url(:/icons/images/icons2/battery_100.png);"
        self.style_battery_percentage_na = "background-image: url(:/icons/images/icons2/battery_na.png);"

        # network connection icons
        self.style_network_connected = "background-image: url(:/icons/images/icons2/network_connected.png);"
        self.style_network_disconnected = "background-image: url(:/icons/images/icons2/network_disconnected.png);"
        self.style_network_na = "background-image: url(:/icons/images/icons2/network_na.png);"

        # mess2 app connection icons
        self.style_ssh_connected = "background-image: url(:/icons/images/icons2/ssh_connected.png);"
        self.style_ssh_disconnected = "background-image: url(:/icons/images/icons2/ssh_disconnected.png);"
        self.style_ssh_na = "background-image: url(:/icons/images/icons2/ssh_na.png);"

        # mess2 device types
        self.types_sensor = [
            "sensor",
            "vicon",
            "flir"
        ]
        self.types_ugvs = [
            "ugv",
            "burger",
            "waffle",
            "waffle_pi",
            "wafflepi"
        ]
        self.types_uavs = [
            "uav",
            "hawk"
        ]

        # mess2 widget options
        self.types_ui = {
            "sensor": "Ui_tileDiagnosticsSensor",
            "ugv": "Ui_tileDiagnosticsUGV",
            "uav": "Ui_tileDiagnosticsUAV"
        }

        self.widget = QWidget()
        self.ui: Union[Ui_tileDiagnosticsSensor, Ui_tileDiagnosticsUGV, Ui_tileDiagnosticsUAV] = None

        self.battery_percentage_text = None
        self.battery_percentage_style = None


    def ui_lookup(self, type: str):
        """
        """
        if type in self.types_sensor:
            result = self.types_ui.get("sensor", None)
        elif type in self.types_ugvs:
            result = self.types_ui.get("ugv", None)
        elif type in self.types_uavs:
            result = self.types_ui.get("uav", None)
        else:
            result = None
        return result


    def set_name_text(self, value: str):
        """
        Updates the device's name text in the app gui.
        """
        self.ui.name_text.setText(value)


    def set_battery_percentage_text(self, value: str):
        """
        Updates the device's battery percentage text in the app gui.
        """
        if value != self.battery_percentage_text:
            self.ui.battery_text.setText(value)
            self.battery_percentage_text = value


    def set_battery_percentage_icon(self, value: float):
        """
        Updates the device's battery percentage icon in the app gui.
        """
        if value < -1.0:
            replacement = self.style_battery_percentage_na
        elif value < 0.20:
            replacement = self.style_battery_percentage_0     # should be 0
        elif value < 0.30:
            replacement = self.style_battery_percentage_25     # should be 1
        elif value < 0.55:
            replacement = self.style_battery_percentage_50     # should be 2
        elif value < 0.80:
            replacement = self.style_battery_percentage_75     # should be 3
        else:
            replacement = self.style_battery_percentage_100     # should be 5

        if replacement != self.battery_percentage_style:
            style_old = self.widget.styleSheet()
            style_new = style_old.replace(self.style_battery_percentage_0, replacement)
            style_new = style_new.replace(self.style_battery_percentage_25, replacement)
            style_new = style_new.replace(self.style_battery_percentage_50, replacement)
            style_new = style_new.replace(self.style_battery_percentage_75, replacement)
            style_new = style_new.replace(self.style_battery_percentage_100, replacement)
            style_new = style_new.replace(self.style_battery_percentage_na, replacement)
            self.widget.setStyleSheet(style_new)
            self.battery_percentage_style = replacement


    def set_ssh_icon(self, value: bool):
        """
        Updates the device's SSH icon in the app gui. If the value is None, the SSH icon in the app gui will be disabled.
        """
        style = self.widget.styleSheet()
        if value == None:
            style = style.replace(self.style_ssh_connected, self.style_ssh_na)
            style = style.replace(self.style_ssh_disconnected, self.style_ssh_na)
        elif value == True:
            style = style.replace(self.style_ssh_na, self.style_ssh_connected)
            style = style.replace(self.style_ssh_disconnected, self.style_ssh_connected)
        elif value == False:
            style = style.replace(self.style_ssh_na, self.style_ssh_disconnected)
            style = style.replace(self.style_ssh_connected, self.style_ssh_disconnected)
        self.widget.setStyleSheet(style)


    def set_network_icon(self, value: bool):
        """
        Updates the device's network icon in the app gui. If the value is None, the network icon in the app gui will be disabled.
        """
        style = self.widget.styleSheet()
        if value == None:
            style = style.replace(self.style_network_connected, self.style_network_na)
            style = style.replace(self.style_network_disconnected, self.style_network_disconnected)
        elif value == True:
            style = style.replace(self.style_network_na, self.style_network_connected)
            style = style.replace(self.style_network_disconnected, self.style_network_connected)
        elif value == False:
            style = style.replace(self.style_network_na, self.style_network_disconnected)
            style = style.replace(self.style_network_connected, self.style_network_disconnected)
        self.widget.setStyleSheet(style)


    def set_ip_text(self, value: str):
        """
        Updates the device's ip text in the app gui.
        """
        self.ui.ip_text.setText(value)


class DeviceFunctions():
    """
    Manages the non-ui attributes and methods for a mess2 app diagnostics instance.
    """
    def __init__(self):
        """
        Initializes non-ui attributes.
        """
        self.network = NetworkFunctions()


class Device(DeviceFunctions, DeviceUI):
    """
    Manages a mess2 app diagnostics device. 
    """
    def __init__(self, type: str, name: str, ip: str, username: str = "ubuntu", password="1234", port: int = -1, logger: QPlainTextEdit = None, threadpool: QThreadPool = None, enable_network: bool = True, enable_ssh: bool = False, enable_battery: bool = False):
        """
        Initializes device attributes and shows the device in the mess2 app.
        """
        DeviceFunctions.__init__(self)
        DeviceUI.__init__(self)

        # device discriminators
        self.type = type
        self.name = name

        # device network information
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port

        #
        self.enable_network = enable_network
        self.enable_ssh = enable_ssh
        self.enable_battery = enable_battery

        # device visual information
        self.ui_draw()

        #
        self.logger = LoggerUI(logger)
        self.threadpool = threadpool


    def __del__(self):
        """
        Safely destroys the device by closing any active SSH connections.
        """
        self.network.disconnect()
        

    def ui_draw(self):
        """
        """
        self.widget.setObjectName(f"{self.type}_{self.name.replace(" ", "_").replace(".", "_")}")
        if self.type == None:
            pass
        else:
            self.ui = Ui_tileDiagnosticsUGV()
            self.ui.setupUi(self.widget, self.enable_network, self.enable_ssh, self.enable_battery)
            self.set_name_text(self.name)

            # print(vars(self.widget))

            # if self.enable_network == False:
            #     self.ui.__delattr__("network_icon")

            # if self.enable_ssh == False:
            #     self.ui.__delattr__("ssh_icon")
            
            # if self.enable_battery == False:
            #     self.ui.__delattr__("battery_icon")
            #     self.ui.__delattr__("battery_text")
            
            if hasattr(self.ui, "battery_text"):
                self.set_battery_percentage_text("n/a")
                self.ui.battery_text.setAlignment(Qt.AlignRight)

            if hasattr(self.ui, "battery_icon"):
                self.set_battery_percentage_icon(-2.0)

            if hasattr(self.ui, "ssh_icon"):
                self.set_ssh_icon(False)
                self.ui.ssh_icon.clicked.connect(self.click_ssh)

            if hasattr(self.ui, "network_icon"):
                self.set_network_icon(False)
            
            self.set_ip_text(self.ip)
            self.ui.nodesLayout.setAlignment(Qt.AlignTop)


    def ui_redraw(self, battery_percentage_text: str = None, battery_percentage_value: float = None, status_ssh: bool = None, status_network: bool = None):
        """
        Updates the device's dynamic app gui elements with new values if updates are necessary. Any parameters that are no
        """
        # only update battery percentage text if value has changed (check performed in method). 
        if hasattr(self.ui, "battery_text") and battery_percentage_text != None:
            self.set_battery_percentage_text(battery_percentage_text)

        # only update battery percentage icon if value causes style change (check performed in method).
        if hasattr(self.ui, "battery_icon") and battery_percentage_value != None:
            self.set_battery_percentage_icon(battery_percentage_value)

        # only update ssh icon if ssh status changed
        if hasattr(self.ui, "ssh_icon") and status_ssh != None:
            if self.network.status_ssh != status_ssh:
                self.set_ssh_icon(status_ssh)
                self.network.status_ssh = status_ssh

        # only update network icon if network status changed
        if hasattr(self.ui, "network_icon") and status_network != None:
            if self.network.status_network != status_network:
                self.set_network_icon(status_network)
                self.network.status_network = status_network


    def click_ssh(self):
        """
        """
        if self.network.status_ssh == True:
            worker = WorkerDeviceSSHDisconnect(self)
        else:
            worker = WorkerDeviceSSHConnect(self)
        self.threadpool.start(worker)


class WorkerDeviceUI(QRunnable):
    """
    Manages threaded worker to check and update network connection icons.
    """
    def __init__(self, sensors: List[Device], actors: list[Device]):
        """
        """
        super().__init__()
        self.sensors = sensors
        self.actors = actors


    def run(self):
        """
        Executes the network and/or SSH checks for the given devices and calls redraw_ui with both results.
        """
        results_network = defaultdict(lambda: None)
        results_ssh = defaultdict(lambda: None)

        with ThreadPoolExecutor() as executor:
            futures_network = {executor.submit(device.network.ping, device.ip): device for device in self.sensors + self.actors if device.name != "" and device.name != None}
            futures_ssh = {executor.submit(device.network.status): device for device in self.actors if device.name != "" and device.name != None}
            
            for future in futures_network:
                try:
                    device = futures_network[future]
                    result = future.result()
                    results_network[device.name] = result
                except Exception as e:
                    pass
            
            for future in futures_ssh:
                try:
                    device = futures_ssh[future]
                    result = future.result()
                    results_ssh[device.name] = result
                except Exception as e:
                    pass

            for device in self.sensors + self.actors:
                try:
                    if device.name != "" and device.name != None:
                        status_network = results_network[device.name]
                        # status_ssh = results_ssh[device.name]
                        status_ssh = None
                        device.ui_redraw(
                            battery_percentage_text=None,
                            battery_percentage_value=None,
                            status_network=status_network,
                            status_ssh=status_ssh
                        )
                except Exception as e:
                    pass


def ssh_connect(device: Device):
    """
    Establishes an SSH connection with a remote device with more-involved networking logic and diagnostics logging.
    """
    if device.network.status_network != True:
        result_ping = device.network.ping(device.ip)
        device.network.status_network = result_ping

    if device.network.status_network == False:
        device.logger.log(f"unable to establish network connection {device.name}")

    elif device.network.status_network == True:

        if device.network.connect(hostname=device.ip, username=device.username, password=device.password, port=device.port):
            device.network.status_ssh = True
            device.logger.log(f"established SSH connection with {device.name}")

        else:
            device.network.status_ssh = False
            device.logger.log(f"unable to establish SSH connection with {device.name}")


class WorkerDeviceSSHConnect(QRunnable):
    """
    Manages threaded worker to establish an SSH connection with a single device.
    """
    def __init__(self, device: Device):
        """
        """
        super().__init__()
        self.device = device


    def run(self):
        """
        """
        ssh_connect(self.device)
        

class WorkerDevicesSSHConnect(QRunnable):
    """
    Manages threaded worker to establish SSH connections with multiple devices.
    """
    def __init__(self, devices: List[Device]):
        """
        """
        super().__init__()
        self.devices = devices


    def run(self):
        """
        """
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(ssh_connect, device): device for device in self.devices if device.name != "" and device.name != None}


def ssh_disconnect(device: Device):
    """
    Closes an SSH connection with a remote device using more-involved networking logic and diagnostics logging.
    """
    if device.network.status_network != True:
        result_ping = device.network.ping(device.ip)
        device.network.status_network = result_ping

    if device.network.status_ssh == True:

        if device.network.disconnect():
            device.network.status_ssh = False
            device.logger.log(f"closed SSH connection with {device.name}")

        else:
            device.network.status_ssh = True
            device.logger.log(f"unable to close SSH connection with {device.name}")


class WorkerDeviceSSHDisconnect(QRunnable):
    """
    Manages threaded worker to close an SSH connection with a single device.
    """
    def __init__(self, device: Device):
        """
        """
        super().__init__()
        self.device = device


    def run(self):
        """
        """
        ssh_disconnect(self.device)
        

class WorkerDevicesSSHDisconnect(QRunnable):
    """
    Manages threaded worker to close SSH connections with multiple devices.
    """
    def __init__(self, devices: List[Device]):
        """
        """
        super().__init__()
        self.devices = devices


    def run(self):
        """
        """
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(ssh_disconnect, device): device for device in self.devices if device.name != "" and device.name != None}
