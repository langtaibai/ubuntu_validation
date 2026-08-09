from abc import ABC, abstractmethod
from uvf.logger.logger import get_logger

class BaseTest(ABC):
    """
    All tests should inherit from this class
    """
    TAGS = []

    def __init__(self, ssh):
        self.ssh = ssh
        self.logger = get_logger(
            self.__class__.__name__
        )

    @abstractmethod
    def run(self):
        """
        return TestResult
        """
        pass