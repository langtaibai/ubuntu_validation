class TestRunner:

    def __init__(self):
        self.tests = []
        self.results = []

    def add_test(self,test):
        """
        :param test:
        :return:
        """
        self.tests.append(test)

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