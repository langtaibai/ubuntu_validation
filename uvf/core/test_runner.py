import importlib
import pkgutil
import time

import uvf.tests
import inspect
from core.test_result import TestResult
from core.test_session import TestSession
from reporters.json_reporter import JsonReporter
from reporters.terminal_reporter import TerminalReporter
from core.status import Teststatus

class TestRunner:

    def __init__(self, ssh):
        self.tests = []
        #self.results = []
        self.session = TestSession()
        self.selected_tests = []
        self.ssh = ssh

    # def add_test(self,test):
    #     """
    #     :param test:
    #     :return:
    #     """
    #     self.tests.append(test)

    def auto_discovery(self):
        """
        auto discovery all Test case by scanning all sub modules
        :param test_dir:
        :return:
        """
        #print(f"\n[DISCOVERY] scanning uvf.tests package\n")
        #traverse package all module
        for _, module_name, _ in pkgutil.iter_modules(uvf.tests.__path__):
            full_module_name = f"uvf.tests.{module_name}"
            module = importlib.import_module(full_module_name)
        # find class
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj):
                    if name.endswith("Test") and name != "BaseTest":
                        #print(f"\n[DISCOVERY] {name}\n")
                        instance = obj(self.ssh)
                        self.tests.append(instance)

    def select_tests(self, tag=None):
        if tag is None:
            self.selected_tests = self.tests.copy()
            return
        self.selected_tests = []
        for test in self.tests:
            if tag in test.TAGS:
                self.selected_tests.append(test)

    def _summary(self):
        self.session.total = len(self.session.results)
        self.session.passed = sum(
            1
            for r in self.session.results
            if r.status == Teststatus.PASS
        )
        self.session.failed = sum(
            1
            for r in self.session.results
            if r.status == Teststatus.FAIL
        )
        self.session.skipped = sum(
            1
            for r in self.session.results
            if r.status == Teststatus.SKIP
        )


    def run_all(self):
        """
        :return:
        """
        self.session.start_time = time.time()
        print("\n====== UVF TEST RUNNER START ======\n")
        # print(self.selected_tests)
        # print(self.select_tests)
        for test in self.selected_tests:
            # print(test.__class__.__name__)
            # print(test.TAGS)
            result = test.run()
            #self.results.append(result)
            self.session.results.append(result)
        self.session.end_time = time.time()
        self.session.duration = (
            self.session.end_time - self.session.start_time
        )
        self._summary()
        #    print(f"[{ result['name']}] {result['result']} - {result['message']}")
        # for result in self.results:
        #     print(
        #         f"[{result.status}]  "
        #         f"{result.name}   "
        #         f"{result.duration:.2f}s"
        #     )
        #reporter = TerminalReporter()
        reporter = JsonReporter()
        reporter.generate(self.session)
        print("\n====== UVF TEST RUNNER END ======\n")