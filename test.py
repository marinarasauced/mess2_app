
from paramiko import SSHClient, AutoAddPolicy



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

        @return: True if SSH connection established, False otherwise.
        """
        try:
            if port == -1:
                self.ssh.connect(
                    hostname=hostname,
                    username=username,
                    password=password
                )
                self.ssh.get_transport().set_keepalive(30)
                print(self.status())
            else:
                self.ssh.connect(
                    hostname=hostname,
                    username=username,
                    password=password,
                    port=port
                )
                self.ssh.get_transport().set_keepalive(30)
            return True
        except Exception as e:
            return False


    def disconnect(self):
        """
        Closes an SSH connection with a remote host.

        @return: True if closed SSH connection, False otherwise.
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


if __name__=="__main__":
    client = SSH()
    client.connect("192.168.0.197", "ubuntu", "1234")
    client.disconnect()