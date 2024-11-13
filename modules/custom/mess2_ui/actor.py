
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget

from modules.custom.mess2_ui.ui_tileDiagnosticsUGV import *


class Obj_mess2ActorSettings():
    """
    """
    def __init__(self):
        """
        """
        # battery icons
        self.style_battery_percentage_0 = "background-image: url(:/icons/images/icons2/battery_0.png);"
        self.style_battery_percentage_25 = "background-image: url(:/icons/images/icons2/battery_25.png);"
        self.style_battery_percentage_50 = "background-image: url(:/icons/images/icons2/battery_50.png);"
        self.style_battery_percentage_75 = "background-image: url(:/icons/images/icons2/battery_75.png);"
        self.style_battery_percentage_100 = "background-image: url(:/icons/images/icons2/battery_100.png);"
        self.style_battery_percentage_na = "background-image: url(:/icons/images/icons2/battery_na.png);"

        # network connection icons
        self.style_disconnected_from_network = "background-image: url(:/icons/images/icons2/status_offline.png);"
        self.style_connected_to_network = "background-image: url(:/icons/images/icons2/status_online.png);"

        # mess2 app connection icons
        self.style_disconnected_from_mess2 = "background-image: url(:/icons/images/icons2/status_disconnected.png);"
        self.style_connected_to_mess2 = "background-image: url(:/icons/images/icons2/status_connected.png);"
        
        # mess2 widget options
        self.widget_categories = {
            "ugv": "Ui_tileDiagnosticsUGV",
            "uav": "Ui_tileDiagnosticsUAV"
        }
        self.diagnostics_layouts = {
            "ugv": "diagnosticsUGVsLayout",
            "uav": "diagnosticsUAVsLayout"
        }


class Obj_mess2Actor(Obj_mess2ActorSettings):
    """
    """
    def __init__(self, actor_type: str, actor_name: str, actor_ip: str = ""):
        """
        """
        super().__init__()
        assert(actor_type is not None and actor_type != "")
        assert(actor_name is not None and actor_name != "")

        self.actor_type = actor_type
        self.actor_name = actor_name
        self.actor_ip = actor_ip
        self.widget = QWidget()
        self.ui = None

        self.ui_category = self.ui_lookup_widget_category(self.actor_type)
        self.ui_layout = self.ui_lookup_diagnostics_layout(self.actor_type)

        self.counter_displayed_nodes = 0
        self.show()


    def ui_update_actor_name_text(self, value: str):
        """
        This method updates the actor's name text.
        """
        self.ui.name_text.setText(value)


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


    def ui_update_actor_ip_text(self, value: str):
        """
        This method updates the actor's name text.
        """
        self.ui.ip_text.setText(value)


    def ui_update_battery_percentage_text(self, value: str):
        """
        This method updates the actor's battery percentage text.
        """
        self.ui.battery_text.setText(value)


    def ui_update_battery_percentage_icon(self, value: float):
        """
        This method updates the battery percentage icon using the battery percentage.
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

        style_old = self.widget.styleSheet()
        style_new = style_old.replace(self.style_battery_percentage_0, replacement)
        style_new = style_new.replace(self.style_battery_percentage_25, replacement)
        style_new = style_new.replace(self.style_battery_percentage_50, replacement)
        style_new = style_new.replace(self.style_battery_percentage_75, replacement)
        style_new = style_new.replace(self.style_battery_percentage_100, replacement)
        style_new = style_new.replace(self.style_battery_percentage_na, replacement)
        self.widget.setStyleSheet(style_new)
    

    def ui_lookup_widget_category(self, key: str):
        """
        """
        result = self.widget_categories.get(key, "null")
        return result
    

    def ui_lookup_diagnostics_layout(self, key: str):
        result = self.diagnostics_layouts.get(key, "null")
        return result


    def show(self):
        """
        
        """
        self.widget.setObjectName(f"{self.actor_type}Actor{self.actor_name}")
        if self.ui_category == "null":
            pass
        else:
            self.ui = eval(f"{self.ui_category}()")
            self.ui.setupUi(self.widget)
            self.ui_update_actor_name_text(self.actor_name)
            self.ui_update_actor_ip_text(self.actor_ip)
            self.ui_update_battery_percentage_icon(-2.0)
            self.ui_update_battery_percentage_text("n/a")
            self.ui.battery_text.setAlignment(Qt.AlignRight)
            self.ui.nodesLayout.setAlignment(Qt.AlignTop)










