
from paramiko import SSHClient, AutoAddPolicy
import platform
from scp import SCPClient
import subprocess


class UIFunctionsDiagnostics():
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

        # 
        self.is_connected: bool = None
        self.is_online: bool = None


    def ui_update_name_text(self, value: str):
        """
        This method updates the actor's name text.
        """
        self.ui.name_text.setText(value)


    def ui_update_connected_to_mess2_icon(self, value: bool):
        """
        This method updates the connected to mess2 (ssh) icon.
        """
        if value != self.is_connected:
            self.is_connected = value
            style_old = self.widget.styleSheet()
            if value:
                style_new = style_old.replace(self.style_disconnected_from_mess2, self.style_connected_to_mess2)
            elif not value:
                style_new = style_old.replace(self.style_connected_to_mess2, self.style_disconnected_from_mess2)
            self.widget.setStyleSheet(style_new)

    
    def ui_disable_connected_to_mess2_icon(self):
        """
        """
        style_old = self.widget.styleSheet()
        style_new = style_old.replace(self.style_connected_to_mess2, "")
        style_new = style_new.replace(self.style_disconnected_from_mess2, "")
        self.widget.setStyleSheet(style_new)

    
    def ui_update_connected_to_network_icon(self, value: bool):
        """
        This method updates the connected to network icon.
        """
        if value != self.is_online:
            self.is_online = value
            style_old = self.widget.styleSheet()
            if value:
                style_new = style_old.replace(self.style_disconnected_from_network, self.style_connected_to_network)
            elif not value:
                style_new = style_old.replace(self.style_connected_to_network, self.style_disconnected_from_network)
            self.widget.setStyleSheet(style_new)

    
    def ui_disable_connected_to_network_icon(self):
        """
        """
        style_old = self.widget.styleSheet()
        style_new = style_old.replace(self.style_connected_to_network, "")
        style_new = style_new.replace(self.style_disconnected_from_network, "")
        self.widget.setStyleSheet(style_new)


    def ui_update_ip_text(self, value: str):
        """
        This method updates the actor's name text.
        """
        self.ui.ip_text.setText(value)


    def ui_update_battery_percentage_text(self, value: str):
        """
        This method updates the actor's battery percentage text.
        """
        self.ui.battery_text.setText(value)


class Ping():
    """
    """
    def ping(self, ip: str):
        """
        """
        if ip is not None:
            param = "-n" if platform.system().lower() == "windows" else "-c"

            try:
                response = subprocess.run(["ping", param, "1", ip],
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE,
                                          timeout=4)

                if response.returncode == 0:
                    # print(f"{ip} is online and reachable.")
                    return True
                else:
                    # print(f"{ip} is not reachable.")
                    return False
            except Exception as e:
                # print(f"Error: {e}")
                return False


class SSH():
    """
    The SSH class manages SSH connection and SCP transfers.
    """
    def __init__(self):
        """
        Initializes the SSH client and load's the system host keys.
        """
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
    

    def __del__(self):
        """
        Safely closes the SSH connection when the SSH class instance is destroyed.
        """
        self.ssh_disconnect()


    def is_active(self):
        """
        Checks if the SSH connection is active.
        """
        transport = self.ssh.get_transport()
        return transport is not None and transport.is_active()


    def ssh_connect(self, hostname: str, username: str, password: str, port: int = -1):
        """
        """
        try:
            if port == -1:
                self.ssh.connect(
                    hostname=hostname,
                    username=username,
                    password=password
                )
            else:
                self.ssh.connect(
                    hostname=hostname,
                    username=username,
                    password=password,
                    port=port
                )
            return True
        except Exception as e:
            return False
    

    def ssh_disconnect(self):
        """
        """
        if self.ssh:
            self.ssh.close()
            return True
        else:
            return False
        

    def scp_upload(self, local_path: str, remote_path: str):
        """
        """
        try:
            if not self.is_active():
                self.ssh_connect()
            scp = SCPClient(self.ssh.get_transport())
            scp.put(
                files=local_path,
                remote_path=remote_path,
                recursive=True
            )
            scp.close()
            return True
        except Exception as e:
            return False


    def scp_download(self, local_path: str, remote_path: str):
        """
        """
        try:
            if not self.is_active():
                self.ssh_connect()
            scp = SCPClient(self.ssh.get_transport())
            scp.get(
                remote_path=remote_path,
                local_path=local_path,
                recursive=True
            )
            scp.close()
            return True
        except Exception as e:
            return False