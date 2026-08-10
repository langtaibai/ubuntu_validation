import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError

class TestExecutor:
    def __init__(self,retry=0, timeout=60):
        self.retry = retry
        self.timeout = timeout

    def execute(self, test):
        attempts = self.retry + 1
        for i in range(attempts):
            try:
                with ThreadPoolExecutor(max_workers=attempts) as pool:
                    future = pool.submit(test.run)
                    result = future.result(timeout=self.timeout)
                    return result
            except TimeoutError:
                print(f"{test} timeout")
            except Exception as e:
                print(e)
        return None
