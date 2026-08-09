from reporters.base_reporter import BaseReporter

class TerminalReporter(BaseReporter):
    def generate(self, results):
        print("=" * 50)
        print("UVF Test Report")
        print("=" * 50)
        for result in results:
            print(
                f"{result.status:6}"
                f"{result.name:25}"
                f"{result.duration:.2f}s"
            )