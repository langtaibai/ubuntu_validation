class BaseTest:
    """
    Base class for tests
    """
    def __init__(self, ssh):
        self.ssh = ssh
    def run(self):
        raise NotImplementedError("Test must implement run()")