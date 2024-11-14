
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget

from modules.custom.mess2_ui.common import *
from modules.custom.mess2_ui.ui_tileDiagnosticsUGV import *


class Actor(UIFunctionsDiagnostics, Ping):
    """
    """
    def __init__(self, actor_type: str, actor_name: str, actor_ip: str = ""):
        """
        """
        super().__init__()
        assert(actor_type is not None and actor_type != "")
        assert(actor_name is not None and actor_name != "")

        self.type = actor_type
        self.name = actor_name
        self.ip = actor_ip
        self.widget = QWidget()
        self.ui = None

        self.ui_category = self.ui_lookup_widget_category(self.type)
        self.ui_layout = self.ui_lookup_diagnostics_layout(self.type)

        self.counter_displayed_nodes = 0
        self.show()


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
        self.widget.setObjectName(f"{self.type}Actor{self.name}")
        if self.ui_category == "null":
            pass
        else:
            self.ui = eval(f"{self.ui_category}()")
            self.ui.setupUi(self.widget)
            self.ui_update_name_text(self.name)
            self.ui_update_ip_text(self.ip)
            self.ui_update_battery_percentage_icon(-2.0)
            self.ui_update_battery_percentage_text("n/a")
            self.ui.battery_text.setAlignment(Qt.AlignRight)
            self.ui.nodesLayout.setAlignment(Qt.AlignTop)










