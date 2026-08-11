#from core.ssh_client import SSHClient
#from config.config import load_config
import time

from uvf.core.status import Teststatus
from uvf.tests.base import BaseTest
from uvf.core.test_result import TestResult

class BootTest(BaseTest):

    TAGS = ["boot"]
    def __init__(self,ssh):
        # config = load_config()
        # self.ssh = SSHClient(
        #     host=con fig["host"],
        #     user=config["user"],
        #     password=config["password"]
        # )
        super().__init__(ssh)
        #self.ssh = ssh
    # def connect(self):
    #     """connect test machine"""
    #     self.ssh.connect()
    #
    # def disconnect(self):
    #     """disconnect test machine"""
    #     self.ssh.close()

    def run(self):
        self.logger.info("start boot test")
        start = time.time()
        result = self.ssh.run(
            "systemctl is-system-running"
        )
        self.logger.info(
            f"stdout={result['stdout']}"
        )
        self.logger.info(
            f"exit={result['exit_code']}"
        )
        duration = time.time() - start
        status = result["stdout"].strip()
        if status in ["running", "degraded"]:
            return TestResult(
                name=self.__class__.__name__,
                status=Teststatus.PASS,
                duration=duration,
                message=status

            )
        else:
            return  TestResult(
                name=self.__class__.__name__,
                status=Teststatus.FAIL,
                duration=duration,
                message=status
            )


