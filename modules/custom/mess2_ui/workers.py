
from PySide6.QtCore import QRunnable

from concurrent.futures import ThreadPoolExecutor
from typing import List

from modules.custom.mess2_ui.sensor import *
from modules.custom.mess2_ui.actor import *


class Worker_mess2CheckNetworkConnection(QRunnable):
    """
    """
    def __init__(self, sensors: List[Sensor], ugvs: List[Actor], uavs: List[Actor]):
        """
        """
        super().__init__()
        self.sensors = sensors
        self.ugvs = ugvs
        self.uavs = uavs
        self.devices = self.sensors + self.ugvs + self.uavs


    def run(self):
        """
        """
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(device.ping, device.ip): device for device in self.devices}

        for future in futures:
            device = futures[future]
            result = future.result()
            try:
                device.ui_update_connected_to_network_icon(result)
            except:
                pass
