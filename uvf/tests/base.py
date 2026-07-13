from abc import ABC, abstractmethod

class BaseTest(ABC):
    """
    All tests should inherit from this class
    """
    TAGS = []

    def __init__(self, ssh):
        self.ssh = ssh

    @abstractmethod
    def run(self):
        pass