
from paramiko import SSHClient, AutoAddPolicy
import platform
import psutil
from scp import SCPClient
import subprocess
import os
import signal

import launch
import launch_ros.actions
from launch import LaunchDescription
from launch import LaunchService


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
            if self.ssh.get_transport() == None:
                return False
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


class ROS2Local():
    """
    Manages ROS2 command execution and termination on the local device. 
    """
    def start(self, device, priority: int):
        """
        Starts ROS2 nodes on the device based on the given priority.
        """
        if priority == 1:
            commands = device.commands1
        elif priority == 2:
            commands = device.commands2
        for command in commands:
            command_ = command.split()
            process = subprocess.Popen(command_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setpgrp)
            device.logger.log(f"{device.name} started \"{command}\" as process {process.pid}")
            if priority == 1:
                device.processes1.append(process)
            elif priority == 2:
                device.processes2.append(process)


    def stop(self, device, priority: int):
        """
        Terminates the processes associated with the given priority on the device, including child processes.
        """
        if priority == 1:
            processes = device.processes1
        elif priority == 2:
            processes = device.processes2
        removable = []
        for process in processes:
            os.killpg(process.pid, signal.SIGTERM)
            device.logger.log(f"{device.name} stopped process {process.pid}")
            removable.append(process)
        for process in removable:
            if priority == 1:
                device.processes1.remove(process)
            elif priority == 2:
                device.processes2.remove(process)



        # if priority not in device.pids or not device.pids[priority]:
        #     return

        # for pid in device.pids[priority]:
        #     try:
        #         parent_process = psutil.Process(pid)

        #         for child in parent_process.children(recursive=True):
        #             if 'grep' not in child.name():
        #                 child.terminate()

        #         parent_process.terminate()
        #         parent_process.wait(timeout=1)

        #         if parent_process.is_running():
        #             print(f"Process {pid} is still running after graceful termination, force killing.")
        #             parent_process.kill()

        #         result = subprocess.run(f"ps -p {pid}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #         if result.returncode == 0:
        #             print(f"Process {pid} is still running after SIGKILL.")
        #         else:
        #             print(f"Process {pid} successfully terminated.")

        #         device.pids[priority].remove(pid)
        #     except psutil.NoSuchProcess:
        #         print(f"Process with PID {pid} no longer exists.")
        #     except psutil.AccessDenied:
        #         print(f"Access denied while trying to terminate PID {pid}.")
        #     except Exception as e:
        #         print(f"Error terminating process with PID {pid}: {e}")

        # print(f"All processes for device {device.name} with priority {priority} have been stopped.")


class ROS2Remote():
    """
    Manages ROS2 command execution and termination on the local device. 
    """
    def start(self, device, priority: int):
        """
        """
        # if priority == 1:
        #     commands = device.commands1
        # elif priority == 2:
        #     commands = device.commands2
        
        # if not device.network.status():
        #     device.logger.log(f"unable to execute commands on {device.name}")
        #     return
        
        # device.pids = {}

        # for command in commands:
        #     command_ = f"{' '.join(command)} & echo $!"
        #     stdin, stdout, stderr = device.network.ssh.exec_command(command_)
        #     pid = stdout.read().decode().strip()
        #     device.pids[priority] = device.pids.get(priority, [])
        #     device.pids[priority].append(pid)


    def stop(self, device, priority: int):
        """
        Terminates the processes associated with the given priority.
        """
        # if priority not in device.pids or not device.pids[priority]:
        #     return

        # for pid in device.pids[priority]:
        #     try:
        #         command = f"kill {pid}"
        #         stdin, stdout, stderr = device.network.ssh.exec_command(command)
        #         device.pids[priority].remove(pid)
        #     except ProcessLookupError:
        #         # print(f"Process with PID {pid} not found.")
        #         pass
        #     except Exception as e:
        #         # print(f"Error terminating process with PID {pid}: {e}")
        #         pass

        # device.pids[priority] = []


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
        self.local = ROS2Local()
        self.remote = ROS2Remote()


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
