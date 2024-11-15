
from paramiko import SSHClient, AutoAddPolicy
import platform
from scp import SCPClient
import subprocess


class SSH():
    """
    Manages SSH connections to clients on a static network.
    """
    def __init__(self):
        """
        Initializes the SSH client and load's the system host keys.
        """
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())

        self.status_ssh: bool = False

    
    def __del__(self):
        """
        Safely closes the SSH connection when the SSH class instance is destroyed.
        """
        self.disconnect()


    def connect(self, hostname: str, username: str, password: str, port: int = -1):
        """
        Establishes an SSH connection with a remote host.
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


    def disconnect(self):
        """
        Closes an SSH connection with a remote host.
        """
        try:
            if self.ssh:
                self.ssh.close()
                return True
            else:
                return False
        except Exception as e:
            return False
    

    def status(self):
        """
        Checks if the SSH connection is active.
        """
        try:
            transport = self.ssh.get_transport()
            if transport is None:
                return False
            # start_time = time.time()
            # while transport.is_active():
            #     if time.time() - start_time > timeout:
            #         return False
            #     time.sleep(0.1)
            return True
        except Exception as e:
            return False


class SCP(SSH):
    """
    Manages SCP file transfers with a client on a static network.
    """
    def __init__(self):
        """
        """
        SSH.__init__(self)


    def upload(self, local_path: str, remote_path: str):
        """
        Uploads a file or directory from a local path to a client at a remote path.
        """
        try:
            if not self.status():
                self.ssh.connect()
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
    

    def download(self, local_path: str, remote_path: str):
        """
        Downloads a file or directory to a local path from a client at a remote path.
        """
        try:
            if not self.status():
                self.ssh.connect()
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


class NetworkFunctions(SCP):
    """
    Manages method's and attributes relating to network protocols.
    """
    def __init__(self):
        """
        Initializes the network functions.
        """
        SCP.__init__(self)
        self.status_network: bool = None


    def ping(self, ip: str):
        """
        Pings a static IP address on a local network to determine whether the device with that IP is online.
        """
        if ip != None:
            param = "-n" if platform.system().lower() == "windows" else "-c"
            try:
                response = subprocess.run(
                    ["ping", param, "1", ip],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=3
                )
                if response.returncode == 0:
                    return True
                else:
                    return False
            except Exception as e:
                return False
