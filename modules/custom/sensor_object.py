
from modules.custom.settings import Obj_settings


class Obj_tileSensorTemplate(Obj_settings):
    """
    """
    def __init__(self, sensor_name: str = "", sensor_ip: str = "", widget_name: str = None, show_connected: bool = False, show_online: bool = False):
        """
        """
        super().__init__()

        self.sensor_name = sensor_name
        self.sensor_ip = sensor_ip
        self.widget_name = widget_name

        self.show_connected = show_connected
        self.show_online = show_online
