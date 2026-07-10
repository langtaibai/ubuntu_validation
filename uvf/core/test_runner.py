import importlib
import pkgutil
import uvf.tests
import inspect

class TestRunner:

    def __init__(self, ssh):
        self.tests = []
        self.results = []
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
        print(f"\n[DISCOVERY] scanning uvf.tests package\n")
        #traverse package all module
        for _, module_name, _ in pkgutil.iter_modules(uvf.tests.__path__):
            full_module_name = f"uvf.tests.{module_name}"
            module = importlib.import_module(full_module_name)
        # find class
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj):
                    if name.endswith("Test") and name != "BaseTest":
                        print(f"\n[DISCOVERY] {name}\n")
                        instance = obj(self.ssh)
                        self.tests.append(instance)

    def run_all(self):
        """
        :return:
        """
        print("\n====== UVF TEST RUNNER START ======\n")
        for test in self.tests:
            result = test.run()
            self.results.append(result)

            print(f"[{ result['name']}] {result['result']} - {result['message']}")

        print("\n====== UVF TEST RUNNER END ======\n")

        return self.results