
from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QPlainTextEdit

from datetime import datetime


class LoggerUI(QObject):
    """
    Manages the ui attributes and methods for a custom terminal logger in the mess2 app.
    """
    signal = Signal(str)


    def __init__(self, logger: QPlainTextEdit):
        """
        """
        super().__init__()
        self.logger = logger

        self.signal.connect(self.update)


    def log(self, value: str=""):
        """
        """
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        message = f"{timestamp} : {value}"

        self.signal.emit(message)


    def update(self, value: str):
        """
        """
        if self.logger != None:
            self.logger.appendPlainText(value)
            self.logger.verticalScrollBar().setValue(self.logger.verticalScrollBar().maximum())
