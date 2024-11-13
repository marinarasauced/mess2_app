
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget

from modules.custom.mess2_ui.ui_tileDiagnosticsSensor import *


class Obj_mess2SensorSettings():
    """
    """
    def __init__(self):
        """
        """
        # network connection icons
        self.style_disconnected_from_network = "background-image: url(:/icons/images/icons2/status_offline.png);"
        self.style_connected_to_network = "background-image: url(:/icons/images/icons2/status_online.png);"

        # mess2 app connection icons
        self.style_disconnected_from_mess2 = "background-image: url(:/icons/images/icons2/status_disconnected.png);"
        self.style_connected_to_mess2 = "background-image: url(:/icons/images/icons2/status_connected.png);"


class Obj_mess2Sensor(Obj_mess2SensorSettings):
    """
    """
    def __init__(self, sensor_type: str, sensor_name: str, sensor_ip: str = "", show_connected: bool = False, show_online: bool = True, is_empty: bool = False):
        """
        """
        super().__init__()
        assert(sensor_type is not None and sensor_type != "")
        assert(sensor_name is not None and sensor_name != "")

        self.sensor_type = sensor_type
        self.sensor_name = sensor_name
        self.sensor_ip = sensor_ip
        self.show_connected = show_connected
        self.show_online = show_online
        self.widget = QWidget()
        self.ui = Ui_tileDiagnosticsSensor()

        self.ui_layout = "diagnosticsSensorsLayout"

        self.counter_displayed_nodes = 0
        self.show(is_empty)


    def ui_update_sensor_name_text(self, value: str):
        """
        This method updates the sensor's name text.
        """
        self.ui.name_text.setText(value)
    

    def ui_disable_connected_to_mess2_icon(self):
        """
        
        """
        style_old = self.widget.styleSheet()
        style_new = style_old.replace(self.style_connected_to_mess2, "")
        style_new = style_new.replace(self.style_disconnected_from_mess2, "")
        self.widget.setStyleSheet(style_new)


    def ui_update_connected_to_mess2_icon(self, value: bool):
        """
        This method updates the connected to mess2 (ssh) icon.
        """
        style_old = self.widget.styleSheet()
        if value:
            style_new = style_old.replace(self.style_disconnected_from_mess2, self.style_connected_to_mess2)
        elif not value:
            style_new = style_old.replace(self.style_connected_to_mess2, self.style_disconnected_from_mess2)
        self.widget.setStyleSheet(style_new)

    
    def ui_disable_connected_to_network_icon(self):
        """
        
        """
        style_old = self.widget.styleSheet()
        style_new = style_old.replace(self.style_connected_to_network, "")
        style_new = style_new.replace(self.style_disconnected_from_network, "")
        self.widget.setStyleSheet(style_new)

    
    def ui_update_connected_to_network_icon(self, value: bool):
        """
        This method updates the connected to network icon.
        """
        style_old = self.widget.styleSheet()
        if value:
            style_new = style_old.replace(self.style_disconnected_from_network, self.style_connected_to_network)
        elif not value:
            style_new = style_old.replace(self.style_connected_to_network, self.style_disconnected_from_network)
        self.widget.setStyleSheet(style_new)


    def ui_update_sensor_ip_text(self, value: str):
        """
        This method updates the sensor's name text.
        """
        self.ui.ip_text.setText(value)


    def show(self, is_empty: bool = False):
        """
        
        """
        if is_empty:
            self.widget.setObjectName(f"{self.sensor_name}")
        else:
            self.widget.setObjectName(f"{self.sensor_type}Sensor{self.sensor_name}")
            self.ui.setupUi(self.widget)
            self.ui_update_sensor_name_text(self.sensor_name)
   
            self.ui_update_sensor_ip_text(self.sensor_ip)
            self.ui.nodesLayout.setAlignment(Qt.AlignTop)

            print(self.widget.styleSheet().find(self.style_disconnected_from_network))

            if self.show_connected is False:
                self.ui_disable_connected_to_mess2_icon()
            if self.show_online is False:
                self.ui_disable_connected_to_network_icon()
