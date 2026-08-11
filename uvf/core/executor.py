import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError

from uvf.core.exceptions import SkipTest
from uvf.core.status import Teststatus
from uvf.core.test_result import TestResult
from uvf.core.exceptions import SkipTest

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
            except SkipTest as e:
                return TestResult(
                    name=test.__class__.__name__,
                    status=Teststatus.SKIP,
                    duration=0,
                    message=str()
                )
            except TimeoutError:
                print(f"{test} timeout")
            except Exception as e:
                print(e)
        return None
