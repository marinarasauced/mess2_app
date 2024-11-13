
from PySide6.QtCore import QRunnable

from concurrent.futures import ThreadPoolExecutor
import platform
import subprocess
from typing import List

from modules.custom.mess2_ui.sensor import *
from modules.custom.mess2_ui.actor import *


class Worker_mess2CheckNetworkConnection(QRunnable):
    """
    """
    def __init__(self, sensors: List[Obj_mess2Sensor], ugvs: List[Obj_mess2Actor], uavs: List[Obj_mess2Actor]):
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
            futures = {executor.submit(self.ping, device): device for device in self.devices}

        for future in futures:
            device = futures[future]
            result = future.result()
            try:
                device.ui_update_connected_to_network_icon(result)
            except:
                pass

    def ping(self, device):
        """
        """
        if device.ip is not None:
            param = "-n" if platform.system().lower() == "windows" else "-c"

            try:
                response = subprocess.run(["ping", param, "1", device.ip],
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE,
                                          timeout=4)

                if response.returncode == 0:
                    print(f"{device.ip} is online and reachable.")
                    return True
                else:
                    print(f"{device.ip} is not reachable.")
                    return False
            except Exception as e:
                print(f"Error: {e}")
                return False


    def ui_update_network_connection_icons(self, device, result: bool):
        """
        """
        



# class Signal_mess2CheckNetworkConnection(QObject):
#     """
#     """
#     signal = pyqtSignal(str)


# class Worker_mess2CheckNetworkConnection(QRunnable):
#     """
#     """
#     def __init__(self): #, sensors: List[Obj_mess2Sensor], ugvs: List[Obj_mess2Actor], uavs: List[Obj_mess2Actor]
#         """
#         """
#         super().__init__()
#         # self.sensors = sensors
#         # self.ugvs = ugvs
#         # self.uavs = uavs
#         self.signals = Signal_mess2CheckNetworkConnection()


#     @pyqtSlot()
#     def run(self):
#         """
#         """
#         # for sensor in self.sensors:
#         #     print(sensor.sensor_ip)
#         print("hi")
#         self.signals.signal.emit("thread test")
