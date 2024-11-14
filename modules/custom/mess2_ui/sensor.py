
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget

from modules.custom.mess2_ui.common import *
from modules.custom.mess2_ui.ui_tileDiagnosticsSensor import *


class Sensor(UIFunctionsDiagnostics, Ping):
    """
    """
    def __init__(self, sensor_type: str, sensor_name: str, sensor_ip: str = "", show_connected: bool = False, show_online: bool = True, is_empty: bool = False):
        """
        """
        super().__init__()
        assert(sensor_type is not None and sensor_type != "")
        assert(sensor_name is not None and sensor_name != "")

        self.type = sensor_type
        self.name = sensor_name
        self.ip = sensor_ip
        self.show_connected = show_connected
        self.show_online = show_online
        self.widget = QWidget()
        self.ui = Ui_tileDiagnosticsSensor()

        self.ui_layout = "diagnosticsSensorsLayout"

        self.counter_displayed_nodes = 0
        self.show(is_empty)


    def show(self, is_empty: bool = False):
        """
        
        """
        if is_empty:
            self.widget.setObjectName(f"{self.name}")
            self.type = None
            self.name = None
            self.ip = None
            self.show_connected = None
            self.show_online = None
        else:
            self.widget.setObjectName(f"{self.type}Sensor{self.name}")
            self.ui.setupUi(self.widget)
            self.ui_update_name_text(self.name)
   
            self.ui_update_ip_text(self.ip)
            self.ui.nodesLayout.setAlignment(Qt.AlignTop)

            print(self.widget.styleSheet().find(self.style_disconnected_from_network))

            if self.show_connected is False:
                self.ui_disable_connected_to_mess2_icon()
            if self.show_online is False:
                self.ui_disable_connected_to_network_icon()
