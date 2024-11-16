
from PySide6.QtWidgets import QPlainTextEdit

from datetime import datetime


class LoggerUI():
    """
    Manages the ui attributes and methods for a custom terminal logger in the mess2 app.
    """
    def __init__(self, logger: QPlainTextEdit):
        """
        """
        self.logger = logger


    def log(self, value: str=""):
        """
        """
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        message = f"{timestamp} : {value}"

        if self.logger != None:
            self.logger.appendPlainText(message)
            self.logger.verticalScrollBar().setValue(self.logger.verticalScrollBar().maximum())
