

class Sensor():
    """
    """
    def __init__(self):
        """
        """
        super().__init__()

        self.name = None
        self.ip = None

        self.is_connected = False
        self.is_online = False
        self.is_running = False

        self.display_connected = False
        self.display_online = False

        self.btnName: str = None
        self.frameName: str = None
        self.frameNameOnline: str = None
        self.frameNameConnected: str = None


class SensorVICON(Sensor):
    """
    """
    def __init__(self, name: str, btnName: str):
        """
        """
        super().__init__()

        self.name = name
        self.btnName = btnName
        self.frameName = self.btnName.replace("btn", "frame")
        self.frameNameOnline = self.frameName + "Online"
        self.frameNameConnected = self.frameName + "Connected"

        
class SensorFLIR(Sensor):
    """
    """
    def __init__(self, name: str, ip: str):
        """
        """
        super().__init__()

        self.name = name
        self.ip = ip

        self.display_connected = True
        self.display_online = True