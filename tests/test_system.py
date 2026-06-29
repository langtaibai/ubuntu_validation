from systemd import journal

from core.ssh_client import SSHClient
from config.config import load_config

config = load_config()
print(config)
HOST = config["host"]
USER = config["user"]
PASSWORD = config["password"]

class TestSystem:
    def __init__(self):


        self.ssh = SSHClient(
            host=HOST,
            user=USER,
            password=PASSWORD
        )

    def connect(self):
        """connect test machine"""
        self.ssh.connect()

    def disconnect(self):
        """disconnect test machine"""
        self.ssh.close()

    def check_system_status(self):
        """check system status"""
        result = self.ssh.run("systemctl is-system-running")
        status = result["stdout"].strip()
        if status == "running":
            print("PASS")
        elif status == "degraded":
            print("WARNING")
        else:
            print("FAIL")
    #    assert result["exit_code"] in [0, 1]  # degraded 也算OK

        return status

    def collect_journal(self):
        """collect journal"""
        result = self.ssh.run(
            "journalctl -p err -b --no-pager"
        )
        with open(
            "logs/journal.log",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(result["stdout"])
        print("journal.log collected")
