import time

class TestExecutor:
    def __init__(self,retry=0):
        self.retry = retry

    def execute(self, test):
        attempts = self.retry + 1
        for i in range(attempts):
            try:
                result = test.run()
                return result
            except Exception as e:
                if i == attempts - 1:
                    raise e
                time.sleep(1)
