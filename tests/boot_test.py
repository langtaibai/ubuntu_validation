from core.ssh_client import SSHClient
from config.config import load_config

class BootTest:
    def __init__(self,ssh):
        # config = load_config()
        # self.ssh = SSHClient(
        #     host=config["host"],
        #     user=config["user"],
        #     password=config["password"]
        # )
        self.ssh = ssh
    # def connect(self):
    #     """connect test machine"""
    #     self.ssh.connect()
    #
    # def disconnect(self):
    #     """disconnect test machine"""
    #     self.ssh.close()

    def run(self):
        result = self.ssh.run(
            "systemctl is-system-running"
        )
        status = result["stdout"].strip()
        if status == "running":
            return {
                "name": "Boot Test",
                "result": "PASS",
                "message": "System is running"
            }
        elif status == "degraded":
            return {
                "name": "Boot Test",
                "result": "WARNING",
                "message": "System is degraded"
            }
        else:
            return {
                "name": "Boot Test",
                "result": "FAIL",
                "message": "System is not running"
            }